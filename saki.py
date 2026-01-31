#!/usr/bin/env python3
"""
Saki - The Agent Skill Installer
================================
Refactored Entry Point
"""
import sys
from pathlib import Path

# Add src to python path so we can import 'saki' package
# assuming saki.py is at root and src/saki is inside
ROOT = Path(__file__).parent / "src"
sys.path.insert(0, str(ROOT))

if __name__ == "__main__":
    from saki.cli import main
    main()
