"""Modues with command line interface utlities."""
import argparse
from rosalind_problems.utils import static

class GetCookies(argparse.ArgumentParser):
    """Command line Parser for getting browser informations."""
    
    def __init__(self, *args, **kwargs):
        """Initalises GetCookies."""
        super().__init__(*args, **kwargs)
        self.add_argument(
			"--session_id",
			help=f"Session ID from {static.BASE_URL}. After logging in can be retreived from the Cookies view of you browser's dev mode."
		)
        self.add_argument(
			"--session_id",
			help=f"Session ID from {static.BASE_URL}. After logging in can be retreived from the Cookies view of you browser's dev mode."
		)
        
class GetProblem(argparse.ArgumentParser):
    """Command line parser for getting problem name."""
    
    def __init__(self, *args, **kwargs):
        """Initliases GetProblem."""
        super().__init__(*args, **kwargs)
        self.add_argument(
			"problem_id",
			type=str,
			help=f"Problem ID as presented in {static.BASE_URL}/problems/list-view",
		)

class GetLogging(argparse.ArgumentParser):
    """Command line parser for getting log level."""
    
    def __init__(self, *args, **kwargs):
        """Initialises GetLogging."""
        super().__init__(*args, **kwargs)
        self.add_argument(
			"-v",
			"--verbose",
			action="count",
			default=0,
			help="Set logging level. Provide -v up to 3 times for incresed versbosity."
		)