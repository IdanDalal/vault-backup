# 16 Jul at 18-44.m4a — side by side

Diarization: **2 speakers detected** (expected 2), 13 turns.

## stock-large-v3 (7s)

[00:05] SPEAKER_00: Test 2. Okay, let's talk about the lesson. I have a table, a chair, and a big red pencil.
[00:15] SPEAKER_01: I like the red pencil. Can I draw a cat and a dog?
[00:20] SPEAKER_00: Yes. Draw a black cat under the table and a small dog on the chair.
[00:26] SPEAKER_01: The dog is jumping. Jump, jump, jump.
[00:29] SPEAKER_00: Very good. Now stand up, touch something blue, and sit down.
[00:36] SPEAKER_01: I touched the blue book. Easy.
[00:39] SPEAKER_00: What's your name? How are you? How old are you?
[00:44] SPEAKER_01: My name is Dana. I'm fine. I'm 9 years old.
[00:49] SPEAKER_00: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
[00:56] SPEAKER_01: Hello. Goodbye. Please.
[00:59] SPEAKER_01: Thank you. See you later.

## ivrit-turbo (5s)

[00:01] SPEAKER_00: טסט 2. אוקיי,
[00:08] SPEAKER_00: ננסה לדבר על העברה.
[00:10] SPEAKER_00: יש לי מעל,
[00:12] SPEAKER_00: יולד ופנקול גדול.
[00:15] SPEAKER_01: אני אוהב את הפנקול גדול.
[00:17] SPEAKER_01: יכולתי להגיד אוכל ואוכל?
[00:20] SPEAKER_00: כן.
[00:21] SPEAKER_00: להגיד אוכל מישהו מישהו ללדול ואוכל מישהו מישהו ללדול.
[00:26] SPEAKER_01: הילד יולד, יולד, יולד, יולד.
[00:30] SPEAKER_00: מאוד טוב, עכשיו יולד,
[00:33] SPEAKER_00: תעשה משהו בלור,
[00:34] SPEAKER_00: וסתכל עליו.
[00:36] SPEAKER_01: אני קראת את הכל בלור,
[00:37] SPEAKER_01: קצת.
[00:40] SPEAKER_00: מה אתה מדבר?
[00:41] SPEAKER_00: איך אתם?
[00:42] SPEAKER_00: איך גדולים?
[00:44] SPEAKER_01: אני אוהב דנה.
[00:45] SPEAKER_01: אני חושבת שאני עוד 90 שנה.
[00:49] SPEAKER_00: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
[00:56] SPEAKER_01: היי, טוב, תודה, תודה, תודה רבה.

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
