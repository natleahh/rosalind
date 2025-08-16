""""""

import argparse

from rosalind_problems.utils import get


class GetCookies(argparse.ArgumentParser):
    """"""
    
    def __init__(self, *args, **kwargs):
        """"""
        self.add_argument(
            "--session_id",
            help=f"A {get.BASE_URL} session ID retreived from the dev view of the website."
        )
        
        self.add_argument(
            "--token",
            help=f"A {get.BASE_URL} csrf token retreived from the dev view of the website."
        )
