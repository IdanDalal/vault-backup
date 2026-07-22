# 16 Jul at 18-46.m4a — side by side

Diarization: **2 speakers detected** (expected 2), 24 turns.

## stock-large-v3 (9s)

[00:03] SPEAKER_01: בדיקה שלוש
[00:13] SPEAKER_00: טוב, דנה, תגידי אחריי
[00:17] SPEAKER_00: Jump
[00:17] SPEAKER_01: Jump, זה אומר לקפוץ, נכון?
[00:21] SPEAKER_00: בדיוק
[00:22] SPEAKER_00: ואיך אומרים כלב באנגלית?
[00:25] SPEAKER_01: Dog
[00:25] SPEAKER_01: יש לנו דוג בבית, קוראים לו רקסי
[00:28] SPEAKER_00: יפה מאוד
[00:30] SPEAKER_00: What's your name?
[00:31] SPEAKER_01: קוראים לי דנה
[00:33] SPEAKER_01: אה, רגע
[00:35] SPEAKER_01: My name is Dana
[00:37] SPEAKER_00: מעולה
[00:39] SPEAKER_00: עכשיו בואי נעיית
[00:40] SPEAKER_00: C-A-T
[00:43] SPEAKER_00: מה יצא לנו?
[00:45] SPEAKER_01: Cat, חתול
[00:46] SPEAKER_01: אני יודעת גם
[00:48] SPEAKER_01: B-Y-E
[00:51] SPEAKER_01: זה בי
[00:52] SPEAKER_00: וכמה זה
[00:54] SPEAKER_00: Three ועוד Four
[00:57] SPEAKER_01: שבע
[00:59] SPEAKER_01: אה, באנגלית זה
[01:00] SPEAKER_01: Seven
[01:01] SPEAKER_00: תראי את התמונה
[01:04] SPEAKER_00: יש פה One, Two, Three ילדים
[01:08] SPEAKER_00: ועוד שני Dogs
[01:10] SPEAKER_01: והילדה הקטנה אומרת Hello לאבא שלה
[01:14] SPEAKER_00: נכון מאוד
[01:16] SPEAKER_00: עכשיו Sit down בבקשה
[01:18] SPEAKER_00: ונעשה עוד משחק אחד
[01:21] SPEAKER_01: רק אם אחר כך יש סטורי
[01:24] SPEAKER_01: אני הכי אוהבת סיפורים באנגלית

## ivrit-turbo (5s)

[00:03] SPEAKER_01: בדיקה שלוש.
[00:15] SPEAKER_00: טוב, דנה, תגידי אחריי,
[00:17] SPEAKER_00: ג'אמפ.
[00:18] SPEAKER_01: ג'אמפ, זה אומר לקפוץ, נכון?
[00:21] SPEAKER_00: בדיוק,
[00:22] SPEAKER_00: ואיך אומרים כלב באנגלית?
[00:25] SPEAKER_01: דוג.
[00:26] SPEAKER_01: יש לנו דוג בבית, קוראים לו רקסי.
[00:29] SPEAKER_00: יפה מאוד.
[00:31] SPEAKER_00: מה's your name?
[00:32] SPEAKER_01: קוראים לי דנה.
[00:34] SPEAKER_01: אה, רגע.
[00:36] SPEAKER_01: My name is דנה.
[00:38] SPEAKER_00: מעולה.
[00:39] SPEAKER_00: עכשיו בואי נעיית.
[00:41] SPEAKER_00: C-A-T.
[00:43] SPEAKER_00: מה יצא לנו?
[00:45] SPEAKER_01: קט, חתול.
[00:47] SPEAKER_01: אני יודעת גם B-Y-E.
[00:51] SPEAKER_01: זה ביי.
[00:53] SPEAKER_00: וכמה זה 3 ועוד 4?
[00:58] SPEAKER_01: 7. אה, באנגלית זה 7.
[01:02] SPEAKER_00: תראי את התמונה.
[01:04] SPEAKER_00: יש פה 1, 2, 3 ילדים ועוד 2 דולס.
[01:11] SPEAKER_01: והילדה הקטנה אומרת הלו לאבא שלה.
[01:15] SPEAKER_00: נכון מאוד.
[01:16] SPEAKER_00: עכשיו, sit down בבקשה,
[01:19] SPEAKER_00: ונעשה עוד משחק אחד.
[01:21] SPEAKER_01: רק אם אחר כך יש סטורי.
[01:25] SPEAKER_01: אני הכי אוהבת סיפורים באנגלית.

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
