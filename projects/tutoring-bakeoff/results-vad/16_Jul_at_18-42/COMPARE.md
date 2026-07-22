# 16 Jul at 18-42.m4a — side by side

Diarization: **2 speakers detected** (expected 2), 16 turns.

## stock-large-v3 (5s)

[00:05] SPEAKER_00: טוב, אז מה עושים בשבת?
[00:08] SPEAKER_00: בדיקה אחת
[00:10] SPEAKER_00: טוב, אז מה עושים בשבת? חשבתי שנצא לים בבוקר
[00:15] SPEAKER_01: בבוקר? אתה קם בשש, אני לא קמה לפני עשר
[00:19] SPEAKER_00: נתפשר על שמונה וחצי, ניקח גם את הכלב של השכנים?
[00:26] SPEAKER_01: ברור, הם נושאים לחתונה בחיפה ביום שישי
[00:29] SPEAKER_00: מעולה, תזכירי לי לקנות קפה, נגמר לנו אתמול
[00:34] SPEAKER_01: ולחר, ושלוש עגבניות, אני רושמת רשימה
[00:38] SPEAKER_00: כמה עולה הכניה שם? עשרים שקל?
[00:42] SPEAKER_01: שלושים וחמישה, העלו את המחיר אחרי פסק
[00:45] SPEAKER_00: לא נורמלי, טוב, אז שמונה וחצי בשבת, ים, כלב, קפה
[00:51] SPEAKER_01: סגור, ותביא איתך את המטריה הגדולה, אין צל בחוף הזה

## ivrit-turbo (4s)

[00:05] SPEAKER_00: טוב, אז מה עושים בשבת? בדיקה אחת, לא? אה, בדיקה אחת.
[00:11] SPEAKER_00: טוב, אז מה עושים בשבת?
[00:13] SPEAKER_00: חשבתי שנצא לים בבוקר.
[00:16] SPEAKER_01: בבוקר, אתה קו בשש, אני לא קמה לפני עשר.
[00:21] SPEAKER_00: נתפשר על שמונה וחצי.
[00:23] SPEAKER_00: ניקח גם את הכלב של השכנים?
[00:27] SPEAKER_01: ברור, הם נוסעים לחתונה בחיפה ביום שישי.
[00:30] SPEAKER_00: מעולה.
[00:31] SPEAKER_00: תזכירי לי לקנות קפה, נגמר לנו את וואן.
[00:35] SPEAKER_01: ולחם.
[00:36] SPEAKER_01: ושלוש עגבניות.
[00:37] SPEAKER_01: אני רושמת רשימה.
[00:39] SPEAKER_00: כמה עולה החניה שם?
[00:40] SPEAKER_00: עשרים שקל?
[00:42] SPEAKER_01: שלושים וחמישה. העלו את המחיר אחרי פזל.
[00:45] SPEAKER_00: לא נורמלי.
[00:47] SPEAKER_00: טוב, אז שמונה וחצי בשבת,
[00:50] SPEAKER_00: ים, כלב, קפה.
[00:52] SPEAKER_01: סגור, ותביא איתך את המטריה הגדולה. אין צל בחוף עדיין.

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
