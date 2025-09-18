"""Tests for perm."""
from pathlib import Path
from rosalind_problems.problems.perm import main
from rosalind_problems.utils import testing_utils

FIXTURES = Path("tests/test_problems/test_perm/fixtures")

def test_perm():
	"""TEST - main function of perm solved the sample problem."""
	sample_dataset, sample_solution = testing_utils.get_samples(FIXTURES)
	assert main.perm(sample_dataset) == sample_solution