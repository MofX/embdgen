import pathlib
from typing import List
import strictyaml as y
from  strictyaml.parser import YAMLChunk

from .ListBase import ListBase

class Path(y.Str):
    RESULT_TYPE = pathlib.Path

    def validate_scalar(self, chunk: YAMLChunk) -> pathlib.Path:
        return pathlib.Path(super().validate_scalar(chunk))

class PathList(ListBase):
    RESULT_TYPE = List[pathlib.Path]

    def __init__(self):
        super().__init__(Path())
