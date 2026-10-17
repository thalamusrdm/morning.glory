#!/usr/bin/env python3
"""Render house / techno bassline grids to a Standard MIDI File (type 0, 480 PPQ).

No third-party packages. Works with Python 3.8+.

Examples
--------
    python3 make_bass_midi.py --list
    python3 make_bass_midi.py --style tech-rolling --key Fm --bpm 126 --bars 8 --out bass.mid
    python3 make_bass_midi.py --pattern "R . . g . . 5 . . . R g R . . b7" --key Am --bpm 124 \
        --bars 8 --swing 58 --out groovy.mid
    python3 make_bass_midi.py --style deep-pedal --key Gm --octave 1 --humanize 8 --out deep.mid

Grid notation (one bar = 16 tokens separated by spaces, bars separated by '|'):
    .        rest                     -        tie (extend previous note one step)
    R or 1   root                     g        ghost (root, velocity ~38, gate 20 %)
    o / O    root +1 / +2 octaves     _        root -1 octave
    b2 2 b3 3 4 5 b6 6 b7 7 9        semitone offsets above the root
    x@110    velocity override        x:40     gate % override        x@110:40 both
    x+       nudge early (humanize)   x~       nudge late

Variation bars: --vary makes bar 4 and bar 8 of each 8-bar phrase differ (octave on the
last offbeat in bar 4, pickup and dropped note in bar 8) when a single-bar pattern is given.

Pitch names: the script prints scientific pitch (C2 = MIDI 36). Ableton Live displays
MIDI 36 as C1, one octave lower in name; the sound is identical.
"""
from __future__ import annotations

import argparse
import random
import struct
import sys
from dataclasses import dataclass, field
from typing import List, Optional, Sequence, Tuple

PPQ = 480
STEP = PPQ // 4            # one 16th note in ticks
STEPS_PER_BAR = 16
KICK_STEPS = {0, 4, 8, 12}  # zero-based

DEGREES = {
    "R": 0, "1": 0, "b2": 1, "2": 2, "b3": 3, "3": 4, "4": 5, "5": 7,
    "b6": 8, "6": 9, "b7": 10, "7": 11, "9": 14, "o": 12, "O": 24, "_": -12,
}
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
FLAT_TO_SHARP = {"Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#", "Bb": "A#", "Cb": "B", "Fb": "E"}

# ---------------------------------------------------------------------------
# Built-in styles: (description, default bpm, default swing %, pattern string)
# ---------------------------------------------------------------------------
STYLES = {
    "deep-pedal": (
        "Deep house: root pedal held across the bar with a 5th pickup (118-124 BPM)",
        122, 50,
        "R - - - - - . . . . R - . . . 5@70",
    ),
    "deep-sway": (
        "Deep house: two-note sway, bass as the quiet lead",
        122, 52,
        "R - - - . . R - . . . . R - . .",
    ),
    "deep-sixnote": (
        "Deep house: bouncing 4-pitch line in the 'Can You Feel It' spirit, bass as lead (2-bar loop)",
        120, 50,
        "R . . R . . b7 . . . 5 . . . R . | R . . R . . b7 . . . 5 . . b3 . .",
    ),
    "tech-offbeat": (
        "Tech house: offbeat 8ths with octave + short pickup on the last beat (124-128 BPM)",
        126, 57,
        ". . R . . . R . . . R . . . o R:30@60",
    ),
    "tech-stumble": (
        "Tech house: offbeat 8ths with the second note pulled a 16th early",
        126, 57,
        ". . R . . R . . . . R . . . R .",
    ),
    "tech-rolling": (
        "Tech house / minimal: rolling 16ths from root-5th-octave, kick slots empty, one slot varies per bar",
        126, 57,
        ". R R 5 . R R o . R R 5 . R R o | . R R 5 . R o o . R R 5 . R R . | "
        ". R R 5 . R R o . R 5 5 . R R o | . R R 5 . R R o . R R 5 . R o b7@70",
    ),
    "tech-rolling-b7": (
        "Tech house: rolling 16ths from root-b7-octave",
        126, 57,
        ". R b7 R . o R b7 . R b7 R . o R .",
    ),
    "tech-minimal": (
        "Minimal: two percussive hits per bar, the gaps are the groove",
        127, 56,
        ". . R:35 . . . . . . . R:35 . . . . .",
    ),
    "tech-phrygian": (
        "Tech house: offbeat 8ths with a Phrygian b2 pickup into the next bar",
        126, 57,
        ". . R . . . R . . . R . . . R b2@65:40",
    ),
    "groovy-tresillo": (
        "Groovy / jackin': 3+3+2 tresillo accents with ghost notes and a b7 pickup (122-128 BPM)",
        125, 59,
        "R . . g . . 5 . . . R g R . . b7@70",
    ),
    "groovy-anticipate": (
        "Groovy: anticipated tresillo, last accent tied over the barline",
        125, 59,
        "R . . . . . R . . . . . . . 5 -",
    ),
    "disco-octave": (
        "Disco / French house: 8ths alternating root and octave, doubled at the phrase end",
        124, 54,
        "R . o . R . o . R . o . R . o o",
    ),
    "groovy-dorian": (
        "Groovy: Dorian noodle line that resolves to the root on beat 1",
        125, 58,
        "R . . 6 . . 5 . . b7 . . R . . .",
    ),
    "techno-rolling": (
        "Techno: single pitch on every 16th except kick slots, velocity cycle 50/127/75 (128-135 BPM)",
        132, 51,
        ". R@50 R@127 R@75 . R@50 R@127 R@75 . R@50 R@127 R@75 . R@50 R@127 R@75",
    ),
    "techno-offbeat": (
        "Techno: offbeat sub on the 'and's",
        132, 50,
        ". . R . . . R . . . R . . . R .",
    ),
}

