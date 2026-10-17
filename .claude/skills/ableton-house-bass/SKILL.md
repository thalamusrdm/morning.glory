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

The bassline is the groove of a house record. Kerri Chandler builds tracks bass-first; Larry
Heard's "Can You Feel It" is six notes on a Juno-60. A kick on every quarter note is a fixed
grid; the bass decides whether the grid *walks*, *bounces* or *rolls*. This skill turns that
into a repeatable method: fix the frame, pick a rhythmic archetype, pick the notes, shape
velocity / length / timing, phrase it over 4 and 8 bars, lock it to the kick in Ableton.

Answer in the language the user writes in (Hebrew users get Hebrew). Keep musical terms in
English alongside (e.g. "אופביט (offbeat)") so they can search for them.

## Read the right reference

Load only what the task needs, in this order:

| Situation | Read |
|---|---|
| Any new bassline | `references/rhythm.md` then `references/theory.md` |
| Deep house | `references/deep-house.md` |
| Tech house / deep tech / minimal | `references/tech-house.md` |
| Groovy, jackin', funky, disco or French house | `references/groovy-house.md` |
| Techno, rumble, acid | `references/techno.md` |
| Programming it in Live (Groove Pool, MIDI Tools, synth settings, sidechain) | `references/ableton-workflow.md` |
| Need a concrete grid to start from or to hand the user | `references/patterns.md` |
| User asks where a claim comes from | `references/sources.md` (all articles read in full) |

The generator is `scripts/make_bass_midi.py` (Python 3, no packages). `--list` shows 28
built-in styles; `--pattern` takes the grid notation from `references/patterns.md`.

## The method

### 1. Fix the frame before writing a note
- **Tempo decides the genre.** Deep house 120–124 (modal 122), tech house 125–128 (126),
  minimal house 124–128, deep tech 124–127, minimal techno 124–130, Berlin techno 128–138.
  "If you're writing at 126 you're not making deep house anymore." Density that works at 124
  clutters at 128.
- **Key.** With chords, the bass takes the chord roots and the voicing moves with it. Without,
  pick a root whose fundamental sits in E1–G2 (41–98 Hz). Common: A minor first, then F, G, C,
  D minor; techno A / D / E minor and E Phrygian. Ableton labels MIDI 36 as **C1**, one octave
  lower than scientific pitch; give MIDI numbers when it matters.
- **Kick pitch.** Tuner on the kick's body (not the transient); labels lie. Bass root = same
  note an octave up, or 5th / minor 3rd / 6th. Never a few cents off (beating). Repitch the kick
  up to ±2 semitones if needed.
- **Bass philosophy per genre.** Tech house: rolling 3–5 notes, second-loudest element. Deep
  house: 2–4 sustained notes, felt not heard. Minimal: 1–2 percussive stabs, the gap is the
  groove. Techno: hypnosis through sameness. Jackin' / funky: a player's line with ghosts and
  pickups.

### 2. Choose the rhythmic archetype (details in `rhythm.md`)
Kick on steps 1, 5, 9, 13 of 16. The bass's one anchor is the downbeat; everything else lives
between kicks ("the macro groove": bass and perc share the same accent map).

1. **Pedal / sustained**: deep house, 20–50 ms portamento between long notes.
2. **Offbeat 8ths** (3-7-11-15): classic / tech house. Four notes, then break the symmetry:
   third note a 16th early, fourth up an octave or to the 5th. Long-then-short contrast
   ("and" of 1 sustained, "and" of 2 punchy) is where the groove lives.
3. **Tresillo / habanera / anticipation** (3+3+2): groovy, jackin'. Ghosts in front of notes,
   turnaround to the 5th, pickups into the next bar.
4. **Rolling 16ths**, two philosophies: kick slots *empty* (techno, Attack / Zen World) or tonic
   *on* the kick and ducked (Chris Stussy map: R q q q | 5 R o R, 110 on the kick slots, 90 on
   the "and"s, 70–80 elsewhere; downbeats 60 % gate, offbeats 90–100 %). Vary one slot per bar;
   bar 4 ends with a chromatic walk 5 → b6 → 6 → b7 into the next tonic.
5. **Rolling 8ths** on one pitch, 10–15 % velocity randomisation, half-step dip on beat 3.
6. **Stab and sustain** for peak time; **slides** over a 4-bar arc (root, root, sliding 4th/5th,
   resolve).

### 3. Choose the notes (details in `theory.md`)
Root / 5th / octave backbone (or root / b3 / 5th under a minor-triad stab). Natural minor by
default; Dorian's 6th for warmth (the im7 → IV7 vamp is the Larry Heard sound); Phrygian's b2
as a short approach for darkness. Chromatic approach notes on weak positions only. 7ths and
9ths live in the chords, not the bass. Write the pattern first with a plain sine; "the
difference is almost never the synth".

