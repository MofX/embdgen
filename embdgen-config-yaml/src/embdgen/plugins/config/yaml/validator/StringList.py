from typing import List

import strictyaml as y

from .ListBase import ListBase

class StringList(ListBase):
    RESULT_TYPE = List[str]

    def __init__(self):
        super().__init__(y.Str())
