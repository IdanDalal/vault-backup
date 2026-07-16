---
type: project
created: 2026-07-15
status: active
author: jep
tags:
  - tutoring
---

# Heblish Test Recordings — Scripts (phone-ready)

Ground-truth scripts for the transcription bake-off (stock Whisper large-v3 vs ivrit.ai turbo vs Whisper Hebrish vs Meta Omnilingual, + pyannote community-1 diarization on the RTX 4090 PC). Each clip below is one code block = one tap on Obsidian's copy button → paste to WhatsApp. Labels: **ע:** = Idan · **ד:** = the partner (playing "דנה" where relevant). Text in (parentheses) is a stage direction — **don't read it aloud**.

## Recording protocol (for you, not for pasting)

- Pixel 8 Pro, **Recorder app**, phone **face-down in the corner of the table**, both speakers at real lesson distance (~1.5–2 m). Don't touch it between lines.
- **One file per clip** — five files total. Each script opens with a spoken slate ("בדיקה אחת…") so the files label themselves.
- Stay close to the script but don't restart over slips — we compare models against the *audio*, the script just guarantees every hard case gets covered. If you improvise a whole extra exchange, fine.
- Export each recording (share → audio file) into a Syncthing-synced folder.
- These are ~90 seconds each scripted + one 10–12 min improv. Total sitting: ~30 min including giggling.

## Clip 1 — pure Hebrew (~90 sec)

Purpose: Hebrew accuracy baseline. Numbers, names, and places included on purpose — ASR fumbles those first.

### Script one
בדיקה אחת.
ע: טוב, אז מה עושים בשבת? חשבתי שנצא לים בבוקר.
ד: בבוקר? אתה קם בשש, אני לא קמה לפני עשר.
ע: נתפשר על שמונה וחצי. ניקח גם את הכלב של השכנים?
ד: ברור, הם נוסעים לחתונה בחיפה ביום שישי.
ע: מעולה. תזכירי לי לקנות קפה, נגמר לנו אתמול.
ד: ולחם. ושלוש עגבניות. אני רושמת רשימה.
ע: כמה עולה החניה שם? עשרים שקל?
ד: שלושים וחמישה. העלו את המחיר אחרי פסח.
ע: לא נורמלי. טוב, אז שמונה וחצי בשבת: ים, כלב, קפה.
ד: סגור. ותביא את המטרייה הגדולה, אין צל בחוף הזה.

## Clip 2 — pure English (~90 sec)

Purpose: English baseline, Israeli accents included. Deliberately lesson-flavored vocabulary — these exact words will appear in real sessions.

Test two.
ע: Okay, let's talk about the lesson. I have a table, a chair, and a big red pencil.
ד: I like the red pencil. Can I draw a cat and a dog?
ע: Yes! Draw a black cat under the table, and a small dog on the chair.
ד: The dog is jumping! Jump, jump, jump!
ע: Very good. Now stand up, touch something blue, and sit down.
ד: I touch the blue book. Easy!
ע: What's your name? How are you? How old are you?
ד: My name is Dana. I'm fine. I am nine years old.
ע: One, two, three, four, five, six, seven, eight, nine, ten.
ד: Hello, goodbye, please, thank you, see you later!

## Clip 3 — dense Heblish (~2 min) — the money clip

Purpose: the exact texture of a real lesson — Hebrew matrix, English islands of every kind: single embedded words, question-answer language switches, spelled letters, mixed-language counting.

בדיקה שלוש.
ע: טוב דנה, תגידי אחריי: jump!
ד: !Jump זה אומר לקפוץ, נכון?
ע: בדיוק. ואיך אומרים כלב באנגלית?
ד: !Dog יש לנו dog בבית, קוראים לו רקסי.
ע: יפה מאוד. What's your name?
ד: קוראים לי דנה. אה, רגע — !my name is Dana
ע: מעולה. עכשיו בואי נאיית: C-A-T. מה יצא לנו?
ד: !Cat חתול! אני יודעת גם B-Y-E, זה ביי.
ע: וכמה זה three ועוד four?
ד: שבע! אה, באנגלית — !seven
ע: תראי את התמונה: יש פה one, two, three ילדים, ועוד שני dogs.
ד: והילדה הקטנה אומרת hello לאבא שלה.
ע: נכון מאוד. עכשיו sit down בבקשה, ונעשה עוד משחק אחד.
ד: רק אם אחר כך יש story! אני הכי אוהבת סיפורים באנגלית.

## Clip 4 — lesson hazards (~2 min)

Purpose: the acoustic edge cases a real kid produces — deliberate mispronunciations, singing, overlap, whispering, laughter, distance. This clip decides which model degrades gracefully.

בדיקה ארבע.
ע: עכשיו תדברי כמו ילדה קטנה שטועה בכוונה.
ד: (בקול ילדותי) !Dis is my dod! I like de wed color
ע: (מתקן בעדינות) Dog. Red. תנסי שוב.
ד: (צוחקת חזק) !Doooog! Wwwed... רגע — red
ע: (שר) ...Hello, it's me... I was wondering
ד: (מצטרפת לשירה) !Hello from the other siiiide
(חמש שניות: שניכם מדברים בו-זמנית — הוא בעברית על מזג האוויר, היא סופרת באנגלית עד עשר)
ע: (לוחש) ...and now we whisper... one, two, three
ד: (לוחשת) ...I can hear you
ע: (הולך לקצה השני של החדר וקורא משם) !Very good! Excellent! You are the champion
ד: (צועקת בחזרה) !Thank you תחזור, לא שומעים אותך!

## Clip 5 — lesson sim (10–12 min, improvised by this beat list)

Purpose: realism the scripts can't give — pacing, movement noise, position drift, and one full minute of near-silence (the classic Whisper hallucination trap: we need to see which model invents sentences there).

בדיקה חמש — שיעור מדומה. לאלתר לפי הרשימה, בערך:
1. פתיחה (דקה) — "!Hello" ואז סמול-טוק בעברית.
2. ציד אוצר (2 דק') — ע' שואל "מה את הכי אוהבת לעשות?" ומוצאים ביחד מילים באנגלית בתוך התשובה.
3. סיימון סייז עם תנועה אמיתית (2 דק') — לקום, לקפוץ, לגעת בדברים. שהכיסאות יחרקו.
4. החלפת מקומות (דקה) — ע' רחוק מהטלפון, היא קרובה. ממשיכים לדבר.
5. שקט (דקה שלמה! חשוב) — "מציירים" בלי לדבר. מקסימום מלמול פה ושם.
6. סיפור קצר באנגלית (2-3 דק') — ע' מספר לאט, היא מפריעה עם שאלות בעברית.
7. פרידה (חצי דקה) — "!Bye! See you" וצחוקים.

## After recording

Five audio files → Syncthing folder → tell jep. The bake-off harness (four ASR models + pyannote community-1) gets built on the 4090 PC, each model transcribes all five clips, and we read the Clip 3 + Clip 4 outputs side by side against these scripts. Winner becomes the `lesson-transcribe` pipeline; Clip 5 settles diarization and hallucination behavior.
