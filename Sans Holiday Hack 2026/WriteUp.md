# SANS Holiday Hack Challenge 2026

https://2026.holidayhackchallenge.com/

----
## List of Challenges (badge order)
1. Holiday Hack Orientation ✅
2. SQL Injection ✅
3. Holiday Hack Hero ✅
4. Reversing Introduction ✅
5. Buffer Overflow
6. The Shared Responsibility Sorting Game
7. Holiday Portal
8. 3D Jigsaw Pyramid
9. Santa's Game of Ice
10. CLI Whetstone
11. Holiday Hack Z: Freezer Dream Tournament
12. 5n4ck3y
13. Cold Trail
14. 3D Printer
15. DTMF
16. Race Condition
17. SARIF ✅

----
## 1. Holiday Hack Orientation

Jingle Ringford (Orientation area) asks you to "prove you're human" on the terminal beside him.
The terminal is a parody CAPTCHA ("HumanCHECK, homemade by Jingle"). Tick **I am a human** and you're through.

Lesson: in almost every challenge you find the elf, click the terminal next to them, and dive in.

Real world: a homemade "CAPTCHA" whose only rule is "robots please don't click" is security theater. Real bot checks (reCAPTCHA, Turnstile) score browser signals server-side; a checkbox the client controls stops nothing.

----
## 2. SQL Injection

Antechamber, Sparkle Redberry. Angel and Tinsel are locked out of the **North Pole Task Tracker**. Get back in and recover both to-do lists.

**Step 1: find a real username (user enumeration).**
- The login rejects non-alphanumeric usernames, so the username field isn't injectable.
- Sign-up needs an invite code, but the sign-up page's JavaScript checks names as you type with `GET /check-username?username=X` → `{"available": true|false}`. That endpoint needs **no invite code**.
- `Angel` → available, `angel` → **taken**. Usernames are case-sensitive.

**Step 2: login bypass via the password field.** The password field isn't filtered. `' OR '1'='1` didn't work, probably because it returns every row and the app wants exactly one user. A **balanced-quote** payload (no `--` needed) pins the query to one row:

```
username: angel
password: ' OR username='angel
→ ... WHERE username='angel' AND password='' OR username='angel'
```

**Step 3: the search box leaks every user's tasks.** The search calls `GET /api/todo?search=X`, which is roughly `WHERE owner='angel' AND item LIKE '%X%'`. The query ends with `%'`, so the payload has to absorb it:

```
search: ' OR '%'='
→ ... AND item LIKE '%' OR '%'='%'      (always true → every row in the table)
```

The result shows Angel's 3 tasks plus 6 that belong to someone else (presumably Tinsel), including:
`URGENT before Christmas Eve -- confirm delivery. HHC{y0u_f0und_s0m30n3_3ls3s_t0d0_l1st}`

Completion banner: "Thanks for retrieving my TODO list items. Your progress has been saved." ✅

Lessons:
- Validating one field (username) while trusting another (password) is still SQL injection. Every input needs parameterized queries, not just the ones that look dangerous.
- A "check availability" endpoint is a user-enumeration oracle. Rate-limit it, or only reveal availability at the final submit step.
- When `--` comments are blocked or awkward, close the query by balancing the quotes so it stays valid SQL.
- Filters like `WHERE owner = me` belong in the same parameterized query, and access should also be checked on the server per row. One injection shouldn't be able to read everyone's data.

Real world:
- Login bypass with `' OR '1'='1` is the oldest trick in the book and still turns up in legacy and IoT admin panels.
- User enumeration through sign-up or "forgot password" messages is how credential-stuffing and phishing campaigns build target lists. It's why many sites now say "if that account exists, we've sent an email".
- Search boxes and filters are a classic injection point because developers often build `LIKE '%...%'` strings by hand. Attacks like this one, reading other tenants' rows, are why multi-tenant SaaS apps add database-level row security (for example Postgres RLS).

----
## 3. Holiday Hack Hero

Castle Approach. A Guitar-Hero-style rhythm game (Phaser). To complete the objective you have to clear **Winter Oveland - But Harder** (Expert, 402 notes) with **≥95% accuracy**. The footer says "CHECK THE CODE".

Recon (`game-common.js`, `game.js`):
- API: `/api/session/create` → `start-song` → periodic `submit-score` (sends `current_time` every 5 s "for anti-cheat") → `complete-challenge`.
- So the server checks the timing of the run. Calling `complete-challenge` directly with fake numbers is the obvious trap.
- Scoring is still client-side: `hitNote(n, timing)` gives a perfect when `timing <= perfectWindow`, and `missNote(n)` runs when a note scrolls past.

Exploit: patch the miss handler in DevTools so every missed note counts as a perfect hit, then play the song normally. It runs in real time, so the anti-cheat sees a normal run.

```js
const GS = game.scene.getScene('GameScene').constructor.prototype;
GS.missNote = function (n) { this.hitNote(n, 0); };
```

Start → "Winter Oveland - But Harder" → keep hands off the keyboard for about 75 s → 402/402 perfect, 100% → challenge complete.

Lessons:
- Never trust the client. If the client decides what counts as a hit, the server is only validating the client's word, however good its timing checks are.
- Server-side timing checks stop replay or "skip to the end" cheats. They don't stop a tampered client that plays the song in real time.
- Real fix: send the raw key-press timestamps and let the server judge them against the chart.

Real world: this is how most online-game cheats work (aimbots, speed hacks, score editors). It's the same flaw as an e-commerce site that trusts a `price` field sent from the browser, or a mobile app that decides `isPremium` locally. Rule: the server is the authority; the client only displays.

----
## 4. Reversing Introduction

Grand Gallery, Poinsettia McMittens. A "Hardware diagnostic program" pulled off a console verifies every new pyramid block. A web-based Ghidra learning platform walks you through it in 9 guided steps.

Recon (Strings tab): a 32-bit Linux ELF (`/lib/ld-linux.so.2`, `GLIBC_2.0`) built from `target.c`. It imports `strcpy`, and has symbols like `func_debug` and `func_trampoline` that the menu never mentions.

Decompiled (Ghidra):

```c
int main()  { ... fgets(buf,16,stdin); func_choice(atoi(buf)); }

