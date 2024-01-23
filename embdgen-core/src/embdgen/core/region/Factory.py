from embdgen.plugins import region

from ..utils.class_factory import FactoryBase
from . import BaseRegion

class Factory(FactoryBase[BaseRegion]):
    @classmethod
    def load(cls):
        return cls.load_plugins(region, BaseRegion, 'PART_TYPE')
