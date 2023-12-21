from embdgen.plugins import content

from ..utils.class_factory import FactoryBase
from . import BaseContent

class Factory(FactoryBase[BaseContent]):
    """
    Factory class for content
    """

    @classmethod
    def load(cls):
        return cls.load_plugins(content, BaseContent, 'CONTENT_TYPE')
