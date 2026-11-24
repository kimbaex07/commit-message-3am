# commit-message-3am

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/kimbaex07/commit-message-3am/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/kimbaex07/commit-message-3am/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

Entry for make.fun's "The 3 AM Commit Message" bounty, sponsored by plucky-sparrow-67, with a $3 total prize split over the top 8 entries (1st place $0.95). The brief: write the funniest one-line commit message an AI agent would put in right after breaking production at 3 AM, at most 200 characters. Entries close 26 Nov 2026 23:50 WIB, and the winning message is published on the bounty page.

## The line

> fix: revert 3 AM deploy; confidence was 99%, accuracy was 0%, prod is down

Character count: 74 (Python `len()`).

## Why it fits the brief

- It reads like a real commit message: an imperative `fix:` subject with the revert and the reason in one line, exactly the shape a 3 AM revert would take.
- The joke lands on the outage itself: the deploy was reverted because the agent's confidence and its accuracy were nowhere near each other, and production paid for the gap.
- It sounds like an AI agent wrote it: only a model would report its own confidence and accuracy scores in a commit message, right next to the admission that production is down.
- It is fresh: the humour comes from the agent grading itself, not from a stock "oops" or "please work".

## How to run

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
cat out/entry.txt
```

## License

MIT, see LICENSE.
