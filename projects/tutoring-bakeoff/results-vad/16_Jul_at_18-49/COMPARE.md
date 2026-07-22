# 16 Jul at 18-49.m4a — side by side

Diarization: **3 speakers detected** (expected 2), 34 turns.

## stock-large-v3 (21s)

[00:00] SPEAKER_02: בדיקה ארבע
[00:05] SPEAKER_00: בדיקה ארבע
[00:07] SPEAKER_00: עכשיו תדברי כמו ילדה קטנה שטועה בכוונה
[00:11] SPEAKER_02: This is my dog
[00:13] SPEAKER_02: I like the red color
[00:17] SPEAKER_00: דוג
[00:18] SPEAKER_00: רד
[00:19] SPEAKER_00: תנסי שוב
[00:24] SPEAKER_02: דוג
[00:25] SPEAKER_02: רד
[00:27] SPEAKER_02: רגע
[00:28] SPEAKER_02: רד
[00:31] SPEAKER_01: Hello
[00:32] SPEAKER_01: It's me
[00:34] SPEAKER_01: I was wondering
[00:37] SPEAKER_02: Hello from the other side
[00:41] SPEAKER_00: היום היה ממש חם
[00:45] SPEAKER_00: ומחר יהיה ממש חם
[00:48] SPEAKER_00: וכשעוד אני אעבור אנחנו לא יפתיק להלווה
[00:50] SPEAKER_00: על כמה שהיה ממש ממש ממש חם
[00:53] SPEAKER_00: ואני מופתע אם לא יהיה
[00:56] SPEAKER_00: סיעים של חום כל השבוע
[01:01] SPEAKER_00: And now we whisper
[01:13] SPEAKER_01: Very good
[01:15] SPEAKER_01: Excellent
[01:17] SPEAKER_01: You are the champion
[01:21] SPEAKER_02: Thank you
[01:22] SPEAKER_02: תחזור רצו ממתך

## ivrit-turbo (4s)

[00:00] SPEAKER_00: בדיקה 4. בדיקה 4. עכשיו תדברי כמו ילדה קטנה שטועה בכוונה.
[00:11] SPEAKER_02: This is my dog.
[00:13] SPEAKER_02: I like a wet collar.
[00:17] SPEAKER_00: dog?
[00:18] SPEAKER_00: Red.
[00:20] SPEAKER_00: תנסי שוב.
[00:21] SPEAKER_02: דוג,
[00:26] SPEAKER_02: וד, רגע,
[00:28] SPEAKER_02: רד.
[00:29] SPEAKER_01: Hello, it's me.
[00:35] SPEAKER_01: I was wondering.
[00:37] SPEAKER_02: Hello, from the other side.
[00:43] SPEAKER_00: היום היה ממש חם.
[00:45] SPEAKER_00: 1, 2, 3, וכשעוגר יבוא, הוא לא יפסיק לעגוע.
[00:51] SPEAKER_00: 5, ואני מופתע אם לא יהיה שיאים של חום כל השבוע.
[01:01] SPEAKER_00: And now we whisper Very good.
[01:15] SPEAKER_01: Excellent.
[01:17] SPEAKER_01: You are the champion.
[01:21] SPEAKER_02: Thank you.
[01:22] SPEAKER_02: תחזור, לא שומעים אותך.

## hebrish

_hebrish FAILED: Could not load libtorchcodec. Likely causes:
          1. FFmpeg is not properly installed in your environment. We support
             versions 4, 5, 6, 7, and 8, and we attempt to load libtorchcodec
             for each of those versions. Errors for versions not installed on
             your system are expected; only the error for your installed FFmpeg
             version is relevant. On Windows, ensure you've installed the
             "full-shared" version which ships DLLs.
          2. The PyTorch version (2.13.0+cu126) is not compatible with
             this version of TorchCodec. Refer to the version compatibility
             table:
             https://github.com/pytorch/torchcodec?tab=readme-ov-file#installing-torchcodec.
          3. Another runtime dependency; see exceptions below.

        The following exceptions were raised as we tried to load libtorchcodec:
        
[start of libtorchcodec loading traceback]
FFmpeg version 8:
Traceback (most recent call last):
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torch\_ops.py", line 1516, in load_library
    ctypes.CDLL(path)
  File "C:\Users\Idi\AppData\Local\Programs\Python\Python312\Lib\ctypes\__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: Could not find module 'C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\libtorchcodec_core8.dll' (or one of its dependencies). Try using the full path with constructor syntax.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torch\_ops.py", line 1518, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\libtorchcodec_core8.dll

FFmpeg version 7:
Traceback (most recent call last):
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torch\_ops.py", line 1516, in load_library
    ctypes.CDLL(path)
  File "C:\Users\Idi\AppData\Local\Programs\Python\Python312\Lib\ctypes\__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: Could not find module 'C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\libtorchcodec_core7.dll' (or one of its dependencies). Try using the full path with constructor syntax.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torch\_ops.py", line 1518, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\libtorchcodec_core7.dll

FFmpeg version 6:
Traceback (most recent call last):
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torch\_ops.py", line 1516, in load_library
    ctypes.CDLL(path)
  File "C:\Users\Idi\AppData\Local\Programs\Python\Python312\Lib\ctypes\__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: Could not find module 'C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\libtorchcodec_core6.dll' (or one of its dependencies). Try using the full path with constructor syntax.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torch\_ops.py", line 1518, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\libtorchcodec_core6.dll

FFmpeg version 5:
Traceback (most recent call last):
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torch\_ops.py", line 1516, in load_library
    ctypes.CDLL(path)
  File "C:\Users\Idi\AppData\Local\Programs\Python\Python312\Lib\ctypes\__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: Could not find module 'C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\libtorchcodec_core5.dll' (or one of its dependencies). Try using the full path with constructor syntax.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torch\_ops.py", line 1518, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\libtorchcodec_core5.dll

FFmpeg version 4:
Traceback (most recent call last):
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torch\_ops.py", line 1516, in load_library
    ctypes.CDLL(path)
  File "C:\Users\Idi\AppData\Local\Programs\Python\Python312\Lib\ctypes\__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: Could not find module 'C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\libtorchcodec_core4.dll' (or one of its dependencies). Try using the full path with constructor syntax.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\_internally_replaced_utils.py", line 93, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "C:\tutoring-bakeoff\venv\Lib\site-packages\torch\_ops.py", line 1518, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: C:\tutoring-bakeoff\venv\Lib\site-packages\torchcodec\libtorchcodec_core4.dll
[end of libtorchcodec loading traceback]._ (optional model, skipped)
