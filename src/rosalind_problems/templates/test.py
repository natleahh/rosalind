"""Tests for {problem_id}."""
from rosalind_problems.problems.{problem_id} import main
from rosalind_problems.utils.testing_utils

FIXTURES = Path("tests/test_problems/test_{problem_id}/fixtures")

def test_{problem_id}():
	"""TEST - main function of {problem_id} solved the sample problem."""
	sample_dataset, sample_solution = testing_utils.get_samples(FIXTURES)
	assert main.{problem_id}(sample_dataset) == sample_solution