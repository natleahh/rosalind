"""Solution for perm Rosalind Problem."""
from itertools import permutations
from rosalind_problems.utils import run, cli 


def perm(data_set: str) -> str:
	"""Code to solve perm."""
	i = int(data_set.strip())
	ps = [" ".join(map("{}".format, p)) for p in permutations(range(1, i + 1))]
	return "\n".join([str(len(ps)), *ps]) + "\n"

def main(argv: list[str] | None = None):
	"""Queries Rosalind for perm function and returns the result."""
	args = cli.GetCookies(
		description="Queries Rosalind for perm's dataset and runs against the specified script. Automated scraping is against  Rosalind's TOS, so only run for personal use and sparingly."
	).parse_args(argv)
	
	run.run_problem(func=perm, **vars(args))
