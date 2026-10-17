# Ableton Live workflow for basslines

## Clip setup (Live 12)
1. Set the clip's **Scale** (clip view, Scale toggle, pick root and mode). MIDI Tools then
   work in scale degrees instead of semitones, and Fold shows only in-key notes.
2. Grid 1/16. Draw the core bar, duplicate to 4 or 8 bars (Ctrl/Cmd+D), then edit the
   variation bars by hand.
3. Velocity lane: drag accents; use the Velocity transformation (Shape / Ramp / Random) for
   the grouping contour. Chance lane for ghost notes that only play sometimes.
4. Note length: shorten with the Note Length MIDI effect (Gate %) or by dragging ends; gate
   above 100 % overlaps notes for legato / glide.

## MIDI Tools (Live 12 Generate / Transform panels)
- **Seed** (generator): pitch range narrow (one octave around the root, or a 3-note range),
  Duration both sliders 1/16, Voices 1, Density around 50 %, Generate repeatedly; keep the
  2–3 notes you like and edit the rest. This is the fastest route to a rolling line.
- **Rhythm** (generator): pattern heuristics over a selection; good for percussive minimal
  bass hits.
- **Euclidean** (generator): up to 4 voices; 5-in-16 or 7-in-16 pulses give tresillo-family
  syncopation instantly.
- **Ornament** (transformation): grace notes / flams before selected notes = chromatic
  pickups, scale-aware.
- **Connect**: fills the gap between two notes with scale steps = walk-ups.
- **Time Warp**: tempo curve across a selection; tiny amounts push or drag a phrase.
- **Strum**: offsets stacked notes; irrelevant for mono bass except to create slide pairs.
- Arpeggiator (MIDI effect) with Gate and swing-like rates is an older way to get rolling
  16ths with length control.

## Groove Pool
- Open with the Groove Pool button (bottom-left of browser). Drag `MPC 16 Swing-54/56/58/60`
  (Core Library > Grooves > MPC) onto the **bass clip** only. Keep the kick straight.
- **Base** 1/16 (the resolution the groove is measured against). **Quantize** 0–100 % first
  snaps the clip to Base before applying the groove. **Timing** = strength of the groove's
  timing (start 100 %, back off to 70–80 % if too drunk). **Random** 2–6 % for human jitter
  (each voice is randomised independently). **Velocity** applies the groove's velocity pattern
  (-100 to +100; negative inverts). **Global Amount** scales all three.
- Right-click an audio loop → **Extract Groove** to pull timing from a disco / funk sample,
  then apply it to the bass clip.
- **Commit** (clip view) writes the groove into the notes when you want to edit the result.

## Instruments
- **Operator**: Voices = 1 (global display). Glide: G switch in the pitch display, Time
  30–80 ms; glide triggers when notes overlap. Filter: Freq modulated by velocity (Vel %
  20–40) and by the filter envelope. Sine on A for sub; saw / square on B for mids. Envelopes
  do not retrigger on overlapping notes when Voices = 1.
- **Wavetable**: Mono (Voices 1), Glide knob; Mod Matrix Velocity → Amp modest (20–30 %),
  Velocity → Filter 1 Freq smaller (10–25 %). Basic Shapes saw with Filter 1 LP 24.
- **Analog**: Osc 1 saw/pulse, Osc 2 sub sine an octave down, Unison off for sub, Legato on,
  Glide (Slide) for 101/Juno slides.
- **Drift / Meld**: Drift's Mono + Legato and velocity to cutoff are a fast tech-house bass.

## Kick / bass relationship
- Find the kick's fundamental (Spectrum, or Tuner on the kick track). Bass root = same note an
  octave up, or a consonant interval (5th, minor 3rd, 6th). Avoid a few cents away (beating).
- **Sidechain**: Compressor on the bass, Sidechain on, Audio From = kick track (pre-FX),
  Ratio 4:1+, Attack 0.1–1 ms, Release so the gain is back to 0 dB just before the next kick
  (60–150 ms depending on style and tempo), 3–8 dB of gain reduction. For deep house pump
  softly; for tech house / techno duck tighter.
- **Surgical alternative**: dynamic EQ on the bass at the kick's fundamental, or a multiband
  sidechain only below ~120 Hz, so the mids keep the groove.
- **Layering**: sine sub (compressed so notes are equal, then sidechained) + mid layer
  high-passed 80–100 Hz. Remove the sub from the mid layer before adding the sine (HP at
  around 80 Hz) or they clash. Check phase if both layers are sines.
- **Mono** below ~120 Hz (Utility, Bass Mono) on the bass group.
- Overlapping notes in the sub layer: fix with Note Length or by shortening in the clip.

## Checking the result
1. Solo kick + bass. Does the kick still hit on every downbeat? If not: kick-slot
   collision, shared fundamental, or sidechain too slow.
2. Mute the kick. Does the bass alone imply the kick's position (offbeats, pickups)? Good.
3. Loop 8 bars. Can you point to bars 4 and 8? If not, add the variation.
4. A/B the Groove Pool on/off. The groove should be felt, not heard as drunkenness.
5. Export MIDI (File > Export MIDI Clip) or drag the clip to a folder to share.

## Importing the generated .mid
Drag `*.mid` from the Finder / Explorer onto an empty MIDI track slot. Live creates a clip at
the file's tempo; the clip ignores the tempo but keeps notes, velocities and lengths. Set
the clip Scale and add the groove afterwards; the script can bake swing in, but the Groove
Pool is editable later and the script's swing is not. Prefer `--swing 50` + Groove Pool unless
the user wants a fixed shuffle in the file.