# Default velocities by step position (zero-based)
def default_velocity(step: int) -> int:
    if step in KICK_STEPS:
        return 110
    if step % 4 == 2:          # offbeat 8ths (steps 3,7,11,15 one-based)
        return 100
    return 88

DEFAULT_GATE = 65
GHOST_VELOCITY = 38
GHOST_GATE = 20


@dataclass
class Note:
    start: int          # ticks
    length: int         # ticks
    pitch: int
    velocity: int
    nudge: int = 0      # ticks, may be negative


@dataclass
class Token:
    kind: str                       # "rest", "tie", "note"
    semitones: int = 0
    velocity: Optional[int] = None
    gate: Optional[int] = None
    ghost: bool = False
    nudge: int = 0                  # -1 early, +1 late, 0 none


def parse_token(raw: str) -> Token:
    s = raw.strip()
    if s == ".":
        return Token("rest")
    if s == "-":
        return Token("tie")
    nudge = 0
    if s.endswith("+"):
        nudge, s = -1, s[:-1]
    elif s.endswith("~"):
        nudge, s = 1, s[:-1]
    velocity = gate = None
    # split overrides: body[@vel][:gate] in any order
    body = ""
    i = 0
    while i < len(s) and s[i] not in "@:":
        body += s[i]
        i += 1
    rest = s[i:]
    while rest:
        marker, rest = rest[0], rest[1:]
        num = ""
        while rest and rest[0].isdigit():
            num += rest[0]
            rest = rest[1:]
        if not num:
            raise ValueError(f"bad override in token {raw!r}")
        if marker == "@":
            velocity = max(1, min(127, int(num)))
        else:
            gate = max(1, min(400, int(num)))
    if body == "g":
        return Token("note", 0, velocity or GHOST_VELOCITY, gate or GHOST_GATE, True, nudge)
    if body not in DEGREES:
        raise ValueError(f"unknown token {raw!r}; valid: {' '.join(sorted(DEGREES))} . - g")
    return Token("note", DEGREES[body], velocity, gate, False, nudge)


def parse_pattern(pattern: str) -> List[List[Token]]:
    bars = []
    for bar_txt in pattern.split("|"):
        toks = [parse_token(t) for t in bar_txt.split()]
        if len(toks) != STEPS_PER_BAR:
            raise ValueError(f"each bar needs {STEPS_PER_BAR} tokens, got {len(toks)} in: {bar_txt.strip()!r}")
        bars.append(toks)
    return bars


def parse_key(key: str) -> Tuple[int, str]:
    """Return (pitch class 0-11, mode string). Accepts 'Am', 'F#m', 'Bb minor', 'C', 'E phrygian'."""
    k = key.strip()
    if not k:
        raise ValueError("empty key")
    name = k[0].upper()
    rest = k[1:]
    if rest[:1] in ("#", "b"):
        name += rest[0]
        rest = rest[1:]
    name = FLAT_TO_SHARP.get(name, name)
    if name not in NOTE_NAMES:
        raise ValueError(f"unknown key root {key!r}")
    mode = rest.strip().lower().lstrip("-_ ") or "minor"
    if mode in ("m", "min"):
        mode = "minor"
    return NOTE_NAMES.index(name), mode


def root_midi(pitch_class: int, octave: int) -> int:
    """Scientific pitch: C2 = 36. octave=1 → C1 = 24."""
    return 12 * (octave + 1) + pitch_class


def note_name(midi: int) -> str:
    return f"{NOTE_NAMES[midi % 12]}{midi // 12 - 1}"


