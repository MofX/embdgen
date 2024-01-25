# SPDX-License-Identifier: GPL-3.0-only

from embdgen.core.content import BaseContent, Factory

from .ObjectBase import ObjectBase

class Content(ObjectBase):
    RESULT_TYPE = BaseContent
    FACTORY = Factory
