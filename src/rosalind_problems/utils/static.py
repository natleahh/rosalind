"""Module defining static values."""

from pathlib import Path

import git


BASE_URL = "https://rosalind.info"
TEMPLATES = Path("src/rosalind_problems/templates")
GIT_ROOT = Path(git.Repo(__file__, search_parent_directories=True).git.rev_parse("--show-toplevel"))