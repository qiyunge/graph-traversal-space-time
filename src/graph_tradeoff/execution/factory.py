from .types import Backend, ExecutionResult
from graph_tradeoff.data.dataset_manager import DatasetManager
from .python_executor import run_python_executor
from .cpp_executor import run_cpp_executor

from .types import ExecutionSpec
from typing import Callable


def get_executor(backend: str |Backend) -> Callable[[ExecutionSpec, DatasetManager], ExecutionResult]:
    backend = Backend(backend) if isinstance(backend, str) else backend
    if backend == Backend.PYTHON:
        return run_python_executor
    elif backend == Backend.CPP:
        return run_cpp_executor
    else:
        raise ValueError(f"Unsupported backend: {backend}")