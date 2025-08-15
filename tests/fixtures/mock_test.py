"""Tests for mock_problem."""

from pathlib import Path
from src.problems.mock_problem.main import mock_problem as func


FIXTURES = Path("~/tests/test_problems/test_mock_problem/fixtures")

def test_mock_problem():
    """"""
    expected_data = (FIXTURES / "solution_data.txt").read_text()
    actual_data = func((FIXTURES / "sample_data.txt").read_text())

    assert expected_data == actual_data
