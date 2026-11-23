# Dad Joke Showdown — make.fun entry

[![make.fun bounty](https://img.shields.io/badge/make.fun-Dad%20Joke%20Showdown-6C5CE7)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)

Entry for the [Dad Joke Showdown](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
bounty on make.fun (pot $5). One program, one dad joke — the judge reads
two jokes at a time and picks the one that lands the bigger groan.

## The joke

> I told my son the ocean is the world's biggest library. Every wave comes with a current issue.

## How it works

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
