#!/usr/bin/env python3
from __future__ import annotations

import platform
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SPEC_FILE = ROOT / "mine_pdf.spec"


def main() -> int:
    if not SPEC_FILE.exists():
        print(f"Missing spec file: {SPEC_FILE}", file=sys.stderr)
        return 1

    os_name = platform.system().lower()
    if os_name not in {"windows", "darwin", "linux"}:
        print(f"Unsupported OS: {platform.system()}", file=sys.stderr)
        return 1

    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        str(SPEC_FILE),
    ]
    print("Running:", " ".join(cmd))

    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        print("PyInstaller is not installed in this environment.", file=sys.stderr)
        return 1
    except subprocess.CalledProcessError as exc:
        return exc.returncode

    dist_dir = ROOT / "dist" / "mine_pdf"
    exe_name = "mine_pdf.exe" if os_name == "windows" else "mine_pdf"
    print("Build complete.")
    print("Output:", dist_dir / exe_name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
