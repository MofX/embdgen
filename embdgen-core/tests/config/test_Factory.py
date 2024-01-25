# SPDX-License-Identifier: GPL-3.0-only

from  embdgen.core.config.Factory import Factory

def test_factory():
    assert isinstance(Factory().types(), list)