def ableton_name(midi: int) -> str:
    return f"{NOTE_NAMES[midi % 12]}{midi // 12 - 2}"


def apply_variations(bars: List[List[Token]], total_bars: int) -> List[List[Token]]:
    """Expand a pattern to total_bars; if the source is one bar, vary bars 4 and 8 of each phrase."""
    out: List[List[Token]] = []
    n = len(bars)
    for b in range(total_bars):
        src = [Token(**vars(t)) for t in bars[b % n]]
        if n == 1:
            pos = b % 8
            if pos == 3:  # bar 4: last sounding offbeat goes up an octave
                for i in (14, 15, 13, 12, 11, 10):
                    if src[i].kind == "note" and not src[i].ghost:
                        src[i].semitones += 12 if src[i].semitones < 12 else -12
                        break
            elif pos == 7:  # bar 8: drop one mid-bar note, add a b7 pickup on the last step
                dropped = False
                for i in (9, 10, 11, 8):
                    if src[i].kind == "note" and not src[i].ghost and not dropped:
                        src[i] = Token("rest")
                        # also kill a tie that depended on it
                        if i + 1 < 16 and src[i + 1].kind == "tie":
                            src[i + 1] = Token("rest")
                        dropped = True
                if src[15].kind != "tie":
                    src[15] = Token("note", 10, 70, 40, False, 0)
        out.append(src)
    return out


def render(bars: List[List[Token]], root: int, swing: float, gate_default: int,
           humanize_ms: float, bpm: float, rng: random.Random) -> List[Note]:
    notes: List[Note] = []
    ms_per_tick = 60000.0 / bpm / PPQ
    eighth = STEP * 2
    swing_delay = int(round((swing - 50.0) / 100.0 * eighth))  # ticks added to even 16ths
    current: Optional[Note] = None
    for bar_i, bar in enumerate(bars):
        for step_i, tok in enumerate(bar):
            abs_step = bar_i * STEPS_PER_BAR + step_i
            grid = abs_step * STEP
            if tok.kind == "tie":
                if current is not None:
                    current.length += STEP
                continue
            current = None
            if tok.kind == "rest":
                continue
            start = grid + (swing_delay if step_i % 2 == 1 else 0)
            vel = tok.velocity if tok.velocity is not None else default_velocity(step_i)
            gate = tok.gate if tok.gate is not None else gate_default
            length = max(10, int(STEP * gate / 100.0))
            nudge = 0
            if tok.nudge:
                nudge = tok.nudge * int(round(10.0 / ms_per_tick))  # 10 ms
            elif humanize_ms > 0 and step_i not in KICK_STEPS:
                nudge = int(round(rng.uniform(-humanize_ms, humanize_ms) / ms_per_tick))
            n = Note(start, length, root + tok.semitones, vel, nudge)
            notes.append(n)
            current = n
    # Avoid overlaps in a monophonic bass: trim each note to the next note's start.
    notes.sort(key=lambda n: n.start + n.nudge)
    for a, b in zip(notes, notes[1:]):
        a_start, b_start = a.start + a.nudge, b.start + b.nudge
        if a_start + a.length > b_start - 2:
            a.length = max(10, b_start - a_start - 2)
    return notes


# ---------------------------------------------------------------------------
# SMF writing
# ---------------------------------------------------------------------------
def vlq(value: int) -> bytes:
    out = bytearray([value & 0x7F])
    value >>= 7
    while value:
        out.insert(0, 0x80 | (value & 0x7F))
        value >>= 7
    return bytes(out)


def write_midi(path: str, notes: Sequence[Note], bpm: float, total_ticks: int, track_name: str) -> None:
    events: List[Tuple[int, int, bytes]] = []  # (tick, order, data)
    for n in notes:
        on = max(0, n.start + n.nudge)
        off = on + n.length
        events.append((on, 1, bytes([0x90, n.pitch & 0x7F, n.velocity & 0x7F])))
        events.append((off, 0, bytes([0x80, n.pitch & 0x7F, 0x40])))
    events.sort(key=lambda e: (e[0], e[1]))

    track = bytearray()
    name_b = track_name.encode("utf-8")
    track += vlq(0) + b"\xFF\x03" + vlq(len(name_b)) + name_b
    tempo = int(round(60_000_000 / bpm))
    track += vlq(0) + b"\xFF\x51\x03" + struct.pack(">I", tempo)[1:]
    track += vlq(0) + b"\xFF\x58\x04" + bytes([4, 2, 24, 8])
    last = 0
    for tick, _, data in events:
        track += vlq(tick - last) + data
        last = tick
    end_tick = max(total_ticks, last)
    track += vlq(end_tick - last) + b"\xFF\x2F\x00"

    with open(path, "wb") as f:
        f.write(b"MThd" + struct.pack(">IHHH", 6, 0, 1, PPQ))
        f.write(b"MTrk" + struct.pack(">I", len(track)) + bytes(track))


