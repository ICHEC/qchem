import os
from typing import List

def available_molecules(path) -> List[str]:
    """
    Returns a list of the molecules in the directory given by the path.
    Assumes the files are '.xyz'.
    """
    return [i.split(".")[0] for i in os.listdir(path)]


def load_molecule(formula: str, path: str = None) -> str:
    """Loads a molecule from the 'default_molecules' directory or directory given by the path."""
    if not path:
        path = "%s/default_molecules" % os.path.dirname(__file__)

    try:
        with open("%s/%s.xyz" % (path, formula), 'r') as file:
            data = file.read()
    except FileNotFoundError:
        raise Exception("Molecule '%s' is not in '%s'" % (formula, path))
    return data
