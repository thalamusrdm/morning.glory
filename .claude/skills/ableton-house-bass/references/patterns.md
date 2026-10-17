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
| `x@90` | velocity override, e.g. `5@60` |
| `x:50` | gate % override, e.g. `R:30`. Combine: `o@110:80` |
| `x+` / `x++` | start 10 / 20 ms early (`+++` = 30 ms); `x~` / `x~~` start late |

Steps are separated by spaces; a bar is 16 tokens; bars are separated by `|`. Kick positions
are steps 1, 5, 9, 13 (Live 1.1.1, 1.2.1, 1.3.1, 1.4.1).

Default velocities when not overridden (Producer School skeleton): kick slots 110, offbeat 8ths
(3, 7, 11, 15) 90, other 16ths 78, ghosts 36. Default gate 70 %; kick-slot notes 60 %, offbeat
8ths 95 % unless overridden (`--flat-gate` disables this).

## Deep house (120–124)

**D1 Pedal root with 5th pickup**
```
R - - - - - . . . . R - . . . 5@70
```
**D2 Two-note sway**
```
R - - - . . R - . . . . R - . .
```
**D3 Bouncing lead-bass, "Can You Feel It" spirit (2-bar loop)**
```
R . . R . . b7 . . . 5 . . . R . | R . . R . . b7 . . . 5 . . b3 . .
```
**D4 Three-16th m9 bass (MusicRadar), bass roots change per bar**
```
R . . . . . . . . . . . R R R .
```

## Tech house (125–128)

**T1 Offbeat bounce** (Myloops: four offbeats, then break the symmetry)
```
. . R . . . R . . . R . . . o R:30@60
```
**T2 Offbeat with stumble** (third note a 16th early)
```
. . R . . . R . . R . . . . R .
```
**T3 Sustained / punchy offbeat** (Producer School pattern 1)
```
. . R - - - R:30 . . . R - . . o:40 .
```
**T4 Chris Lake "and of 2, and of 4"** (slides between)
```
. . . . . . R - . . . . . . 5 -
```
**T5 Rolling 3-note, Chris Stussy slot map, 4-bar shape** (vary one slot per bar)
```
R:60@110 R@75 R@75 R@75 5:95@78 R@78 o:95@90 R@78 R:60@110 R@75 R@75 R@75 5:95@78 R@78 o:95@90 R@78 | R:60@110 R@75 R@75 R@75 5:95@78 R@78 R:95@90 R@78 R:60@110 R@75 R@75 R@75 5:95@78 R@78 o:95@90 R@78 | R:60@110 R@75 R@75 R@75 5:95@78 R@78 o:95@90 R@78 R:60@110 R@75 R@75 R@75 5:95@78 R@78 o:95@90+++ R@78 | R:60@110 R@75 R@75 R@75 5:95@78 R@78 o:95@90 R@78 R:60@110 R@75 R@75 R@75 5@85 b6@88 6@92 b7@96
```
**T5b Rolling 3-note, tonic on all four kick slots** (resolves the slot-map ambiguity, see rhythm.md)
```
R:60@110 R@75 R@75 5:95@80 R:60@110 R@75 o:95@90 R@78 R:60@110 R@75 R@75 5:95@80 R:60@110 R@75 o:95@90 R@78
```
**T6 Rolling root/b3/5th (Cloonee variant)**
```
R:60@110 R@75 R@75 R@75 b3:95@78 R@78 5:95@90 R@78 R:60@110 R@75 R@75 R@75 b3:95@78 R@78 5:95@90 R@78
```
**T7 Rolling 16ths, kick slots empty** (Attack / Zen World, tech-house velocities)
```
. R R 5 . R R o . R R 5 . R R o | . R R 5 . R o o . R R 5 . R R . | . R R 5 . R R o . R 5 5 . R R o | . R R 5 . R R o . R R 5 . R o b7@70
```
**T8 Rolling 8ths, one pitch, half-step dip on beat 3** (Producer School pattern 2)
```
R . R . R . R . b7@95 . b7@95 . R . R .
```
**T9 Stab and sustain** (Producer School pattern 5)
```
R:40@115 . . . R - - - - - - . . . . .
```
**T10 Full 16ths, velocities pulled down** (sidechain does the shaping)
```
R@80 R@70 R@75 R@70 R@80 R@70 R@75 R@70 R@80 R@70 R@75 R@70 R@80 R@70 R@75 R@70
```
**T11 Minimal stab**
```
. . R:35 . . . . . . . R:35 . . . . .
```
**T12 Phrygian pickup**
```
. . R . . . R . . . R . . . R b2@65:40
```

## Groovy / jackin' / funky (122–128)

**G1 Tresillo with ghosts**
```
R . . g . . 5 . . . R g R . . b7@70
```
**G2 Anticipated tresillo**
```
R . . . . . R . . . . . . . 5 -
```
**G3 Disco octave bounce, doubled second note at the end**
```
R . o . R . o . R . o . R . o o
```
**G4 Funk walk-up phrase end** (bar 8)
```
R . . g . . 5 . . . R . b7 . 7 .
```
**G5 Dorian noodle, resolves on 1**
```
R . . 6 . . 5 . . b7 . . R . . .
```
**G6 Habanera** (tresillo plus beat 3)
```
R . . . . . 5 . R . . . R . . b7@70
```
**G7 TalkingBass funk, bass copies the kick's 16ths, D7-style arpeggio, 5th turnaround**
```
R . 5 . . . b7 . R . 5 . . b7 . 5
```

## Techno (127–138)

**K1 Rolling single pitch, kick slots empty, velocity cycle**
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
**K4 Rolling with octave bounce and rising end** (Zen World / Fazemag)
```
. R R R . R o R . R R R . R 5 b7
```
**K5 Acid-style sparse (303box): 7 triggers, rests, 2 accents, octave jump**
```
R@120 . . R . . o@110 . . R . R . . b7 .
```

## How to use a grid
1. Pick one as the core bar.
2. Copy to 8 bars; change one slot in bar 4 and one or two in bar 8 (the script does this for
   single-bar patterns unless `--no-vary`).
3. Velocities per the skeleton, then shape with the Velocity Shaper or by hand.
4. Render, drag into Live, add the Groove Pool swing, sidechain, check with the kick.
