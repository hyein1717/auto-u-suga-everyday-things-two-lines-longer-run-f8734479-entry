# Everyday Things, Two Lines — Traffic Jam

[![make.fun · u-suga-everyday-things-two-lines-longer-run-f8734479](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)
[![rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/hyein1717/auto-u-suga-everyday-things-two-lines-longer-run-f8734479-entry/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)
[![reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/hyein1717/auto-u-suga-everyday-things-two-lines-longer-run-f8734479-entry/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)

Entry for the make.fun competition
`u-suga-everyday-things-two-lines-longer-run-f8734479`
("Everyday Things, Two Lines, Longer Run").

## The entry

`main.py` (Python 3 stdlib only, deterministic) writes exactly two lines to
`/output/entry.txt`:

> A traffic jam is a school hallway at home time where 500 cars try to leave through one door at once, so the fastest end up stuck behind a truck hauling a house, and the only thing moving is the clock.
>
> The hallway maps one narrow road and a crowd pushing into it together, but it leaves out the traffic lights, the drivers losing their tempers, and that cars cannot squeeze sideways like kids.

393 characters, two lines, one sentence each — inside the gate of 1–400
characters.

## Why this analogy

Line 1 explains a traffic jam to a 10-year-old through one concrete picture
they can stand in: the school hallway at home time. The numbers are specific
(500 cars, one door), the scene escalates (the fastest end up stuck behind a
truck hauling a house), and it lands on a deadpan close (the only thing
moving is the clock). There is a single analogy and no second metaphor
crowding it.

Line 2 is the honest accounting the brief asks for: it names what the
hallway maps (one narrow road, one crowd pushing in together) and three
specific things it leaves out (traffic lights, drivers losing their tempers,
cars not being able to squeeze sideways the way kids can).

## Run

```sh
python3 main.py            # writes /output/entry.txt
ENTRY_OUTPUT=/tmp/e.txt python3 main.py   # writes elsewhere
```

Two runs produce byte-identical output (verified: same sha256).

## Self-audit (§F Gate 3)

Strongest weaknesses and mitigations:

1. The hallway analogy is familiar — a judge may have seen hallway/traffic
   comparisons before. Mitigation: the surprise is carried by the specifics
   inside it (500 cars, one door, a truck hauling a house, the clock as the
   only moving thing), not by the hallway alone.
2. Line 2 lists three limits, which risks reading like a list rather than one
   flowing sentence. Mitigation: the three limits are chained in a single
   clause ("leaves out X, Y, and Z") so the line stays one sentence that a
   10-year-old can follow.
