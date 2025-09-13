"""Solution for gbk Rosalind Problem."""
from rosalind_problems.utils import run, cli
from Bio import Entrez as entrez


def gbk(data_set: str) -> str:
	"""Code to solve gbk."""
	entrez.email = input("Email: ")
	organism, min_date, max_date = data_set.splitlines()
	handle = entrez.esearch(db="nucleotide", term=f"{organism}[Organism] AND ({min_date}[PDAT] : {max_date}[PDAT])")
	record = entrez.read(handle)
	solution = record["Count"]
	return solution

def main(argv: list[str] | None = None):
	"""Queries Rosalind for gbk function and returns the result."""
	args = cli.GetCookies(
		description="Queries Rosalind for gbk's dataset and runs against the specified script. Automated scraping is against  Rosalind's TOS, so only run for personal use and sparingly."
	).parse_args(argv)
	
	run.run_problem(func=gbk, **vars(args))
