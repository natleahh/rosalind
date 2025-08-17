"""Modules with utilities for testing."""
from pathlib import Path


def get_samples(path: Path) -> tuple[str, str]:
    """Gets sample dataset and solution from provided mock."""
    return (
        (path / "sample_dataset.txt").read_text(),
        (path / "sample_solution.txt").read_text()
	)
