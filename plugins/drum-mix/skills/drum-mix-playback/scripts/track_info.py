"""Print basic info for WAV files: sample rate, format, duration, peak, loudness.

Usage:
    python track_info.py                  # opens a folder dialog
    python track_info.py track1.wav track2.wav ...
    python track_info.py tracks_folder/

Read-only: input files are never modified.
"""

import sys
from pathlib import Path

import numpy as np
import pyloudnorm as pyln
import soundfile as sf

from folders import choose_input_folder

MIN_LOUDNESS_DURATION_S = 0.4
CLIP_THRESHOLD = 0.999


def analyze(path: Path) -> dict:
    audio, sample_rate = sf.read(path, always_2d=True)
    num_samples, num_channels = audio.shape
    duration_s = num_samples / sample_rate

    peak = float(np.max(np.abs(audio)))
    peak_dbfs = 20 * np.log10(peak) if peak > 0 else float("-inf")

    if duration_s >= MIN_LOUDNESS_DURATION_S:
        lufs = float(pyln.Meter(sample_rate).integrated_loudness(audio))
    else:
        lufs = float("nan")

    return {
        "file": path.name,
        "sample_rate": sample_rate,
        "channels": num_channels,
        "duration_s": round(duration_s, 2),
        "peak_dbfs": round(peak_dbfs, 1),
        "lufs": round(lufs, 1),
        "clipping": peak >= CLIP_THRESHOLD,
        "subtype": sf.info(path).subtype,  # e.g. PCM_24 = 24-bit
    }


def find_wav_files(args: list[str]) -> list[Path]:
    files = []
    for arg in args:
        path = Path(arg).expanduser()
        if path.is_dir():
            files.extend(sorted(path.glob("*.wav")))
        else:
            files.append(path)
    return files


def main() -> int:
    args = sys.argv[1:]
    if not args:
        folder = choose_input_folder(Path("~/Music"))
        if folder is None:
            print("Canceled.")
            return 1
        args = [str(folder)]

    files = find_wav_files(args)
    if not files:
        print(f"No WAV files found in: {', '.join(args)}")
        return 1

    for path in files:
        try:
            info = analyze(path)
        except Exception as error:
            print(f"✗ {path.name}: unreadable ({error})")
            continue

        warning = "  ⚠ CLIPPING" if info["clipping"] else ""
        print(
            f"{info['file']:<28} {info['sample_rate']} Hz  {info['subtype']:<7} "
            f"{info['channels']} ch  {info['duration_s']:>7} s  "
            f"peak {info['peak_dbfs']:>6} dBFS  {info['lufs']:>6} LUFS{warning}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
