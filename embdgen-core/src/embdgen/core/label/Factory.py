# SPDX-License-Identifier: GPL-3.0-only

from embdgen.plugins import label

from ..utils.class_factory import FactoryBase
from . import BaseLabel

class Factory(FactoryBase[BaseLabel]):
    """
    Factory class for label classes
    """

    @classmethod
    def load(cls):
        return cls.load_plugins(label, BaseLabel, 'LABEL_TYPE')
