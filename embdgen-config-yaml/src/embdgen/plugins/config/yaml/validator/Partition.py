from typing import List

from embdgen.core.partition import BasePartition, Factory

from .ListBase import ListBase
from .ObjectBase import ObjectBase

class Partition(ObjectBase):
    RESULT_TYPE = BasePartition
    FACTORY = Factory

class PartitionList(ListBase):
    RESULT_TYPE = List[BasePartition]

    def __init__(self):
        super().__init__(Partition())
