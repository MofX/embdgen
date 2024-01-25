# SPDX-License-Identifier: GPL-3.0-only

from typing import List

from embdgen.core.region import BaseRegion, Factory

from .ListBase import ListBase
from .ObjectBase import ObjectBase

class Region(ObjectBase):
    RESULT_TYPE = BaseRegion
    FACTORY = Factory

class RegionList(ListBase):
    RESULT_TYPE = List[BaseRegion]

    def __init__(self):
        super().__init__(Region())
