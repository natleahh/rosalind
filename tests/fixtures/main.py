"""Solution for mock_problem Rosalind Problem."""
from pathlib import Path
from src.utils.run import run_problem


def mock_problem(source_data: str) -> str:
    """Code to solve mock_problem."""
    return source_data

def main():
    """Queries Rosalind for mock_problem function and returns the result."""
    run_problem(mock_problem)
