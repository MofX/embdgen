# SPDX-License-Identifier: GPL-3.0-only

import abc
from typing import List

from ..utils.class_factory import Config
from ..region import BaseRegion

@Config('parts')
class BaseLabel(abc.ABC):
    """Base class for labels (i.e. partition types, e.g. MBR or GPT)"""

    parts: List[BaseRegion]
    """List of regions to be included in the image"""

    def __init__(self):
        self.parts = []

    @abc.abstractmethod
    def prepare(self):
        pass

    @abc.abstractmethod
    def create(self, filename: str):
        pass
