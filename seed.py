"""
Convenience entry point for database seeding.
Delegates directly to scripts/seed_db.py.
"""
import sys
from pathlib import Path

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.seed_db import clean_and_seed

if __name__ == "__main__":
    clean_and_seed()
