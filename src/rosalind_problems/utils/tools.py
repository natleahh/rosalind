""""""

import getpass
import os

from Bio import Entrez, SeqIO


def apply_types(types: tuple[type], raw_data: tuple[str]):
    """"""
    return tuple(t(d) for t, d in zip(types, raw_data))

def join_lines(xs: list):
    """"""
    return "\n".join(map(str, xs))

def get_env_variable(name: str, prompt: bool = False, secret: bool = False):
    """"""
    if name in os.environ:
        return os.environ[name]
    elif prompt:
        prompter = getpass.getpass if secret else input
        return prompter(f"{name}: ")
    else:
        raise KeyError(f"No variable '{name}' has been set.")


def get_fastas(*ids: str):
    """"""
    Entrez.email = get_env_variable("EMAIL")
    handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
    return [*SeqIO.parse(handle=handle, format="fasta")]


