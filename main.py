"""Publish the bundled world-news image to the make.fun output directory."""

import os
import shutil
from pathlib import Path


def main() -> None:
    """Copy the entry image to the configured output directory."""
    script_dir = Path(__file__).resolve().parent
    # Fall back to the grader's standard output path when no override is set.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(script_dir / "entry.png", output_dir / "entry.png")


if __name__ == "__main__":
    main()
