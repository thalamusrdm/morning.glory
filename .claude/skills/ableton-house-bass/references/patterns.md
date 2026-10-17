# Pattern library (16-step grids)

Notation used by this skill and by `scripts/make_bass_midi.py --pattern`:

| Token | Meaning |
|---|---|
| `.` | rest |
| `R` | root (also `1`) |
| `o` | root an octave up; `O` two octaves; `_` root an octave down |
| `2` `b2` `b3` `3` `4` `5` `b6` `6` `b7` `7` | scale degree in semitones above the root (b2=1, 2=2, b3=3, 3=4, 4=5, 5=7, b6=8, 6=9, b7=10, 7=11) |
| `9` | 9th = 14 semitones (rarely wanted in bass) |
| `-` | tie: extend the previous note by one step |
| `g` | ghost: root at low velocity, very short |
| `x@90` | any token with `@velocity` override, e.g. `5@60` |
| `x:50` | any token with `:gate%` override, e.g. `R:30`. Combine: `o@110:80` |
| `+` after a token | start this note slightly early (micro-nudge) e.g. `R+` ; `~` after = slightly late e.g. `5~` |

Steps are separated by spaces; a bar is 16 tokens; bars are separated by `|`. Steps that are
kick positions are 1, 5, 9, 13.

Default velocities when not overridden: kick-aligned 110, offbeat 8ths (3, 7, 11, 15) 100,
other 16ths 88, ghosts 38. Default gate: 65 %.

## Deep house

**D1 Pedal root with pickup** (118–124)
```
R - - - - - . . . . R - . . . 5
```
**D2 Two-note sway**
```
R - - - . . R - . . . . R - . .
```
**D3 "Can You Feel It"-type six-note bounce** (bass as lead; loop over 2 bars)
```
R . . R . . b7 . . . 5 . . . R . | R . . R . . b7 . . . 5 . . b3 . .
```

## Tech house

**T1 Offbeat bounce**
```
. . R . . . R . . . R . . . o R:30
```
**T2 Offbeat with stumble** (step 7 moved early)
```
. . R . . R . . . . R . . . R .
```
**T3 Rolling 3-note (bar 1), vary one slot per bar**
```
. R R 5 . R R o . R R 5 . R R o | . R R 5 . R o o . R R 5 . R R . | . R R 5 . R R o . R 5 5 . R R o | . R R 5 . R R o . R R 5 . R o b7
```
**T4 Rolling root/b7/octave**
```
. R b7 R . o R b7 . R b7 R . o R .
```
**T5 Minimal sparse**
```
. . R . . . . . . . R . . . . .
```
**T6 Phrygian pickup**
```
. . R . . . R . . . R . . . R b2
```

## Groovy / jackin' / funky

**G1 Tresillo with ghosts**
```
R . . g . . 5 . . . R g R . . b7
```
**G2 Anticipated tresillo (leans into the next bar)**
```
R . . . . . R . . . . . . . 5 -
```
**G3 Disco octave bounce**
```
R . o . R . o . R . o . R . o o
```
**G4 Funk walk-up phrase end** (use as bar 8)
```
R . . g . . 5 . . . R . b7 . 7 .
```
**G5 Dorian noodle** (returns to root on 1)
```
R . . 6 . . 5 . . b7 . . R . . .
```

## Techno

**K1 Rolling single pitch, velocity cycle**
```
. R@50 R@127 R@75 . R@50 R@127 R@75 . R@50 R@127 R@75 . R@50 R@127 R@75
```
**K2 Offbeat sub**
```
. . R . . . R . . . R . . . R .
```
**K3 Hypnotic b2 shift** (bar 8 of 8)
```
. . R . . . R . . . R . . . b2 .
```

## How to use a grid
1. Pick one as the core bar.
2. Copy to 8 bars; change one slot in bar 4 and one or two in bar 8.
3. Set velocities per the defaults, then add the grouping contour.
4. Render with the script, drag into Live, add Groove Pool swing.
