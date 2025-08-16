"""Tests for utils related to running rosalin problems."""
from unittest import mock
from rosalind_problems.utils import run

def function_mock_problem(data_set: str):
    """FUNCTION - Mock problem function."""
    return "The Result!"

def test_run_problems_reports_result_to_std_out(capsys):
    """Run problem exports solution to stdout."""
    mock.Mock(run.get.data_set).return_value("")

    run.run_problem(
        func=function_mock_problem,
        session_id="",
        token="",
    )
    assert capsys.readouterr().out == "The Result!"
