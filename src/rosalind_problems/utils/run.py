import sys
from rosalind_problems.utils import get, annotations

def run_problem(func: annotations.ProblemFunc, session_id: str, token: str) -> None:
    """"""
    data_set = get.data_set(
        problem_id=func.__name__,
        session_id=session_id,
        token=token,
    )
    
    sys.stdout.write(func(data_set=data_set))
