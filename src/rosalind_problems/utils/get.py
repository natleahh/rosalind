"""Module for accessing data from Rosalind."""
import logging
import re
import requests
import bs4
import html_to_markdown as h2m

from rosalind_problems.utils import static, annotations

BASE_FORMAT = "{host}/{path}".format(host=static.BASE_URL, path="{path}")
PROBLEM_FORMAT = BASE_FORMAT.format(
    path="problems/{problem_id}"
)
DATASET_FORMAT = BASE_FORMAT.format(
    path="problems/{problem_id}/dataset"
)

logger = logging.getLogger(__name__)

def data_set(problem_id: str, session_id: str, token: str) -> str:
    """Retreived a the dataset of a problem from Rosalind.info."""
    logger.info("Requesting test data from Rosalind.")
    cookies = {
        "sessionid": session_id,
        "csrftoken": token
    }
    url = DATASET_FORMAT.format(problem_id=problem_id)
    logger.debug(url)
    with requests.get(url, cookies=cookies) as response:
        response.raise_for_status()

    return response.text

def _format_markdown(markdown: str):
    """Makes small changes to correctly format markdown summary."""
    # Make urls absolute
    markdown = re.sub(r"\((\/[\w\d]+[\/|(?\.\w+)]+)\)", fr"({static.BASE_URL}\1)", markdown)
    return markdown

def problem_summary(problem_id: str) -> annotations.ProblemSummary:
    """Retreives a problem summary from Rosalind.info.

    Args:
        problem_id: Rosalind Problem ID.
    """
    problem_url = PROBLEM_FORMAT.format(problem_id=problem_id)
    with requests.get(problem_url) as response:
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, features="html.parser")

    problem_source = soup.find("div", {"class": "problem-statement problem-statement-bordered"})
    markdown = h2m.convert_to_markdown(str(problem_source))
    *head, sample_data_set, sample_solution = problem_source.find_all("pre")

    if head:
        logger.warning(f"Problem ({problem_url}) url has more than 2 code blocks. Check the results as the source.")

    return {
        "as_markdown": _format_markdown(markdown),
        "sample_data": sample_data_set.text,
        "sample_solution": sample_solution.text
    }
