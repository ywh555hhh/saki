
from pathlib import Path

# --- Constants ---
ROOT_DIR = Path(__file__).resolve().parent.parent.parent # src/saki/config.py -> src/saki -> src -> root
SKILL_SOURCE_DIR = ROOT_DIR / "skills" / "saki"
SKILL_DEST_NAME = "saki"

# Tools configuration has been moved to src/saki/core/config_manager.py
# Default: ~/.saki/config.yaml
