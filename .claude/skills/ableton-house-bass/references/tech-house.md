# Tech house, deep tech and minimal bass

**Frame.** Tech house 125–128 BPM (modal 126); the Producer School's pattern guide works at
128–132, Chris Lake-style at 120–126. Keys A minor, A# minor, G minor most common. The bass is
the hook and the second-loudest element after the kick. Drum bus is dense: closed hats on
every 16th, open hat on the offbeats, 5–7 percussion elements. Minimal house shares the tempo
but not the bass philosophy: stabs, not lines. Deep tech (124–127, Max Dean, Solid Grooves)
takes tech house energy with a subbier, more sustained bass and sparser drums.

Reference tracks: Chris Stussy "Mama" / "On The Move", Solardo "On The Corner", Patrick
Topping "Forget", Cloonee "Drunk Dial", Toman "What's Up", Max Dean "Get Down", FISHER
"Losing It". High-cut a reference at 500 Hz to hear the bass pattern alone.

## The five patterns (Producer School) plus the rolling 3-note

### 1. Syncopated offbeat
```
step:  1  2  3  4 | 5  6  7  8 | 9 10 11 12 | 13 14 15 16
bass:  .  .  R  - | -  -  R:30 . | . .  R  .  |  .  .  o  R:30
```
Bass on the "and"s. A sustained note on the "and" of 1 breathes through beat 2, then a short
punchy note on the "and" of 2; the long/short contrast is the groove. A few semitones of
upward pitch modulation on the sustained note adds life. Range around E and G for body and
character. Velocity → cutoff so accents open the filter; "the same rhythmic pattern feels
constantly alive".

Variation: add a few extra 16ths between the main hits, pitch the first hit up an octave, give
one extra note more velocity. "Even with only four extra notes added, the whole vibe changes."
Keep it selective; do not fill every 16th.

Chris Lake variant: notes on steps 7 and 15 only (Live 1.2.3 and 1.4.3), slides between them,
saw + sine an octave below, low-pass 200–300 Hz, LFO on cutoff synced to 1/8 or 1/16.

### 2. Rolling 8ths
Eight even hits, one pitch. Tight transient, tail gone before the next note. 10–15 % velocity
randomisation. Drop a half-step on beat 3 and return on beat 4, or a short riff every 2 bars.

### 3. Ghost-note bass
Quiet hits on the 16ths between kick and clap at 20–30 % of main velocity, short, low-passed.
"Pull them out and the groove goes flat. That's when you know they're working."

### 4. Slides
Root for two bars, sliding 4th or 5th in bar 3, resolve in bar 4. Mono legato, slide time
20–80 ms, overlapping notes, filter envelope opening on the slide. Gliding 303-style bass needs
a sound with body *and* high-end crunch or the glide does not translate; build the foundation
rhythm first, then add octave jumps and glide notes gradually.

### 5. Stab and sustain
Stab anchored on the kick, sustain bleeding across beats 2–3. Fast-attack compressor on the
sustain; filter automation across sections. Also the basis of the call-and-response approach:
a sustained "call" plus a rhythmic "response" layer, leaving room for drums and a top line.

### 6. Rolling 3-note 16ths (the Chris Stussy / Max Dean / Toman / Cloonee lane)
Full slot map, velocities, gates, swing and the 4-bar shape are in `rhythm.md` (archetype 4b).
Summary:
- Set: tonic / 5th / octave (Stussy) or tonic / b3 / 5th (Cloonee). Pattern is interval-based,
  transposes to any key.
- Tonic on the kick slots (1, 9) at 110, 60 % gate; "and"s at 90, 90–100 % gate; fillers 70–80,
  70–80 % gate; slots 2–4 and 10–12 quiet tonics rather than silence.
- MPC 16 Swing 58 or 62 template on the bass clip only, landing at 56–58 %. Then 2–3 manual
  nudges per bar of 5–15 ms, the same ones every bar.
- Vary one slot per bar; bar 4 ends with a chromatic walk 5 → b6 → 6 → b7 into the next tonic.
- Mono voice is mandatory; glide 0 for this pattern.
- The rolling band is 80–250 Hz; a sine sub underneath; chord stab high-passed above 300 Hz;
  hats panned 15–25 % off centre.

### 7. Full 16ths
Every slot filled, velocities pulled down across the board so nothing dominates; the kick
sidechain does the shaping. Denser and more "glued" than offbeat; takes more space.

### 8. Minimal stab
One or two percussive hits per bar (fast attack, fast decay), the kick carries the weight.
"If your bass is a constant rolling pattern you're writing tech house with sparse drums."

## Sound

- **Stussy patch, translated.** Serum original: Osc A sine 100 %, Osc B saw 30–40 % detuned
  5–8 cents, sub sine -1 oct 70 %; LP 24 dB at 200 Hz, res 5–10 %; filter env A 1 ms D 80 ms
  S 30 % R 100 ms, amount 40 % (cutoff opens to 600–800 Hz on each attack); amp env A 1 D 200
  S 60 R 80; mono on, glide 0, bend 0. In Live: Operator with A sine, B saw at low level,
  D sine one octave down (or a second Operator for the sub), filter LP24 ~200 Hz with Env 40 %;
  or Wavetable Osc 1 sine + Osc 2 Basic Shapes saw at -10 dB, Sub on, Filter 1 LP24, Env 2 →
  Filter 1 Freq 40 %, Mono. Name it and reuse it.
- **Offbeat / bounce patch.** Sine or triangle sub below 100 Hz plus a mid layer: slightly
  detuned saw or square with a resonant low-pass around 400–800 Hz. Amp attack 0, decay
  150–250 ms, low sustain, short release. Portamento 30–60 ms on one or two notes per bar.
- Velocity → cutoff 20–40 %, a little → amp; try resonance too.
- 303-ish gliding bass: saw or square, resonant filter, mono legato, portamento.

## Sidechain

| Source | Attack | Release | Ratio | Depth |
|---|---|---|---|---|
| Producer School, rolling @124 | 1–2 ms | 90–130 ms (110 default) | 4:1–6:1, soft knee 3–6 dB | 5–7 dB |
| Myloops, offbeat @125 | 0.1–1 ms | 80–120 ms, "back at 0 dB just before the next kick" | 4:1 | 4–6 dB |
| Niek (Producer School) | band-mode sidechain on the low band so the mids stay audible | | | |

Too short a release gives obvious "wub" pumping, too long buries the roll. At 124 BPM a 16th
is 121 ms, so the release should settle before the next 16th. A volume shaper (LFO Tool,
ShaperBox, Kickstart) with a sharp drop and exponential recovery is often more musical than a
compressor and can add swing by letting the first bass note of each beat start below full
level.

## The five reasons a tech house bass feels stiff (Producer School)

1. All notes the same velocity.
2. All notes the same length.
3. No swing (56–58 % is the minimum for rolling lines).
4. Polyphonic voice; overlapping notes muddy the low end. Mono is mandatory.
5. Sidechain absent or so aggressive you hear the duck instead of the groove.

Walk the list in order; "nine times out of ten the fix is in there".

## Diagnosis checklist
- Sounds like a preset loop → vary one slot per bar, add the velocity skeleton, swing the clip.
- Kick disappears → bass fundamental equals the kick's or the sub layer overlaps; octave up,
  notch at the kick fundamental, or empty the kick slots.
- No bounce → gate uniform; lengthen the offbeats, shorten the others.
- Too busy at 128 → drop from 16ths to offbeat 8ths.
- Bassline great solo, vanishes in the mix → pads or stabs sit in 80–250 Hz; high-pass them
  above 300 Hz.
