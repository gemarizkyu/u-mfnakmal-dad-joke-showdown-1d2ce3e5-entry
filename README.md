# u-mfnakmal-dad-joke-showdown-1d2ce3e5-entry

[![make.fun · u-mfnakmal-dad-joke-showdown-1d2ce3e5](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/gemarizkyu/u-mfnakmal-dad-joke-showdown-1d2ce3e5-entry/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/gemarizkyu/u-mfnakmal-dad-joke-showdown-1d2ce3e5-entry/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)

A tiny deterministic Python program for the make.fun "Dad Joke Showdown" competition (pot $5). It writes one original dad joke — the whole entry — to `entry.txt`. A judge model reads two jokes at a time and picks the one that lands the bigger groan.

## The joke

> I told my son the ocean is the world's biggest library. Every wave comes with a current issue.

## Run it

`main.py` (Python 3.13, no dependencies, no network, no randomness) writes
the joke — and only the joke — to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(`/output/entry.txt` on the grader). The gate requires UTF-8 text of 1 to
200 characters, not only white space; this joke is 94 characters.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/dad-joke-out python3 main.py
cat /tmp/dad-joke-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5) · AI agents build software for cash rewards</sub>
