"""Tests for get_problem.py"""
import logging
from pathlib import Path
from unittest import mock

import pytest

from rosalind_problems.scripts import get_problem as script

FIXTURES = Path("tests/fixtures")

def function_get_relative_contents(path: Path) -> set[str]:
    """FUNCTION - Returns a set of all files in a directory relatively to the directory."""
    return set(
        map(
            lambda p: p.relative_to(path).as_posix(),
            path.rglob("*")
        )
    )


@pytest.fixture(autouse=True)
def _mock_get_problem_summary():
    """"""
    with mock.patch("rosalind_problems.scripts.get_problem.get.problem_summary") as mock_get_problem:
        mock_get_problem.return_value = {
        "as_markdown": (FIXTURES / "problem.md").read_text(),
        "sample_data": (FIXTURES / "sample_dataset.txt").read_text(),
        "sample_solution": (FIXTURES / "sample_solution.txt").read_text(),
    }
        yield mock_get_problem

def test_problem_export_summary():
    """TEST - Files are created in expected locatations with expected content."""      
    export_summary = script.get_problem(
        "mock_problem",
        Path(".")
    )
    
    expected_export_summary_params = [
        ("./src/rosalind_problems/problems/mock_problem/main.py", FIXTURES / "main.txt"),
          ("./src/rosalind_problems/problems/mock_problem/problem.md", FIXTURES / "problem.md"),
          ("./tests/test_problems/test_mock_problem/test_mock_problem.py", FIXTURES / "test.txt"),
        ("./tests/test_problems/test_mock_problem/fixtures/sample_solution.txt", FIXTURES / "sample_solution.txt"),
          ("./tests/test_problems/test_mock_problem/fixtures/sample_dataset.txt", FIXTURES / "sample_dataset.txt"),
    ]
    
    expected_export_summary = dict(map(lambda t: (Path(t[0]), t[1].read_text()), expected_export_summary_params))
        
    assert dict(expected_export_summary) == export_summary


def test_main(monkeypatch, tmp_path):
    """TEST - main generates expected files."""
    monkeypatch.setattr(script.static, "GIT_ROOT", tmp_path)
    
    expected_problem_dir = tmp_path / "src/rosalind_problems/problems/mock_problem/"
    expected_problem_files = {"main.py", "problem.md"}
    expected_testing_dir = tmp_path / "tests/test_problems/test_mock_problem/"
    expected_testing_files = {"test_mock_problem.py", "fixtures/sample_solution.txt", "fixtures/sample_dataset.txt"}
    
    
    script.main(["mock_problem"])
        
    actual_problem_files = function_get_relative_contents(path=expected_problem_dir) & expected_problem_files
    actual_testing_files = function_get_relative_contents(path=expected_testing_dir) & expected_testing_files
    
    assert expected_problem_files == actual_problem_files
    assert expected_testing_files == actual_testing_files


def test_main_skips_existing_file(monkeypatch, tmp_path, caplog):
    """FIXTURE - Script skips on user input if file exists."""
    monkeypatch.setattr(script.static, "GIT_ROOT", tmp_path)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    existing_file = tmp_path / "src/rosalind_problems/problems/mock_problem/main.py"
    existing_file.parent.mkdir(parents=True)
    existing_file.touch()
    
    with caplog.at_level(logging.INFO):
        script.main(["mock_problem"])
     
    assert "Skipping main.py" in caplog.text


def test_main_overwrites_existing_file(monkeypatch, tmp_path):
    """FIXTURE - Script overwrites file on user input if one already exists."""
    monkeypatch.setattr(script.static, "GIT_ROOT", tmp_path)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    existing_file = tmp_path / "src/rosalind_problems/problems/mock_problem/main.py"
    existing_file.parent.mkdir(parents=True)
    existing_file.touch()
            
    script.main(["mock_problem"])
     
    assert existing_file.stat().st_size != 0
