"""Tests for get_problem.py"""
from pathlib import Path
from unittest import mock

import pytest
from src.rosalind_problems.scripts import get_problem as script

FIXTURES = Path("~tests/test_utils/fixtures")

@pytest.fixture(autouse=True)
def _mock_rosalind():
    """Mocks rosalind problem."""
    mock.Mock(script.get.problem, FIXTURES / "problem.md")

def test_problem_summary_is_generated(tmp_path):
    """TEST - Files are created in expected locatations with expected content."""
    # Set Up
    expected_problem_content = (FIXTURES / "problem.md").read_text()
    expected_main_content = (FIXTURES / "main.py").read_text()
    expected_test_content = (FIXTURES / "mock_test.py").read_text()
    expected_data_set_content = (FIXTURES / "sample_data.txt").read_text()
    expected_solution_content = (FIXTURES / "sample_solution.txt").read_text()

    problem_name = "mock_problem"
    actual_problem_file = tmp_path / f"src/problem/{problem_name}.md"
    actual_main_file = tmp_path / f"src/problem/main.py"
    actual_test_file = tmp_path / f"test/test_{problem_name}.py"
    actual_test_data_set = tmp_path / f"test/test_{problem_name}_sample_dataset.txt"
    actual_test_solution = tmp_path / f"test/test_{problem_name}_sample_solution.txt"


    # Excercise
    script.get_problem(problem_name=problem_name, source_dir=tmp_path)

    # Verify
    assert actual_problem_file.read_text() == expected_problem_content
    assert actual_main_file.read_text() == expected_main_content
    assert actual_test_file.read_text() == expected_test_content
    assert actual_test_data_set.read_text() == expected_data_set_content
    assert actual_test_solution.read_text() == expected_solution_content




def test_main():
    """TEST - Command line interface works as expected"""
    script.main(["mock_name"])
