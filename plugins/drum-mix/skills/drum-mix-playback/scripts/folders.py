"""Native macOS folder pickers for choosing the input tracks and the render destination."""

from __future__ import annotations  # macOS ships Python 3.9: keep `Path | None` hints working

import shutil
import subprocess
from pathlib import Path

USER_CANCELED = "-128"


def _applescript_string(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def choose_folder(prompt: str, default: Path | None = None) -> Path | None:
    """Show the Finder "choose folder" dialog. Returns None if the user cancels."""
    if shutil.which("osascript") is None:
        raise RuntimeError("Folder dialog requires macOS; pass the folder path as an argument instead.")

    script = f"choose folder with prompt {_applescript_string(prompt)}"
    if default is not None and default.expanduser().is_dir():
        script += f" default location (POSIX file {_applescript_string(str(default.expanduser()))} as alias)"

    result = subprocess.run(
        ["osascript", "-e", f"POSIX path of ({script})"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        if USER_CANCELED in result.stderr:
            return None
        raise RuntimeError(result.stderr.strip())
    return Path(result.stdout.strip())


def choose_input_folder(default: Path | None = None) -> Path | None:
    return choose_folder("Choisis le dossier où tu as exporté tes pistes", default)


def choose_output_folder(default: Path | None = None) -> Path | None:
    return choose_folder("Choisis où ranger les mix", default)


if __name__ == "__main__":
    import sys

    kind = sys.argv[1] if len(sys.argv) > 1 else "input"
    picker = choose_output_folder if kind == "output" else choose_input_folder
    folder = picker(Path("~/Music"))
    if folder is None:
        print("canceled")
        sys.exit(1)
    print(folder)
