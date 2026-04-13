from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)


