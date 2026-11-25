# Alien Field Notes: The Two Day Earth Review

[![make.fun · u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/jinan86/alien-field-notes-earth-review/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/jinan86/alien-field-notes-earth-review/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

A make.fun entry: a tiny deterministic Python program that writes one line — a review of planet Earth left by an alien tourist — to `/output/entry.txt`.

## The entry

> They explode coloured lights in the sky for fun and call it a celebration. On my planet, that's how a war starts. 4/5

The angle: fireworks. Humans set off coloured explosions in the sky for fun and call it a celebration; the alien reads the same display the way their own world does — as the opening of a war. One clean joke, punch at the end, verdict in the tail.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic, stdlib-only, no network. The program validates its own output against the gate (1–200 UTF-8 characters, not only whitespace, single line) before writing.

## License

MIT — see [LICENSE](LICENSE).
