# Rhythm: where the bass sits against a four-on-the-floor kick

## The grid and how to write it down

One bar of 4/4 = 16 steps = 16th notes. Count them "1 e & a, 2 e & a, 3 e & a, 4 e & a".

```
step:   1  2  3  4 | 5  6  7  8 | 9 10 11 12 | 13 14 15 16
count:  1  e  &  a | 2  e  &  a | 3  e  &  a |  4  e  &  a
kick:   X  .  .  . | X  .  .  . | X  .  .  .  |  X  .  .  .
```

Kick on steps 1, 5, 9, 13 is fixed in these genres. Every bass decision is a decision about
the other 12 steps, and about whether to play *on* the kick at all. Durations at 125 BPM:
quarter 480 ms, 8th 240 ms, 16th 120 ms. At 128 BPM a 16th is 117 ms.

## Why offbeat bass works

Placing bass notes between kicks (steps 3, 7, 11, 15, the "and"s) gives the two parts
alternate turns. The combined kick + bass pulse runs at double the kick's rate, so the track
drives forward while the kick stays an anchor the listener can always find. Because they
never land together there is no low-end collision, and sidechain ducking becomes a flavour
rather than a repair. This is the disco / synth-pop / hi-NRG lineage that house inherited.

## The four archetypes

### 1. Pedal / sustained (deep house, dub techno)
```
bass:  R  -  -  - | -  -  -  - | R  -  -  -  | -  -  -  .
```
One or two long root notes, or a note per chord change. The kick ducks it via sidechain.
Movement comes from the chords above and from the filter, not from the rhythm. Leave a small
gap before beat 1 so the attack retriggers.

### 2. Offbeat 8ths (classic house, tech house)
```
bass:  .  .  R  . | .  .  R  . | .  .  R  .  | .  .  R  .
```
Variations that keep it alive: move one note a 16th early (step 3 → step 2), replace one
"and" with an octave (step 15 = R+12), or add a 16th pickup on step 16 into the next bar.
Rule: start from four offbeats, then change *one* thing.

### 3. Syncopated / tresillo (groovy, jackin', funky house)
Tresillo is the 3+3+2 figure: accents on step 1, step 7 (the "and" of 2) and step 13 (beat 4),
or, when the bar is phrased to anticipate, on 1, the "and" of 2 and the "and" of 4. It is the
basis of the Cuban bass tumbao, and under a straight four-kick it reads as the "rubber band"
house bounce.
```
bass:  R  .  .  . | .  .  5  . | .  .  .  .  |  R  .  .  b7
```
Add ghost notes (same pitch, 25–45 velocity, very short) on steps 4, 8 or 12 to fill space the
way a funk player would with muted thumps. Add a chromatic pickup on step 16 into the next
root. Alternate call (bass busy, drums sparse) and response (bass rests, perc fills).

### 4. Rolling 16ths (tech house, minimal, techno)
```
bass:  .  R  R  5 | .  R  o  R | .  R  R  5  |  .  R  o  R      (o = octave)
```
Mostly 16ths from a small set, usually 3 pitches (root, 5th, octave, or root, b7, octave).
Leave the first 16th of every beat empty so the kick owns it; if you do play the kick slots,
make them the loudest notes (around 110) so they feel intentional. Change exactly one slot per
bar (an octave in bar 2, a rest in bar 3, a 5th in bar 4) so the ear hears movement without
losing the pattern. Shorten each 16th slightly so notes never touch; the sub stays clean.

## Swing

Swing (Roger Linn's MPC convention) is the share of each 8th note taken by its first 16th.
50 % is straight; 58 % delays every second 16th by 8 % of an 8th note (about 19 ms at
125 BPM); 66.7 % is a full triplet. Templates in Logic 16A–16F equal 50, 54, 58, 62, 66, 71 %.

Working ranges from producer practice:

| Style | Swing |
|---|---|
| Deep house | 52–56 % (often straight bass, swung hats) |
| Tech house / minimal | 56–58 % |
| Groovy / jackin' | 56–62 %, up to 65 % for a hard shuffle |
| Techno | 50–54 %, driving rather than shuffled |

Apply swing per clip (bass and hats), keep the kick straight, and remember that the
hardware you are imitating was never exact: 54 % on one MPC lands differently on another,
and the SP-1200 differs again. Swing only affects notes that sit on the even 16ths
(steps 2, 4, 6 …), so a pure offbeat-8th bass (steps 3, 7, 11, 15) is unaffected; swing it
by adding 16th pickups or by nudging.

## Velocity

Flat velocity is the first thing that makes a programmed bass sound like a preset.

- Downbeats / kick-aligned notes: 100–120.
- Offbeats: 80–100.
- Ghost notes: 25–45, roughly a fifth to a third of the main notes, and short. A ghost as
  loud as a main note flattens the groove.
- Grouping trick: lower every 4th 16th by 20–30 % so the line breathes in beats.
- Rolling-bass example from the Chris Stussy-style tutorials: 110 on the two kick-aligned
  slots, 85–95 elsewhere, one or two slots at 60.
- Route velocity to filter cutoff (and a little to amp) so accents open the sound; now the
  same pitches read as a phrase rather than a sequence.

## Note length (gate)

Gate = note length as a percentage of the step.

- Below 50 %: staccato, punchy, the funk-guitar / classic house feel. 10–25 % is a hard pluck.
- 50–90 %: standard "bouncy" house bass.
- 100 %+: notes overlap, legato; this is how you trigger slides in Operator / Wavetable
  (envelopes do not retrigger on overlapping notes when Voices = 1).
- Short notes on downbeats, longer notes on offbeats is a reliable tech-house shape: the long
  offbeat is what the ear hears as the "pull".
- Alternate gate across the bar instead of one value everywhere.
- Sub layer: never overlap two notes. Low notes have much better clarity when short.

## Micro-timing

Research on groove-based music puts expressive timing in the 10–40 ms range. Listeners detect
displaced kicks, snares and hats around 19–24 ms but need 31–35 ms before they notice a bass
being off. In listening tests, bass about 30 ms *ahead* of the drums and bass about 40 ms
*behind* were both rated as good as perfectly quantised, with a slight preference for
bass-ahead. The studies disagree on whether micro-timing improves groove at all, so treat it
as seasoning: nudge two or three off-downbeat notes by 5–15 ms (in Live, a 1/96 note is about
20 ms at 125 BPM), listen, and keep only what you like. Never shift the whole clip; that is
just latency.

## Phrasing (8 bars)

- Build in 8-bar blocks; sections in 8/16-bar multiples.
- Bars 1–3 identical, bar 4 small change (octave on the last beat, dropped note, extra ghost).
- Bars 5–7 like 1–3, bar 8 bigger change (pickup run, rest on beat 4, chromatic approach into
  the next phrase, or move the final note into the first open 8th of the next bar).
- Second drop: variation of the line (new slot choice, different octave on the pickups), not
  a new bassline.
- Call and response: where the bass has 16ths the percussion rests; where the bass rests the
  perc or a vocal chop answers.
- Minimal is the exception: one or two bass hits per bar and the *space* is the groove.
