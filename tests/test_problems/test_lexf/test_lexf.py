"""Tests for lexf."""
from pathlib import Path
from rosalind_problems.problems.lexf import main
from rosalind_problems.utils import testing_utils

FIXTURES = Path("tests/test_problems/test_lexf/fixtures")

def test_lexf():
	"""TEST - main function of lexf solved the sample problem."""
	sample_dataset, sample_solution = testing_utils.get_samples(FIXTURES)
	assert main.lexf(sample_dataset) == sample_solution