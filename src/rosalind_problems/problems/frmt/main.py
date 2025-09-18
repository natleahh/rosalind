"""Solution for frmt Rosalind Problem."""
from rosalind_problems.utils import run, cli, tools 
from Bio import Entrez, SeqIO


def frmt(data_set: str) -> str:
	"""Code to solve frmt."""
	Entrez.email = "a.l.tengbe@gmail.com" # tools.get_user_email()
	handle = Entrez.efetch(db="nucleotide", id=data_set.splitlines(), rettype="fasta")
	records = SeqIO.parse(handle=handle, format="fasta")
	shortest = min(records, key=lambda r: len(r.seq))
	solution = shortest
	return solution.format("fasta")

def main(argv: list[str] | None = None):
	"""Queries Rosalind for frmt function and returns the result."""
	args = cli.GetCookies(
		description="Queries Rosalind for frmt's dataset and runs against the specified script. Automated scraping is against  Rosalind's TOS, so only run for personal use and sparingly."
	).parse_args(argv)
	
	run.run_problem(func=frmt, **vars(args))
