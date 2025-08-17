"""Solution for rna Rosalind Problem."""
from rosalind_problems.utils import run, cli 


def rna(data_set: str) -> str:
    """Code to solve rna."""
    return data_set.replace("T", "U")

def main(argv: list[str] | None = None):
    """Queries Rosalind for rna function and returns the result."""
    args = cli.GetCookies(
        description="Queries Rosalind for rna's dataset and runs against the specified script. Automated scraping is against  Rosalind's TOS, so only run for personal use and sparingly."
    ).parse_args(argv)
    
    run.run_problem(func=rna, **vars(args))
