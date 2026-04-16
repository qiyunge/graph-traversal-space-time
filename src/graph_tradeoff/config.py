from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
CPP_EXE_DIR = BASE_DIR / "cpp"
RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)


