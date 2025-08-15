import typing

class ProblemSummary(typing.TypedDict):
    """Summary of a Rosalind.info problem."""
    as_markdown: str
    sample_data: str
    sample_solution: str
