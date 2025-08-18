"""Solution for hamm Rosalind Problem."""
from itertools import starmap
from rosalind_problems.utils import run, cli 


def hamm(data_set: str) -> str:
    """Code to solve hamm."""
    sequences = data_set.strip().splitlines()
    same = filter(lambda t: t[0] != t[1], zip(*map(list, sequences)))
    return f"{len(list(same))}\n"

def main(argv: list[str] | None = None):
    """Queries Rosalind for hamm function and returns the result."""
    args = cli.GetCookies(
        description="Queries Rosalind for hamm's dataset and runs against the specified script. Automated scraping is against  Rosalind's TOS, so only run for personal use and sparingly."
    ).parse_args(argv)
    
    run.run_problem(func=hamm, **vars(args))
