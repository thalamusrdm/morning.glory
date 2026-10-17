---
name: ableton-house-bass
description: >-
  Write, analyse and improve MIDI basslines for house and techno in Ableton Live, with
  deep focus on deep house, tech house, groovy / jackin' / funky house and (Berlin-style)
  techno. Covers harmony (keys, modes, chord tones, approach notes, pedal tones), rhythm
  (offbeat vs rolling, tresillo, swing %, velocity, gate length, micro-timing), 8-bar
  phrasing, kick/bass tuning and the Ableton-specific workflow (Groove Pool, Live 12 MIDI
  Tools, Operator/Wavetable settings, sidechain). Ships a dependency-free Python script
  that renders ready-to-drag .mid clips. Use this skill whenever the user mentions a
  bassline, bass groove, sub, low end, "bass MIDI", 303/acid line, rolling bass, offbeat
  bass, or wants a house/techno track to "bounce", "roll", "groove" or "feel deeper", even
  if they do not say "bass" explicitly or do not name Ableton. Also use it when the user
  asks why a house loop sounds stiff, static or clashes with the kick.
---

# Ableton House & Techno Bass

The bassline is the groove of a house record. Kerri Chandler puts it bluntly: "the bassline
is the groove of the song". A kick on every quarter note is a fixed grid; the bass is the
part that decides whether the grid *walks*, *bounces* or *rolls*. This skill turns that
intuition into a repeatable method: choose the subgenre, pick a rhythmic archetype, pick the
notes, shape velocity / length / timing, then phrase it over 8 bars and lock it to the kick
in Ableton.

Answer in the language the user writes in (Hebrew users get Hebrew). Keep musical terms in
English alongside (e.g. "אופביט (offbeat)") so they can search for them.

## Read the right reference

Load only what the task needs, in this order:

| Situation | Read |
|---|---|
| Any new bassline | `references/rhythm.md` then `references/theory.md` |
| Deep house | `references/deep-house.md` |
| Tech house / minimal / deep tech | `references/tech-house.md` |
| Groovy, jackin', funky, disco or French house | `references/groovy-house.md` |
| Techno (rumble, rolling, hypnotic) | `references/techno.md` |
| Programming it in Live (Groove Pool, MIDI Tools, synth settings, sidechain) | `references/ableton-workflow.md` |
| Need a concrete grid to start from or to hand the user | `references/patterns.md` |
| User asks where a claim comes from | `references/sources.md` |

The generator lives in `scripts/make_bass_midi.py` (pure Python 3, no packages). Run
`python3 scripts/make_bass_midi.py --list` to see the built-in styles.

## The method (do these in order)

### 1. Fix the frame before writing a note
- **Tempo and subgenre.** Deep house 118–124 BPM, tech house 124–128, jackin'/funky
  122–128, techno 128–135+. Tempo decides how much 16th-note density the ear can take.
- **Key.** If there are chords, the bass takes the chord roots. If not, pick a key whose
  root sits in the sub sweet spot: fundamentals roughly E1 (41 Hz) to G2 (98 Hz). The most
  common house keys are A minor, F minor, G minor, C minor and D minor; techno leans on A, D,
  E minor and E Phrygian. (Ableton's piano roll labels MIDI 36 as **C1**, one octave lower
  than scientific pitch, so "A1 = 55 Hz" is shown as A0 in Live. Give the user MIDI numbers
  when it matters.)
- **Kick pitch.** Find the kick's fundamental (commonly 41–55 Hz, E1–A1). Either put the bass
  root on the same note an octave up, or on a consonant interval (5th, minor 3rd, 6th), never
  a few cents away from it: two near-identical low tones beat and the downbeat warbles.

### 2. Choose the rhythmic archetype
Kick sits on steps 1, 5, 9, 13 of a 16-step bar. The archetypes, in rising density:

1. **Pedal / sustained** (deep house): one or two long notes per bar, the kick ducks them.
2. **Offbeat 8ths** (classic house, tech house): notes on the "and"s, steps 3-7-11-15.
   Disco / hi-NRG lineage; kick and bass take turns so they never fight.
