"""Solution for gc Rosalind Problem."""
from rosalind_problems.problems.dna.main import dna
from rosalind_problems.utils import run, cli 


def gc_content(seqences: list[str]):
    """"""
    _, *gc_counts, _ = full_counts = list(map(int, dna("".join(seqences)).strip().split(" ")))
    return sum(gc_counts) / sum(full_counts) * 100


def gc(data_set: str) -> str:
    """Code to solve gc."""
    # get fastas
    fastas = data_set.split("\n>")

    # for each get gc content
    result = []

    for fasta in fastas:
        print(fasta)
        header, *sequence = fasta.strip().split("\n")
        result.append((header, gc_content(sequence)))
    
    # select highest
    highest = max(result, key=lambda t: t[1])
    print(highest)

    return "{}\n{:.6f}\n".format(*highest)

def main(argv: list[str] | None = None):
    """Queries Rosalind for gc function and returns the result."""
    args = cli.GetCookies(
        description="Queries Rosalind for gc's dataset and runs against the specified script. Automated scraping is against  Rosalind's TOS, so only run for personal use and sparingly."
    ).parse_args(argv)
    
    run.run_problem(func=gc, **vars(args))
