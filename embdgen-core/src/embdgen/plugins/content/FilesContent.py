from typing import List
from pathlib import Path

from embdgen.core.utils.class_factory import Config
from embdgen.core.content.BaseContent import BaseContent

@Config("files")
class FilesContent(BaseContent):
    """A list of files
    
    It is up to the including content module, to decide what happens with the files.
    """
    CONTENT_TYPE = "files"

    files: List[Path]
    """The list of files"""

    def __init__(self):
        super().__init__()
        self.files = []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(map(str, self.files))})"
