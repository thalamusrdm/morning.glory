# Tech house, deep tech and minimal bass

**Frame:** 124–128 BPM. Keys A, F, G, C, D minor; Phrygian flavour for darker rooms. Mood:
the bass is the hook. Two families: **offbeat bounce** (Chris Lake / Fisher style) and
**rolling 16ths** (Chris Stussy / East End Dubs style minimal-tech). Minimal proper is a
third: one or two percussive bass hits per bar and the gaps are the groove.

## Offbeat bounce (archetype 2)

```
step:  1  2  3  4 | 5  6  7  8 | 9 10 11 12 | 13 14 15 16
bass:  .  .  R  . | .  .  R  . | .  .  R  .  |  .  .  o  R'    (o = octave, R' = short pickup)
vel:         105         95          105             90  60
gate:        70%         70%         70%             50% 30%
```
- Four offbeats, then change one thing: step 15 up an octave, step 16 a 16th pickup, or move
  step 7 to step 6 for a stumble.
- Range around E1–G2; a two-pitch line (root + b7, or root + 5th) is plenty.
- Short notes on downbeat-adjacent positions, longer on the offbeats.
- Velocity → cutoff on the synth so the same pattern breathes.
- Swing 56–58 % via Groove Pool on the bass clip; kick straight.

## Rolling 16ths (archetype 4)

Definition from the modern tech-house tutorials: 16ths (or nearly) for most of the bar from a
small interval set, usually 3 pitches, with the tonic landing where the kick lands.

```
step:  1  2  3  4 | 5  6  7  8 | 9 10 11 12 | 13 14 15 16
bar1:  .  R  R  5 | .  R  R  o | .  R  R  5  |  .  R  R  o
bar2:  .  R  R  5 | .  R  o  o | .  R  R  5  |  .  R  R  .
bar3:  .  R  R  5 | .  R  R  o | .  R  5  5  |  .  R  R  o
bar4:  .  R  R  5 | .  R  R  o | .  R  R  5  |  .  R  o  b7
```
- Slots 1, 5, 9, 13 empty (kick owns them). If the user insists on filling them, make those
  the loudest notes (~110) and the only ones that overlap the kick.
- Vary **one slot per bar**: octave, rest, 5th, b7 pickup. Never redraw the whole bar.
- Velocity: 110 on the kick-adjacent accents (steps 2 and 10 or 3 and 11), 85–95 for the
  rest, two slots at 60. Lower every 4th 16th by 20–30 %.
- Gate: shorten each 16th so notes never touch (60–80 %); longer (90 %) on one offbeat per
  beat for the pull.
- Swing 56–58 %; then nudge two or three off-downbeat notes 5–10 ms early or late.
- High-pass the rolling layer around 65–80 Hz and put a sine sub (one note per bar or on the
  offbeat 8ths) underneath so the rolling notes are rhythm and the sub is weight.

## Minimal (sparse)
```
bass:  .  .  R  . | .  .  .  . | .  .  R  .  |  .  .  .  .
```
Percussive envelope (short decay, no sustain), one or two hits, maybe a b2 or 5th grace
note once per 4 bars. The groove is in what is *not* played; resist adding notes and add a
dotted-8th delay on a perc instead.

## Notes
- Root / 5th / octave or root / b7 / octave sets.
- Phrygian trick: slip the b2 in as a short approach into the root on step 16 or step 8.
- Keep the line to 2–3 pitches; melodic interest comes from the octave placement.

## Sound
- Saw or square with a fast amp attack and a fast filter envelope (Operator, Analog,
  Wavetable). Voices = 1, Glide on for slides when notes overlap.
- Velocity → filter cutoff 20–40 %; a little velocity → amp.
- Tight sidechain from the kick: attack 0.1–1 ms, release 60–120 ms so the bass is back to
  full level just before the next kick; 4–8 dB of ducking.
- Sub mono, mid layer may have width above 150 Hz.

## Diagnosis checklist
- Sounds like a preset loop → vary one slot per bar, add velocity contour, swing the clip.
- Kick disappears → bass is on the kick slots or shares the fundamental; empty the slots or
  octave up.
- No bounce → gate uniform; lengthen the offbeats, shorten the others.
- Too busy at 128 → drop to offbeat bounce; density that works at 124 clutters at 128.
