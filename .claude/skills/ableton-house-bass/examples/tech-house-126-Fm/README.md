# Worked example: tech house, 126 BPM, F minor, 8 empty tracks

Generated with the skill. Drag each `.mid` onto its track. Set the Live Set to 126 BPM and the
Set key to F minor (Scale Mode on). Drum notes assume a Core Library style Drum Rack mapping
(C1 36 kick, C#1 37 rim, D#1 39 clap, F#1 42 closed hat, A#1 46 open hat); move the notes if your
kit differs. Pitch names below use Ableton's display (MIDI 41 = F1 in Live, F2 scientific).

## Frame
- Kick tuned to **F**: fundamental F0 in Live's display (43.7 Hz). Check with Tuner on the body.
- Sub plays **F0 (MIDI 29)** on the offbeats only, so it never sounds under the kick.
- Rolling bass is one octave up, **F1–C2–F2 (MIDI 41–48–53)**, the 80–250 Hz band where the
  roll is heard. The kick owns the bottom octave, the sub fills between kicks, the roll is rhythm.

## The 8 tracks

| # | Track | File | Device and starting values |
|---|---|---|---|
| 1 | Kick | `01_kick_C1.mid` | Drum Rack / Simpler, short tech-house kick (200–350 ms tail), tuned to F. Straight, no groove. Peak around -6 dBFS. |
| 2 | Clap | `02_clap_Dsharp1.mid` | Layered clap on 2 and 4, high-pass 300 Hz on the tight layer, short plate on a send. Straight. |
| 3 | Closed hat | `03_closed_hat_Fsharp1_swing57.mid` | 16ths with offbeat 8ths removed for the open hat, velocities 66–96, **57 % swing baked in**. Pan 15–25 % off centre. Rotate 2–3 samples. |
| 4 | Open hat | `04_open_hat_Asharp1.mid` | Offbeats 3-7-11-15, accents on the "and" of 2 and 4. Straight: the open hat is the steady counterweight to the swung closed hats. Release ~225 ms. |
| 5 | Perc | `05_perc_rim_Csharp1_swing57.mid` | Rim / woodblock on the "a" of 2 and the "e" of 4, ghost at the end of every second bar. 57 % swing. Add a filtered live perc loop, high-passed 200–300 Hz, under it. |
| 6 | Sub | `06_sub_sine_F1_offbeat.mid` | Operator: A sine only, Voices 1, amp decay ~200 ms, no sustain. Utility mono. Compressor sidechained from the kick: attack 0.5 ms, release 110 ms, 4:1, 5–7 dB. No groove. |
| 7 | Rolling bass | `07_bass_rolling_F2_straight.mid` (+ `_swing57` version, + `07b` offbeat alternative) | Operator: A sine 100 %, B saw ~-18 dB, D sine one octave down ~-6 dB; filter LP24 at 200 Hz, Res 8 %, filter Env 40 % (A 1 ms, D 80 ms, S 30 %, R 100 ms); amp A 1 D 200 S 60 R 80; Voices 1, Glide off; Vel → Filter Freq 30 %. EQ Eight high-pass 80 Hz. Compressor sidechain from kick: attack 1 ms, release 110 ms, 4:1, soft knee, 5–7 dB. Groove Pool: **MPC 16 Swing-58**, Timing 100 %, Velocity 0 %, Random 0 % on the straight file (or use the swing57 file with no groove). |
| 8 | Stab | `08_stab_Fm7.mid` | Fm7 (F Ab C Eb) voiced F4–Eb5, on the "a" of 2 every bar plus a step-16 pickup in bars 4 and 8. Drift or Analog pluck, high-pass 300 Hz so it stays out of the bass band, 1/8-dotted delay on a send. |

Keep the bass out of the drum bus. Glue the drum bus with 1–2 dB of compression only.

## The bass grid (file 07, F minor, 8 bars)

```
step :    1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
kick :    X   .   .   .   X   .   .   .   X   .   .   .   X   .   .   .
bar 1:   F1  F1  F1  F1  C2  F1  F2  F1  F1  F1  F1  F1  C2  F1  F2  F1   (Live display names)
vel  :  110  75  75  75  78  78  90  78 110  75  75  75  78  78  90  78
gate :   60  70  70  70  95  70  95  70  60  70  70  70  95  70  95  70   (% of a 16th)
bar 2:   slot 7 octave replaced by F1 (one slot changed)
bar 3:   as bar 1, slot 15 (F2) starts 30 ms early (anticipation)
bar 4:   slots 13-16 chromatic walk C2 C#2 D2 D#2 into F1 of bar 5
bars 5-8: repeat 1-4
```
MIDI numbers: F1 = 41, C2 = 48, F2 = 53, walk 48 49 50 51.

In the drop, loop bar 1 only (steadier than the verse). For a second drop swap to
`07b_bass_offbeat_F2_alt.mid` (offbeat 8ths with octave and pickup on beat 4).

## Why it works
The kick and sub never sound at the same time, so the low end is clean before any sidechain.
The roll puts the tonic on the kick slots and the 5th and octave between them, which is the
interlock that makes a tech house line drive; velocity (110 / 90 / 75) and gate (short on the
kick, long on the offbeats) are what stop it sounding like a sequencer. Perc and stab land on
the "a" of 2 and "e" of 4, the cracks the bass leaves, so all three layers share one accent map.

## Regenerate
```
S=scripts/make_bass_midi.py
python3 $S --style tech-stussy --key Fm --octave 2 --bpm 126 --bars 8 --swing 50 --out 07_bass_rolling_F2_straight.mid
python3 $S --pattern ". . R@100 . . . R@100 . . . R@100 . . . R@100 ." --key F --octave 1 --bpm 126 --bars 8 --gate 70 --no-vary --flat-gate --out 06_sub_sine_F1_offbeat.mid
```
Drums use `--key C/D#/F#/A#/C# --octave 2` so the root lands on the Drum Rack pad (MIDI 36–46).
