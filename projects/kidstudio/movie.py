"""Stitch story frames (picture + spoken line) and a song into one mp4 with ffmpeg (static binary from imageio-ffmpeg).

movie(frames, song, out_path) where frames = [(png_path, wav_path_or_None), ...]. Returns total seconds.
"""
import os, shutil, subprocess, tempfile, wave, contextlib

import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
W, H, FPS = 1280, 720, 25
BG = "#07081a"
MIN_SECS = 4.0      # a frame never shows shorter than this
TAIL = 1.2          # silence after the spoken line
SONG_VOL = 0.22


def wav_len(path):
    try:
        with contextlib.closing(wave.open(path)) as w:
            return w.getnframes() / w.getframerate()
    except Exception:
        return 0.0


def run(args, timeout=240):
    r = subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", *args], capture_output=True, text=True, timeout=timeout)
    if r.returncode:
        raise RuntimeError("ffmpeg: " + r.stderr.strip()[-400:])


def clip(img, wav, out, i):
    """One frame: slow zoom in on even frames, slow zoom out on odd ones. Upscaled 2x before zoompan against jitter."""
    dur = max(MIN_SECS, wav_len(wav) + TAIL if wav else MIN_SECS)
    n = int(dur * FPS)
    pre = f"scale=w={W*2}:h={H*2}:force_original_aspect_ratio=decrease,pad={W*2}:{H*2}:(ow-iw)/2:(oh-ih)/2:color={BG},"
    if i % 2 == 0:
        zp = f"zoompan=z='min(zoom+0.0010,1.22)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS}"
    else:
        zp = f"zoompan=z='if(lte(on,1),1.22,max(1.0,zoom-0.0010))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS}"
    vf = pre + zp + ",format=yuv420p"
    args = ["-i", img]
    args += ["-i", wav] if wav else ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo"]
    args += ["-filter_complex", f"[0:v]{vf}[v];[1:a]aresample=44100,aformat=channel_layouts=stereo,apad[a]",
             "-map", "[v]", "-map", "[a]", "-t", f"{dur:.2f}",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "128k", out]
    run(args)
    return dur


def movie(frames, song, out_path):
    tmp = tempfile.mkdtemp(prefix="story-")
    try:
        clips, total = [], 0.0
        for i, (img, wav) in enumerate(frames):
            c = os.path.join(tmp, f"clip{i}.mp4")
            total += clip(img, wav, c, i)
            clips.append(c)
        lst = os.path.join(tmp, "list.txt")
        with open(lst, "w", encoding="utf-8") as f:
            for c in clips:
                f.write("file '" + c.replace("\\", "/").replace("'", "'\\''") + "'\n")
        story = os.path.join(tmp, "story.mp4")
        run(["-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", story])
        if song and os.path.exists(song):
            fade = max(0.0, total - 1.5)
            run(["-i", story, "-stream_loop", "-1", "-i", song, "-filter_complex",
                 f"[1:a]aresample=44100,aformat=channel_layouts=stereo,volume={SONG_VOL}[bg];"
                 f"[0:a][bg]amix=inputs=2:duration=first:dropout_transition=0,afade=t=out:st={fade:.2f}:d=1.5[a]",
                 "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-t", f"{total:.2f}", out_path])
        else:
            shutil.copy(story, out_path)
        return total
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    import sys, time
    imgs = [a for a in sys.argv[1:] if a.lower().endswith(".png")]
    wavs = [a for a in sys.argv[1:] if a.lower().endswith(".wav")]
    t0 = time.time()
    secs = movie([(im, wavs[i % len(wavs)] if wavs else None) for i, im in enumerate(imgs)], wavs[0] if wavs else None, "test-movie.mp4")
    print(f"{secs:.1f} s of video in {time.time()-t0:.1f} s -> test-movie.mp4")
