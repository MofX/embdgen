from typing import Sequence
from .CLI import CLI

def cli(args: Sequence[str] = None):
    CLI().run(args)
