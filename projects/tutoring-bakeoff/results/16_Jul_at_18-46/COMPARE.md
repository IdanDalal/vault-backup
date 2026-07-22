# 16 Jul at 18-46.m4a — side by side

Diarization: **2 speakers detected** (expected 2), 24 turns.

## stock-large-v3 (25s)

[00:00] SPEAKER_01: בדיקה שלוש
[00:13] SPEAKER_00: טוב דנה, תגידי אחריי
[00:16] SPEAKER_00: ג'אמפ
[00:17] SPEAKER_01: ג'אמפ, זה אומר לקפוץ, נכון?
[00:21] SPEAKER_00: בדיוק, ואיך אומרים כלב באנגלית?
[00:25] SPEAKER_01: דוג, יש לנו דוג בבית, קוראים לו רקסי
[00:28] SPEAKER_00: יפים, יפים
[00:29] SPEAKER_00: יפה מאוד, what's your name?
[00:32] SPEAKER_01: קוראים לי דנה
[00:33] SPEAKER_01: אה, רגע, my name is דנה
[00:37] SPEAKER_00: מעולה, עכשיו בואי נעיית
[00:40] SPEAKER_00: C-A-T, מה יצא לנו?
[00:45] SPEAKER_01: קט, חתול, אני יודעת גם
[00:48] SPEAKER_01: B-Y-E, זה בי
[00:52] SPEAKER_00: וכמה זה 3 ועוד 4?
[00:58] SPEAKER_01: שבע
[00:59] SPEAKER_01: אם
[00:59] SPEAKER_01: באנגלית זה סבר?
[01:03] SPEAKER_00: תראי את התמונה
[01:04] SPEAKER_00: יש פה
[01:05] SPEAKER_00: 1, 2, 3 ילדים
[01:08] SPEAKER_00: ועוד שני דורס
[01:10] SPEAKER_01: והילדה הקטנה אומרת
[01:13] SPEAKER_01: הלו לאבא שלה
[01:14] SPEAKER_00: נכון מאוד
[01:16] SPEAKER_00: עכשיו, sit down בבקשה
[01:18] SPEAKER_00: ונעשה עוד משחק אחד
[01:20] SPEAKER_01: רק אם אחר כך יש
[01:23] SPEAKER_01: סטורי
[01:24] SPEAKER_01: אני הכי אוהבת סיפורים באנגלית
[01:29] SPEAKER_01: מה הממן?
[01:32] SPEAKER_01: תודה

## ivrit-turbo (6s)

[00:00] ?: בדיקה שלוש.
[00:15] SPEAKER_00: טוב, דנה, תגידי אחריי,
[00:17] SPEAKER_00: ג'אמפ.
[00:18] SPEAKER_01: ג'אמפ, זה אומר לקפוץ, נכון?
[00:21] SPEAKER_00: בדיוק,
[00:22] SPEAKER_00: ואיך אומרים כלב באנגלית?
[00:25] SPEAKER_01: דוג.
[00:26] SPEAKER_01: יש לנו דוג בבית, קוראים לו רקסי.
[00:28] SPEAKER_00: יפה מאוד.
[00:31] SPEAKER_00: מה קוראים לי דנה?
[00:32] SPEAKER_01: קוראים לי דנה.
[00:34] SPEAKER_01: אה, רגע.
[00:36] SPEAKER_01: My name is דנה.
[00:38] SPEAKER_00: מעולה.
[00:39] SPEAKER_00: עכשיו בואי נאיית.
[00:41] SPEAKER_00: C-A-T.
[00:43] SPEAKER_00: מה יצא לנו?
[00:45] SPEAKER_01: קט, חתול.
[00:47] SPEAKER_01: אני יודעת גם B-Y-E. זה ביי.
[00:53] SPEAKER_00: וכמה זה 3 ועוד 4?
[00:58] SPEAKER_01: 7. אה, באנגלית 7. תראי את התמונה.
[01:04] SPEAKER_00: יש פה 1, 2, 3 ילדים ועוד 2 דומים.
[01:11] SPEAKER_01: והילדה הקטנה אומרת הלו לאבא שלה.
[01:15] SPEAKER_00: נכון מאוד.
[01:16] SPEAKER_00: עכשיו, sit down בבקשה,
[01:19] SPEAKER_00: ונעשה עוד משחק אחד.
[01:21] SPEAKER_01: רק אם אחר כך יש סטורי.
[01:25] SPEAKER_01: אני הכי אוהבת סיפורים באנגלית.
[01:28] SPEAKER_01: תודה רבה.

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
