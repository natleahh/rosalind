import typing

class ProblemSummary(typing.TypedDict):
    """Summary of a Rosalind.info problem."""
    as_markdown: str
    sample_data: str
    sample_solution: str

class ProblemFunc(typing.Protocol):
    """A function that solves a Rosalind problem."""
    def __call__(self, data_set: str) -> str:
        ...
