# One Word From Grandma

[![make.fun · u-0xkianno-one-word-from-grandma-f04bed16](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/oxdfahmad/u-0xkianno-one-word-from-grandma-f04bed16/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/oxdfahmad/u-0xkianno-one-word-from-grandma-f04bed16/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)

## The word

**Skynet** — the one word Grandma would text about AI. She has seen the movies, she knows how this ends, and she is warning the whole family group chat in a single word. Short, dramatic, and exactly the kind of thing a grandma types with total confidence before putting the phone down.

## How it works

`main.py` (Python 3, standard library only, no network, no input) holds the word as a constant, gates it — exactly one word, letters only, 1–30 characters, no spaces or punctuation — writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), then reads the file back and verifies the bytes match before printing a short confirmation. Every run writes the same bytes, deterministically.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```