3. **Syncopated / tresillo** (groovy, jackin'): accents on 1, the "and" of 2 and 4
   (3+3+2), plus 16th pickups into the next downbeat. Rubbery, call-and-response with the drums.
4. **Rolling 16ths** (tech house, techno): most 16ths filled from a 3-note set, kick slots
   left empty or quiet, one slot changed per bar so it never sounds like a preset.

Pick one as the *core bar*. Everything else is variation of that bar.

### 3. Choose the notes
Backbone is root, 5th, octave. Colour comes from the mode: natural minor is the default;
Dorian's natural 6th is warmer (groovy, deep); Phrygian's b2 is the dark tech-house / techno
trick; minor pentatonic (1 b3 4 5 b7) is the safe melodic subset. Add **chromatic approach
notes** a semitone below or above a target on weak positions (the last 16th before beat 1 is
the classic pickup), and the funk **b7 → octave** walk. Under m7/m9 chords the bass usually
stays on the root or root-pedal; the 7th and 9th live in the chords, not the bass. Fewer
distinct pitches is almost always better: Larry Heard's "Can You Feel It" is six notes.

### 4. Shape it: velocity, length, timing
- **Velocity**: downbeats / kick-aligned 100–120, offbeats 80–100, ghosts 25–45
  (roughly 20–30 % of the main notes). Drop every 4th hit by 20–30 % to create grouping.
  Map velocity to filter cutoff on the synth so the accents open up.
- **Length (gate)**: under 50 % of the step is staccato / punchy house; 100 %+ overlaps for
  legato and slides. Short notes on downbeats, longer on offbeats is a modern tech-house
  rule of thumb. In the sub layer never let two notes overlap.
- **Swing**: Linn convention, 50 % = straight, 66.7 % = triplet. House 54–58 %, tech house
  56–58 %, jackin' up to 60–65 %. Keep the kick straight and swing the bass and hats per clip.
- **Micro-timing**: shifts of 10–40 ms are what the ear reads as "laid back" or "pushed";
  listeners only notice bass offsets above ~30 ms. Nudge two or three off-downbeat notes a
  few ms, not the whole clip. At 125 BPM a 16th is 120 ms.

### 5. Phrase it over 8 bars
Keep the core bar stable; change something at bars 4 and 8 (octave jump on the last beat,
pickup into the next phrase, dropped note, extra ghost). Second drop gets a variation, not a
new line. Write call-and-response with the drums: where the bass is busy the percussion
rests, and vice-versa.

### 6. Lock it in Ableton
Groove Pool (MPC 16 Swing-56/58, Timing as strength, tiny Random) on the bass clip only;
Live 12 clip Scale so MIDI Tools stay in key; Operator/Wavetable with Voices = 1, Glide for
slides, velocity → filter; sidechain compressor keyed from the kick, fast attack, release
timed so the bass is back up just before the next kick; bass mono below ~120 Hz; high-pass
any mid layer around 80–100 Hz so the sine sub owns the bottom. Details in
`references/ableton-workflow.md`.

## Deliverables

When the user wants a bassline, give all of these unless they ask for less:

1. **A 16-step grid** per bar (see format in `references/patterns.md`), with note names,
   MIDI numbers, velocities and gate, plus which bars vary and how.
2. **A rendered `.mid`** from `scripts/make_bass_midi.py` saved where the user can drag it
   into Live (project folder or a path they can open). Say the exact path.
3. **Synth and groove settings** for Live: instrument, Voices/Glide, velocity routing,
   Groove Pool choice and %, sidechain starting values.
4. **Why it works**, in two or three sentences tied to the rules above (interlocking with
   the kick, chord-tone choice, phrase shape). Avoid lectures; the user wants to make music.

When the user shows an existing bassline (MIDI, screenshot description or notes), diagnose
against the same checklist: density vs tempo, kick-slot collisions, pitch range vs kick,
velocity flatness, gate uniformity, absence of phrase-level variation, swing mismatch with
the hats.

## Example

User: "tech house, 126 BPM, F minor, kick is tuned to F. I want it to roll."

Response outline: rolling-16th archetype; 3-note set F1-C2-F2 (MIDI 29-36-41), kick slots
1/5/9/13 empty, slot 16 = E1 chromatic pickup at low velocity every 4th bar; velocities 112
on step 3 and 11, 90 elsewhere, ghosts 40 on steps 4 and 12; gate 60 % offbeats / 40 %
others; Groove MPC 16 Swing-57 at 100 % Timing; Operator, Voices 1, saw-ish Operator B
feeding A, velocity → filter 30 %; sidechain from kick, attack 0.1 ms, release ≈ 90 ms. Then
run the script with `--style tech-rolling --key Fm --bpm 126 --bars 8 --swing 57`.
