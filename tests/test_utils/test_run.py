"""Tests for utils related to running rosalin problems."""
from unittest import mock
from src.rosalind_problems.utils import run


def test_run_problems_reports_result_to_std_out(capsys):
    """Run problem exports solution to stdout."""
    mock.Mock(run.get.data_set).return_value((None, None))

    run.run_problem(lambda _: "The Result!")

    assert capsys.readouterr().out == "The Result!"
