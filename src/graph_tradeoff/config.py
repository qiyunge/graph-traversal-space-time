from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
CPP_EXE_DIR = BASE_DIR / "cpp"
DATASETS_DIR = BASE_DIR / "datasets"
RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)


