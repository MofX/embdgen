from embdgen.core.label import BaseLabel, Factory

from .ObjectBase import ObjectBase

class Label(ObjectBase):
    RESULT_TYPE = BaseLabel
    FACTORY = Factory
