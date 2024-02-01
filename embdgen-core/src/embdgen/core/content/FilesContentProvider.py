# SPDX-License-Identifier: GPL-3.0-only

import abc
from typing import List
from pathlib import Path

from .BaseContent import BaseContent

class FilesContentProvider(BaseContent, abc.ABC):
    """Base class for all content providers, that provide a list of files
    """

    @property
    @abc.abstractmethod
    def files(self) -> List[Path]:
        pass
