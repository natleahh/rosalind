"""Tests for interface functions for Rosalind.info."""
from pathlib import Path
from unittest import mock

import pytest
from rosalind_problems.utils import get

FIXTURES = Path("tests/fixtures/")

@pytest.fixture()
def mock_reponse():
    """FIXTURE - Mocks Rosalind.info."""
    with mock.patch("requests.get") as mock_get:
        mock_get.return_value.raise_for_status = lambda _: None
        yield mock_get


def test_data_set(requests_mock):
    """TEST - get.data_set retreives expected input and actual data from Rosalind problem."""
    requests_mock.get(get.BASE_FORMAT.format("problem/mock_problem/dataset"), text="Input")
    assert get.data_set("mock_problem", "123", "456") == "Input"

def test_problem(mock_reponse):
    """Test - Get problem retreieves expected markdown from Rosalind problem."""
    mock_reponse.return_value.text = (FIXTURES / "mock_problem.html").read_text()
    expected_summary = {
        "as_markdown": (FIXTURES / "problem.md").read_text(),
        "sample_data": (FIXTURES / "sample_dataset.txt").read_text(),
        "sample_solution": (FIXTURES / "sample_solution.txt").read_text()
    }
    assert get.problem("mock_problem") == expected_summary
