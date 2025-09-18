"""Solution for lexf Rosalind Problem."""
from itertools import product
from rosalind_problems.utils import run, cli, tools


def lexf(data_set: str) -> str:
	"""Code to solve lexf."""
	s, t = tools.apply_types((str, int), data_set.splitlines())
	enumerations = sorted(product(*[s.split(" ")] * t))
	return "\n".join(map("".join, enumerations)) + "\n"


def main(argv: list[str] | None = None):
	"""Queries Rosalind for lexf function and returns the result."""
	args = cli.GetCookies(
		description="Queries Rosalind for lexf's dataset and runs against the specified script. Automated scraping is against  Rosalind's TOS, so only run for personal use and sparingly."
	).parse_args(argv)
	
	run.run_problem(func=lexf, **vars(args))