int func_choice(int c) {
    if (c == 0) return 0;
    switch (func_math_operation(c)) {        // c % 0x2a  (0x2a = 42)
        case 0:  func_debug(); break;        // hidden menu!
        case 1:  func_information(); break;
        case 2:  func_scan_hw_changes(); break;
    }
}

void func_block_verification() {             // debug menu → option 2
    char input[512]; char block[132];
    fgets(input, 0x200, stdin);              // bounded: OK
    strcpy(block, input);                    // unbounded: 512 → 132  💥
}

void func_trampoline() { ((code*)&stack)(); } // jumps into the stack: an exploit gadget
```

| Step | Question | Answer |
|---|---|---|
| 1 | Compiler/system string | `GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0` |
| 2 | Function main calls to handle input | `func_choice` |
| 3 | Math operation | `modulo` |
| 4 | Secret number | `42` |
| 5 | Function called when result is 0 | `func_debug` |
| 6 | Debug option 2 calls | `func_block_verification` |
| 7 | Biggest buffer | `512` |
| 8 | Unsafe function | `strcpy` |
| 9 | Destination buffer size | `132` |

So the "diagnostic" has a hidden backdoor: any menu choice that's a non-zero multiple of 42 opens a debug menu, and its Block Verification overflows a 132-byte stack buffer with up to 511 bytes of input. Plus `func_trampoline` conveniently jumps into the stack. This sets up the next objective, **Buffer Overflow**.

Lessons:
- Start with **strings**: compiler, libraries, function names and messages give you a map before you read any code.
- Hidden features show up as functions that are never mentioned in the UI (`func_debug`) and "magic number" checks (`% 42 == 0`).
- `fgets(buf, n, ...)` is bounded; `strcpy`, `gets`, `sprintf` and `strcat` are not. A big buffer copied into a small one is the classic overflow.

Real world:
- Hidden debug and maintenance modes behind magic inputs are a recurring real backdoor: hardcoded "engineering" passwords in routers, factory test menus in IoT firmware, and so on. Reverse engineers find them exactly like this.
- `strcpy` stack overflows started the modern exploit era: the Morris worm (1988) and Code Red (2001). They're why compilers add stack canaries, NX and ASLR, and why `strcpy` is banned in many secure-coding standards (use `strncpy`/`strlcpy`/`snprintf`).
- Ghidra (NSA, open source since 2019) is a standard tool for malware analysis, firmware audits, and patch diffing (comparing a vulnerable build with its patch to find the fixed bug).

----
## 17. SARIF

Castle Approach. The ClausCode AI reviewer ran out of tokens after writing a SARIF report (a standard JSON format, OASIS 2.1.0, that static-analysis tools use for their findings). Fix the 3 findings in `registry.py`, then click **Propose Changes**.

| Rule | Line | Bug | Fix |
|---|---|---|---|
| CCC-001 HardcodedCredentials (CWE-798) | 11 | `SECRET_KEY = "santaIsReal2024!"` | `SECRET_KEY = os.environ.get('SECRET_KEY')` |
| CCC-002 SQLInjection (CWE-89) | 19–21 | f-string `... WHERE recipient = '{recipient}'` | parameterized: `cursor.execute("... WHERE recipient = ?", (recipient,))` |
| CCC-003 OSCommandInjection (CWE-78) | 39 | `os.system("echo Delivered to: " + location + " >> /var/log/sleigh.log")` | plain file I/O, no shell |

```python
def log_delivery(location):
    with open('/var/log/sleigh.log', 'a') as f:
        f.write(f'Delivered to: {location}\n')
```

Result: **All 3 checks passed**. The Gift Registry is cleared for deployment.

Lessons:
- Secrets belong in env vars or a secrets manager, never in source. Git history keeps them forever.
- Never build SQL with string formatting. `?` placeholders let the driver handle quoting.
- `os.system` runs your string through a shell, so `;`, `&&` and `|` in user input become extra commands. Use file I/O, or `subprocess.run([...])` with a list of arguments.

Real world:
- Hardcoded secrets: bots scan public GitHub for leaked keys within minutes of a push (the 2022 Toyota T-Connect key leak, the 2016 Uber AWS breach via keys in a repo). Tools: gitleaks, trufflehog, GitHub secret scanning.
- SQL injection: still in the OWASP Top 10. MOVEit Transfer (2023) was a SQLi that hit thousands of organizations.
- Command injection: frequent in network appliances and routers whose web UI passes a "hostname" or "ping target" to a shell (for example Ivanti Connect Secure, CVE-2024-21887).
- SARIF itself is what CodeQL, Semgrep, Snyk and others output; GitHub code scanning reads it and shows alerts on PRs. Triaging these reports is a daily AppSec task.
