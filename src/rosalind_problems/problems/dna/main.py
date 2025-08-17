"""Solution for dna Rosalind Problem."""
import collections
from rosalind_problems.utils import run, cli 


def dna(data_set: str) -> str:
    """Code to solve dna."""
    counter = collections.Counter(data_set.strip())
    counts = list(zip(*sorted(counter.items())))[1]
    strings = map("{}".format, counts)
    return f"{' '.join(strings)}\n"

def main(argv: list[str] | None = None):
    """Queries Rosalind for dna function and returns the result."""
    args = cli.GetCookies(
        description="Queries Rosalind for dna's dataset and runs against the specified script. Automated scraping is against  Rosalind's TOS, so only run for personal use and sparingly."
    ).parse_args(argv)
    
    run.run_problem(func=dna, **vars(args))
