"""Tests for revc."""
from pathlib import Path
from rosalind_problems.problems.revc import main
from rosalind_problems.utils import testing_utils

FIXTURES = Path("tests/test_problems/test_revc/fixtures")

def test_revc():
	"""TEST - main function of revc solved the sample problem."""
	sample_dataset, sample_solution = testing_utils.get_samples(FIXTURES)
	assert main.revc(sample_dataset) == sample_solution