def print_grid(bars: List[List[Token]], notes: List[Note], root: int) -> None:
    by_start = {}
    for n in notes:
        by_start.setdefault(n.start // STEP, n)
    print("step :  " + " ".join(f"{i+1:>3}" for i in range(16)))
    print("kick :  " + " ".join(f"{'X' if i in KICK_STEPS else '.':>3}" for i in range(16)))
    for b, bar in enumerate(bars):
        row, vel = [], []
        for s, tok in enumerate(bar):
            idx = b * 16 + s
            n = by_start.get(idx)
            if tok.kind == "tie":
                row.append("  -"); vel.append("   ")
            elif n is None:
                row.append("  ."); vel.append("   ")
            else:
                row.append(f"{note_name(n.pitch):>3}"); vel.append(f"{n.velocity:>3}")
        print(f"bar {b+1:>2}: " + " ".join(row))
        print("   vel: " + " ".join(vel))
    pitches = sorted({n.pitch for n in notes})
    print("pitches (scientific / Ableton display / MIDI): " +
          ", ".join(f"{note_name(p)} / {ableton_name(p)} / {p}" for p in pitches))


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="list built-in styles and exit")
    ap.add_argument("--style", choices=sorted(STYLES), help="built-in pattern")
    ap.add_argument("--pattern", help="custom grid (see notation above); overrides --style")
    ap.add_argument("--key", default="Am", help="root and mode, e.g. Am, F#m, Gm, 'E phrygian' (mode is informational)")
    ap.add_argument("--octave", type=int, default=1, help="octave of the root in scientific pitch (1 → A1 = 55 Hz for Am). Default 1")
    ap.add_argument("--bpm", type=float, help="tempo written to the file (default per style, else 125)")
    ap.add_argument("--bars", type=int, default=8, help="bars to render (default 8)")
    ap.add_argument("--swing", type=float, help="MPC-style swing %% baked into even 16ths; 50 = straight. Default per style. Prefer 50 + Groove Pool")
    ap.add_argument("--gate", type=int, default=DEFAULT_GATE, help="default note length as %% of a 16th (default 65)")
    ap.add_argument("--humanize", type=float, default=0.0, help="random nudge in ms for non-kick steps (try 5-10)")
    ap.add_argument("--no-vary", action="store_true", help="repeat a single-bar pattern verbatim (no bar 4/8 variation)")
    ap.add_argument("--seed", type=int, default=7, help="random seed for --humanize")
    ap.add_argument("--out", default="bass.mid", help="output .mid path")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    if args.list:
        for name, (desc, bpm, swing, pat) in STYLES.items():
            print(f"{name:<18} {bpm:>3} BPM  swing {swing:>2}%  {desc}")
            print(f"{'':<18} {pat}")
        return 0

    if not args.pattern and not args.style:
        ap.error("give --style or --pattern (or --list)")

    if args.pattern:
        pattern, bpm, swing = args.pattern, args.bpm or 125.0, args.swing if args.swing is not None else 50.0
        style_name = "custom"
    else:
        desc, sbpm, sswing, pattern = STYLES[args.style]
        bpm = args.bpm or sbpm
        swing = args.swing if args.swing is not None else sswing
        style_name = args.style

    try:
        bars = parse_pattern(pattern)
        pc, mode = parse_key(args.key)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    root = root_midi(pc, args.octave)
    if root < 24 or root > 60:
        print(f"warning: root {note_name(root)} (MIDI {root}) is outside the usual bass range E1-G2", file=sys.stderr)

    if args.no_vary:
        full = [bars[i % len(bars)] for i in range(args.bars)]
    else:
        full = apply_variations(bars, args.bars)
    rng = random.Random(args.seed)
    notes = render(full, root, swing, args.gate, args.humanize, bpm, rng)
    write_midi(args.out, notes, bpm, args.bars * STEPS_PER_BAR * STEP, f"{style_name} bass {args.key}")

    if not args.quiet:
        print(f"{style_name}: key {NOTE_NAMES[pc]} {mode}, root {note_name(root)} (Ableton shows {ableton_name(root)}, MIDI {root}), "
              f"{bpm:g} BPM, {args.bars} bars, swing {swing:g}%, {len(notes)} notes -> {args.out}")
        print_grid(full, notes, root)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:  # e.g. piped into `head`
        sys.exit(0)
