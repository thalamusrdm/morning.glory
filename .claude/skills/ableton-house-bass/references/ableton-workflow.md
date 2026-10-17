# Ableton Live workflow for basslines

## Clip setup (Live 12)
1. Set the Set's key and the clip's **Scale** (Scale Mode). MIDI Tools then work in scale
   degrees instead of semitones, Fold shows only in-key notes, and generators follow the key.
2. Grid 1/16. Draw the core bar, duplicate to 4 or 8 bars (Ctrl/Cmd+D), edit the variation bars.
3. Velocity lane for the skeleton (110 / 90 / 70–80); Chance lane for ghost notes that only
   sometimes play.
4. Note length: drag ends, or the Note Length MIDI effect (Gate %: 50 % halves, 200 % doubles,
   above 100 % overlaps for legato).
5. Write with a plain sound first (sine or a simple preset); swap the patch once the pattern
   grooves.

## MIDI Tools (Clip View, Transform and Generate panels)
General behaviour from the manual and the Attack guide: generators fill the **Loop Brace**,
not the whole clip, so set the brace to the length you want (handy for generating a fill in
bars 7–8 only). **Auto** on regenerates on every parameter change; off waits for Generate.
Generated notes stay selected and coloured; **deselect them** before the next generation or
they are replaced; grey notes are fixed. Alt/Option-click the piano ruler to pick a pitch or
range for Seed / Shape.

Generators:
- **Seed**: random notes within pitch, duration and velocity ranges; Voices (max simultaneous)
  and Density (% of the range populated). Bass recipe (Attack / MusicRadar): narrow pitch range
  (a 4th or 5th around the root, or merge the handles for one pitch), Duration 1/16–1/16,
  Velocity 100–110 or a range for variation, Voices 1, Density ~50 %, Generate until something
  works, keep 2–3 notes and edit the rest. Preset used in the Attack example: Wavetable "Basic
  FM House Bass", Tri + Sub.
- **Rhythm**: Steps, Pattern (placement), Density (number of notes), Step Duration, Velocity
  and Accent with Accent Frequency / Offset, Shift, Split %. Works on one pitch at a time; good
  for a single-pitch rolling or ghost layer.
- **Euclidean** (Max for Live): up to 4 voices, each with its own pitch and velocity; Steps,
  Density (pulses), Division, per-voice Rotation and a dice. 5-in-16 or 3-in-8 gives
  tresillo-family syncopation instantly; set the voices to root / 5th / octave.
- **Shape**: monophonic sequence following a drawn or preset contour; Rate, Tie (probability a
  note extends to the next), Density, Jitter.
- **Stacks**: chords from a root, type and inversion; build a progression from your bass roots.

Transformations useful for bass:
- **Velocity Shaper** (M4L): draw an envelope over the selection, Min / Max velocity, Loop and
  Rotate / Division to repeat it per beat. Fastest way to get the 110 / 90 / 75 skeleton.
- **Span**: legato / tenuto / staccato articulation for the whole selection (staccato = half the
  smallest gap), with Offset and Variation.
- **Ornament**: Flam or Grace Notes before selected notes; Grace pitch High / Low / Same (a
  semitone or scale degree) and a relative velocity. Scale-aware chromatic pickups.
- **Connect**: fills gaps between notes with interpolated notes; Spread (pitch range) and
  Density. Walk-ups between two roots.
- **Recombine**: permutes Position, Pitch, Duration or Velocity across the selection: shuffles a
  riff while keeping its shape (MusicRadar).
- **Arpeggiate**: Rate and Gate; Distance in scale degrees. Old-school route to rolling 16ths
  with length control.
- **Time Warp**: speed curve over a selection; tiny amounts drag or push a phrase. **Strum**
  offsets stacked notes; **Chop** splits long notes into patterns with gaps; **Quantize**.
- **Glissando** / **LFO** are MPE tools for pitch-bend slides when the instrument supports MPE.

Other Live tools: the **Sequencers** pack (SQ Sequencer with scale mode and dice for pitch,
rhythm, length, velocity) and the free **Sting** Max for Live acid generator (MusicRadar).

## Audio to MIDI bassline (MusicRadar / Pops Roberts)
Loop the drums (Cmd+L), audition percussion loops in the browser for one that counters the
beat, drag it in, right-click → **Convert Drums to New MIDI Track**, replace the instrument
with a bass, then edit the pitches to chord tones. The rhythm is inherited from a played loop.

## Groove Pool (manual section 14)
- Open: browser drop-down or **Ctrl+Alt+6 / Cmd+Option+6**. Drag a groove from Core Library >
  Grooves onto the **bass clip** (not the kick). Hot-Swap next to the Clip Groove chooser
  steps through grooves while the clip plays. Names: `Swing 16-55` (Swing folder), `MPC 16
  Swing-58`, `MPC 16 Swing-62`, `MPC 16 Swing-73`, `MPC 16 Double Up-55` (moves all 16ths and
  changes velocity).
