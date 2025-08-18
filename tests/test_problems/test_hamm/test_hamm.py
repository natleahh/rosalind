"""Tests for hamm."""
from pathlib import Path
from rosalind_problems.problems.hamm import main
from rosalind_problems.utils import testing_utils

FIXTURES = Path("tests/test_problems/test_hamm/fixtures")

def test_hamm():
	"""TEST - main function of hamm solved the sample problem."""
	sample_dataset, sample_solution = testing_utils.get_samples(FIXTURES)
	assert main.hamm(sample_dataset) == sample_solution