### 4. Shape it
- **Velocity skeleton**: 110 kick slots / 90 "and"s / 70–80 fillers, randomised within bands;
  ghosts 20–30 % of main, short, low-passed. Route velocity to cutoff (20–40 %).
- **Gate**: short on downbeats, long on offbeats; sub layer never overlaps. Silence between
  notes is the bounce.
- **Swing**: Linn convention, 50 straight. House 54–58, rolling tech house 56–58 (MPC 16 Swing
  58/62 template on the bass clip, kick straight), minimal 52–56 at 10–30 % Timing, jackin'
  56–62, techno 50–54. Dense rolling lines want it; sparse offbeat lines often stay straight
  with only the hats swung.
- **Micro-timing**: research says a consistent whole-track offset up to ~30 ms is unnoticed,
  while random per-note jitter *lowers* groove ratings. So: Track Delay for laid-back feel, and
  if you nudge single notes (2–3 per bar, 5–15 ms), nudge the *same* ones every bar. Groove
  Pool Random near zero on bass.

### 5. Phrase it
4-bar shape inside 8-bar phrases: bar 1 full, bar 2 one slot changed, bar 3 a 30 ms anticipation
on the last offbeat, bar 4 a fill; verse moves, drop plays bar 1 looped. Change one thing every
8 bars. Call-and-response with the perc.

### 6. Lock it in Ableton (details in `ableton-workflow.md`)
Clip Scale on; Groove Pool on the bass clip only (Timing as strength, Velocity 0 if you only
want timing, Commit late); Operator / Wavetable / Drift with Voices 1, Glide for slides,
velocity → filter; sidechain compressor keyed from the kick: attack 0.1–2 ms, release 80–130 ms
at 124–126 BPM (deep house 120–180, techno 50–100), 4–7 dB, soft knee, or band-mode on the low
band only; sine sub + mid layer high-passed 65–100 Hz; mono below 120 Hz. Live 12 shortcuts:
Seed (pitch range a 5th, Duration 1/16–1/16, Voices 1, Density 50 %), Euclidean for tresillo
voices, Velocity Shaper for the skeleton, Audio-to-MIDI from a percussion loop for a played
rhythm.

## The five reasons a bass feels stiff (check in this order)
1. All notes the same velocity. 2. All notes the same length. 3. No swing on a rolling line.
4. Polyphonic voice (overlaps muddy the low end). 5. Sidechain missing, or so deep you hear the
duck. "Nine times out of ten the fix is in there."

## Deliverables

When the user wants a bassline, give all of these unless they ask for less:

1. **A 16-step grid** per bar in the `patterns.md` notation, with note names, MIDI numbers,
   velocities and gate, plus which bars vary and how.
2. **A rendered `.mid`** from `scripts/make_bass_midi.py` saved where the user can drag it
   into Live (project folder or a path they can open). Say the exact path. Prefer `--swing 50`
   and let them add the Groove Pool template, unless they want the shuffle baked in.
3. **Synth and groove settings** for Live: instrument, Voices / Glide, velocity routing,
   Groove Pool template and %, sidechain starting values.
4. **Why it works**, in two or three sentences tied to the rules above. No lectures.

When the user shows an existing bassline (MIDI, screenshot description or notes), diagnose
against the five-reasons list plus: density vs tempo, kick-slot collisions, pitch range vs
kick fundamental, absence of a 4-bar shape, swing mismatch with the hats, pads or stabs
sitting in the 80–250 Hz band where the bass movement lives.

## Example

User: "tech house, 126 BPM, F minor, kick is tuned to F. I want it to roll."

Response outline: Stussy rolling map in F minor, set F1–C2–F2 (MIDI 29-36-41); tonic on the
kick slots at 110 and 60 % gate, 5th and octave on the offbeats at 90 with 95 % gate, quiet
tonics at 75 in between; bar 2 drops the first octave, bar 3 anticipates slot 15 by 30 ms,
bar 4 walks C → C# → D → Eb into F. Groove MPC 16 Swing-58 on the bass clip, kick straight.
Operator: A sine, B saw at low level, D sine an octave down, Voices 1, Glide off, filter LP24
~200 Hz with envelope 40 %, Vel → filter 30 %. Compressor sidechained from the kick: attack
1 ms, release 110 ms, 4:1, 5–7 dB. Then:
`python3 scripts/make_bass_midi.py --style tech-stussy --key Fm --bpm 126 --bars 8 --swing 50 --out <project>/bass_Fm_rolling.mid`
