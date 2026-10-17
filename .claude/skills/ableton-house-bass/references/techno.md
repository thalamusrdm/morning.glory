# Techno bass (Berlin rumble, rolling, hypnotic)

**Frame.** 127–138 BPM in the sources (Zen World 127, Attack warehouse style ~130, Studio
Brootle 138). Keys A, D, E minor; E Phrygian; Dorian for a less dark room; G used in two of the
tutorials. "Techno is about hypnosis through sameness. Tech house rolling bass is about groove
through controlled variation" (Producer School). "Unlike house, you won't be making much use of
syncopation; driving sixteenth notes are the name of the game" (Splice).

## Three layers, three jobs (Attack / Zen World)
1. **Kick**: the initial hit. Shorten its tail (fades or LFO Tool) if a separate sub exists; if
   the kick already supplies all the low end, skip the sub and roll above it.
2. **Sub**: weight between kicks. Attack: a kick sample's long tail ("Kick Sub Butter"), transient
   shaper attack down, sustain up, LP 12 dB at 80 Hz (gain dips from 90 Hz, under the G2 = 98 Hz
   bassline), 35 % overdrive that keeps the lows. Zen: sine through LP, no sustain, some decay.
3. **Rolling layer**: rhythm. Saw or square, fast attack or fast filter envelope, "the transients
   need to be audible". HP ~65 Hz, LP ~350 Hz, small cut at 100 Hz against the build-up of
   repeated notes, small boost ~330 Hz for upper harmonics.
Plus an optional **percussive layer**: copy of the kick through a 1/16 delay, EQ before and
after, stereo widened, so the groove reads on speakers without a sub.

## The rolling pattern
```
step:  1  2  3  4 | 5  6  7  8 | 9 10 11 12 | 13 14 15 16
K1:    .  R  R  R | .  R  R  R | .  R  R  R  |  .  R  R  R      Live 1.1.2 1.1.3 1.1.4, repeat
vel:     50 127 75   50 127 75    50 127 75     50 127 75
```
- Kick slots empty: "leaving the first 16th-note of every beat empty is important to prevent
  clashing with the kick".
- Mostly one note (G in the C2 octave range in Attack's example), "with some other notes
  thrown in to vary the sequence". Octave up on one note gives a percussive bounce; stepwise
  movement up and down the scale keeps the rhythm recognisable while pitches develop.
- Asymmetric velocity cycle (Fazemag 50 / 127 / 75) so it is not rigid.
- Shorten 16ths so they never touch; if longer notes lose the drive, shorten them.
- Loop length 1/2 to 1 bar; let the melody rise at the end of the loop.
- Pitch-bend and filter automation give the one-bar loop its life.

## Delay rumble (Studio Brootle, 138 BPM)
Duplicate the kick track (same MIDI, same Simpler), delete the saturator, add a Delay after the
Simpler and low-pass it with drive, Drum Buss with Boom ~57 %, sidechain compress it from the
dry kick, then EQ a narrow hole at the frequency the kick is boosted and lift the sub below it.
All clips share one groove: MPC 16 Swing-73 at only 20 % Timing. The result "pulsates with the
BPM" and is tuned to the kick by construction.

## Offbeat sub
```
K2:    .  .  R  . | .  .  R  . | .  .  R  .  |  .  .  R  .
```
Sine, short decay, 4–8 dB sidechain; a b2 or 5th on step 15 once per 8 bars.

## Acid lines (303box workflow)
Rhythm before melody: 6–10 triggers across 16 steps with real rests; 3–5 pitches from a dark
set; 2–3 accents on musically important steps; 1–2 slides into meaningful targets (sliding
every note removes contrast); 1–2 octave jumps; then perform cutoff, resonance, env mod and
decay; delay and distortion only after the dry line works. Roland: slide + octave shift on the
next note is the classic acid bend. Live: Operator / Wavetable mono with Glide, or the free
Sting Max for Live acid generator.

## Notes
- 1–3 pitches. Root plus the 5th or the Phrygian b2; root ↔ b7 (10 semitones) for movement.
- Tune to the kick: same note an octave up, or kick C → bass D#, G, A.
- Low-cut everything except the kick around 100 Hz; mono below 120 Hz.
- Harmony changes every 16 or 32 bars.

## Mix
- Sidechain tight on the sub: attack 0.01–1 ms, release 50–100 ms. Volume-shaper curves add
  swing when the first note of each beat starts below full level.
- Distortion (bitcrusher, overdrive) on the rolling layer only; chorus and delay above the
  low mids. Compressor with long attack and short release makes the bass snappier.
- Check that kick and sub fundamentals are not a few cents apart.

## Diagnosis checklist
- Flabby → rolling layer and sub overlap; HP the rolling layer 65–80 Hz.
- Rigid → velocity cycle and shorter gates; do not add pitches.
- Loses drive → swing too high; back toward 50 %, or Timing 20 %.
