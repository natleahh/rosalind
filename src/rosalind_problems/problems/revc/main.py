"""Solution for revc Rosalind Problem."""
from rosalind_problems.utils import run, cli 

REVC_PAIRS = [
    ("A", "T"),
    ("G", "C")
]

COMPLEMNT = dict((*REVC_PAIRS, *map(reversed, REVC_PAIRS)))

def revc(data_set: str) -> str:
    """Code to solve revc."""
    complemenary = list(map(COMPLEMNT.get, data_set.strip()))
    solution = "".join(reversed(complemenary))
    return solution + "\n"

def main(argv: list[str] | None = None):
    """Queries Rosalind for revc function and returns the result."""
    args = cli.GetCookies(
        description="Queries Rosalind for revc's dataset and runs against the specified script. Automated scraping is against  Rosalind's TOS, so only run for personal use and sparingly."
    ).parse_args(argv)
    
    run.run_problem(func=revc, **vars(args))
