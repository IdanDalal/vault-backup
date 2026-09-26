"""render.py - fill the slots of a ComfyUI workflow template and queue it.

Fills slots only. Never builds or edits a node graph (Studio Preflight, D3).
Talks to ComfyUI on 127.0.0.1:8188 over loopback; works from any account on this PC.

Usage (from any folder):
  python render.py --prompt "text" [--count 8] [--seed N] [--size 1024x1024]
                   [--prefix decadents/d1-crt/sweep] [--template z-image-turbo.template.json]
                   [--fetch DIR]

  --count N     N renders, each with its own random seed (or seed, seed+1, ... when --seed is given)
  --fetch DIR   also download the finished PNGs into DIR (jep cannot read the admin output folder directly)

Prints one line per render: index, seed, filename. Exit code 1 on any ComfyUI error.
"""
import argparse, json, os, random, sys, time, urllib.request, urllib.error

HOST = "http://127.0.0.1:8188"
HERE = os.path.dirname(os.path.abspath(__file__))


def api(path, data=None):
    req = urllib.request.Request(HOST + path, data=json.dumps(data).encode() if data is not None else None,
                                 headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=60))


def fill(template, prompt, seed, width, height, prefix):
    g = json.loads(json.dumps(template))
    for node in g.values():
        ct, inp = node["class_type"], node["inputs"]
        if ct == "CLIPTextEncode" and inp.get("text") == "{{PROMPT}}":
            inp["text"] = prompt
        elif ct == "KSampler":
            inp["seed"] = seed
        elif ct == "SaveImage":
            inp["filename_prefix"] = prefix
        elif "Latent" in ct:
            inp["width"], inp["height"], inp["batch_size"] = width, height, 1
    return g


def wait(prompt_id, timeout=600):
    t0 = time.time()
    while time.time() - t0 < timeout:
        h = api(f"/history/{prompt_id}")
        if prompt_id in h:
            st = h[prompt_id].get("status", {})
            if st.get("status_str") == "error":
                sys.exit("ComfyUI error: " + json.dumps(st)[:800])
            if st.get("completed"):
                return [i for o in h[prompt_id]["outputs"].values() for i in o.get("images", [])]
        time.sleep(0.5)
    sys.exit("timeout waiting for " + prompt_id)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--count", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--size", default="1024x1024")
    ap.add_argument("--prefix", default="decadents/untitled")
    ap.add_argument("--template", default=os.path.join(HERE, "z-image-turbo.template.json"))
    ap.add_argument("--fetch")
    a = ap.parse_args()
    w, h = (int(x) for x in a.size.lower().split("x"))
    template = json.load(open(a.template))
    try:
        api("/system_stats")
    except urllib.error.URLError as e:
        sys.exit(f"ComfyUI not reachable on {HOST}: {e}")
    seeds = [a.seed + i for i in range(a.count)] if a.seed is not None else [random.randint(1, 2**48) for _ in range(a.count)]
    queued = []
    for s in seeds:
        r = api("/prompt", {"prompt": fill(template, a.prompt, s, w, h, a.prefix), "client_id": "render.py"})
        if r.get("node_errors"):
            sys.exit("node_errors: " + json.dumps(r["node_errors"])[:800])
        queued.append((s, r["prompt_id"]))
    t0 = time.time()
    if a.fetch:
        os.makedirs(a.fetch, exist_ok=True)
    for i, (s, pid) in enumerate(queued, 1):
        for img in wait(pid):
            print(f"{i}\t{s}\t{img['subfolder']}/{img['filename']}")
            if a.fetch:
                url = f"{HOST}/view?filename={img['filename']}&subfolder={img['subfolder']}&type=output"
                open(os.path.join(a.fetch, img["filename"]), "wb").write(urllib.request.urlopen(url, timeout=60).read())
    print(f"# {len(queued)} render(s) in {time.time() - t0:.1f}s, output folder: ComfyUI output/{a.prefix.rsplit('/', 1)[0]}", file=sys.stderr)


if __name__ == "__main__":
    main()