- **Base**: resolution the groove is measured against (1/16 for 16th swing). Notes in the
  groove file that sit on the grid do not move, so neither do the matching clip notes.
- **Quantize**: straight quantize applied *before* the groove (100 % snaps to Base).
- **Timing**: how much the groove's timing affects the clip. Producer School runs MPC 16
  Swing 58/62 at full; Studio Brootle runs Swing-73 at 20 %; IQSounds suggests 10–30 % for
  minimal.
- **Random**: timing jitter, different per voice. Keep near zero on bass (research: random
  per-note displacement lowers groove ratings).
- **Velocity**: -100 to +100, negative inverts. Set 0 when you only want timing.
- **Global Amount**: scales all three, up to 130 %, also in the Control Bar.
- **Commit** writes the groove into the notes and sets the clip groove to None; do it late, once
  you have stopped auditioning (then you can see and edit what it did).
- **Extract Groove**: drag any audio or MIDI clip to the Groove Pool or use the clip context
  menu; only the playing portion is used. Pull timing from a funk or disco loop.
- Edit a groove file: drag it into a MIDI track, edit as a clip, extract again.
- Real-time quantize: Timing / Random / Velocity at 0, Quantize and Base to taste.
- A/B by bypassing: if the groove is audible only in solo it may be too subtle; if the bypassed
  version suddenly sounds cleaner and harder, the swing is too strong. Test at low volume.
- Track Delay (the D button bottom right) shifts a whole channel: -9 ms clap early, +5 ms late
  (Attack). A consistent whole-track offset is the research-safe way to lay the bass back.

## Instruments
- **Operator**: Voices = 1; Glide (G) in the pitch display with Time 30–80 ms, triggered by
  overlapping notes; envelopes do not retrigger on legato. Per-oscillator **Vel** (on a
  modulator it controls FM amount, so harder notes get brighter), **Osc < Vel**, **Time <
  Vel** (envelope segments faster on hard notes), **Key** tracking. Filter Freq / Res with 12
  or 24 dB slopes, its own envelope with curves, and Sync mode that repeats the filter envelope
  every 1/16 for rhythmic movement. A sine on A, a saw on B at low level and a sine an octave
  down on D is the Stussy patch in Operator terms.
- **Wavetable**: Mono, Glide; Mod Matrix Velocity → Amp 20–30 %, Velocity → Filter 1 Freq
  10–25 %, Env 2 → Filter 1 Freq ~40 % for the "talking" attack; Basic Shapes saw + Sub.
- **Analog**: saw or pulse, Osc 2 sub sine an octave down, Legato on, Glide for 101 / Juno slides.
- **Drift**: Mono + Legato, velocity to cutoff; quickest tech-house bass.
- **Simpler** on a kick sample for the techno sub / rumble.

## Kick / bass relationship
- Tuner on the kick (read the body, not the transient) or an EQ sweep for the peak. Bass root =
  same note an octave up, or 5th / minor 3rd / 6th. Never a few cents off.
- **Sidechain compressor** on the bass: Sidechain on, Audio From kick (pre-FX), Ratio 4:1–6:1,
  Attack 0.1–2 ms, Release 80–130 ms at 124–126 BPM (deep house 120–180 ms, techno 50–100 ms),
  4–7 dB of gain reduction, soft knee. Watch the GR meter breathe; if it is still down when the
  next kick arrives, shorten the release.
- Alternatives: multiband / band-mode sidechain on the low band only so the mids keep the
  groove (Niek); dynamic EQ at the kick fundamental; LFO Tool / ShaperBox / Kickstart curves.
- **Layers**: sine sub (compressed so notes are equal, then sidechained) + mid layer
  high-passed 65–100 Hz. Remove the sub from the mid layer before adding the sine or they
  clash; check phase if both are sines.
- **Mono** below ~120 Hz (Utility Bass Mono or a Utility in mono on the bass group); keep the
  bass out of the drum bus so its sidechain and EQ stay independent.
- Overlapping notes in the sub layer: Note Length or shorten in the clip.

## Checking the result
1. Solo kick + bass: does the kick still hit on every downbeat?
2. Mute the kick: does the bass alone imply where the kick is?
3. Loop 8 bars: can you point to bars 4 and 8?
4. Bypass the groove: felt, not heard?
5. Bypass the sidechain: is the duck shaping or hiding the line?
6. Low volume and mono: still bouncing?
7. Export: File > Export MIDI Clip, or drag the clip to a folder.

## Importing the generated .mid
Drag the `.mid` onto an empty MIDI track slot. Live keeps notes, velocities and lengths and
ignores the file tempo. Set the clip Scale and add the groove afterwards. Prefer rendering with
`--swing 50` and applying the Groove Pool in Live (editable); bake swing into the file only when
the user wants a fixed shuffle.
