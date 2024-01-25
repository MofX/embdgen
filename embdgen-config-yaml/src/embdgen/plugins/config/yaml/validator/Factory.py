# SPDX-License-Identifier: GPL-3.0-only

import strictyaml as y

from embdgen.core.utils.class_factory import FactoryBase

from .. import validator

class Factory(FactoryBase[y.Validator]):
    ALLOW_SUBCLASS = True

    @classmethod
    def load(cls):
        return cls.load_plugins(validator, y.Validator, 'RESULT_TYPE')
