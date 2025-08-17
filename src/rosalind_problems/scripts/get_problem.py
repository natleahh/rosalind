"""Script for retreiving problems from Rosalind."""
import logging
from pathlib import Path

from rosalind_problems.utils import get, cli, static

logger = logging.getLogger(name=__name__)


def get_problem(problem_id: str, source_dir: Path | None = None) -> dict[Path, str]:
    """Retreived problem from Rosalind and returns a project summary.

    Args:
        problem_id (str): Problem ID as shows in Rosalind.
        source_dir (Path | None): Path to create files.
    """
    problem_summary = get.problem_summary(problem_id=problem_id)
    # Get Git Repo root if no path is provided
    source_dir = source_dir or static.GIT_ROOT
    
    # Generate export summary
    problem_dir = source_dir / f"src/rosalind_problems/problems/{problem_id}"
    test_dir = source_dir / f"tests/test_problems/test_{problem_id}"
    
    export_summary = {
        problem_dir / "main.py" : (static.TEMPLATES / "main.py").read_text().format(problem_id=problem_id),
        problem_dir / "problem.md": problem_summary["as_markdown"],
        test_dir / f"test_{problem_id}.py": (static.TEMPLATES / "test.py").read_text().format(problem_id=problem_id),
        test_dir / f"fixtures/sample_solution.txt": problem_summary["sample_solution"],
        test_dir / f"fixtures/sample_dataset.txt": problem_summary["sample_data"]
    }
    return export_summary


def main(argv: list[str] | None = None):
    """Main function body of get_problem."""
    parser = cli.GetProblem(
        prog="get_problem",
        description=f"Retreived problem from {static.BASE_URL} and populates problem "\
                     "directory as well as tests, test cases."
    )
   
    # get problem
    export_summary = get_problem(**vars(parser.parse_args(argv)))
    
    # check for exiting files
    for path, content in export_summary.items():
        user_prompt = f"{path.name} already exists at {path.parent}. Overwrite?: "
        if path.exists() and not (input(user_prompt).lower() in ["y", "yes"]):
            logger.info(f"Skipping {path.name}")
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        
if __name__ == "__main__":
    main()
