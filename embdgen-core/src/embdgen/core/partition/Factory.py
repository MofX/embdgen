from embdgen.plugins import partition

from ..utils.class_factory import FactoryBase
from . import BasePartition

class Factory(FactoryBase[BasePartition]):
    @classmethod
    def load(cls):
        return cls.load_plugins(partition, BasePartition, 'PART_TYPE')
