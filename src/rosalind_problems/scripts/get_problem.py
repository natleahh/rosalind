""""""

import argparse
import logging
from pathlib import Path

from src.rosalind_problems.utils import get

TEMPLATES = Path("src/rosalind_problems/templates")

logger = logging.getLogger(name=__name__)

def get_command_line_arguments(argv: list[str] | None = None):

    parser = argparse.ArgumentParser(
        prog="get_problem",
        description=f"Retreived problem from {get.BASE_URL} and populates problem "\
                     "directory as well as tests, test cases."
    )
    parser.add_argument(
        "name",
        metavar="problem_name",
        type=str,
        help=f"Problem ID as presented in {get.BASE_URL}/problems/list-view",
    )

    return parser.parse_args(argv)

def get_problem(problem_id: str, source_dir: Path):
    """"""
    
    problem_summary = get.problem(problem_id=problem_id)
    problem_dir = source_dir / f"src/rosalind_problems/problems/{problem_id}"
    test_dir = source_dir / f"tests/test_problems/test_{problem_id}"
    
    export_summary = {
        problem_dir / "main.py" : (TEMPLATES / "main.py").read_text().format(problem_id=problem_id),
        problem_dir / "problem.md": problem_summary["as_markdown"],
        test_dir / f"test_{problem_id}.py": (TEMPLATES / "test.py").read_text().format(problem_id=problem_id),
        test_dir / f"fixtures/sample_solution.txt": problem_summary["sample_solution"],
        test_dir / f"fixtures/sample_dataset.txt": problem_summary["sample_data"]
    }
    return export_summary


def main(argv: list[str] | None = None):
    args = get_command_line_arguments(argv=argv)
    export_summary = get_problem(**vars(args))
    # check for exiting files
    for path, content in export_summary.items():
        user_prompt = f"{path.name} already exists at {path.parent}. Overwrite?: "
        if path.exists() and not (input(user_prompt).lower() in ["y", "yes"]):
            logger.info(f"Skipping {path.name}")
            continue
        path.write_text(content)
        
if __name__ == "__main__":
    main()
