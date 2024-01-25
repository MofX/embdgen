# SPDX-License-Identifier: GPL-3.0-only

from . import BaseTestPlugin


class TestPluginNotDiscoverable1(BaseTestPlugin):
    pass

class TestPluginNotDiscoverable2():
    TEST_TYPE = "I am not invalid"


class TestPlugin1(BaseTestPlugin):
    TEST_TYPE = "plugin1"

class TestPlugin2(BaseTestPlugin):
    TEST_TYPE = "plugin2"


class TestPlugin3(TestPlugin1):
    TEST_TYPE = "plugin3"

class TestPlugin4(TestPlugin1):
    TEST_TYPE = "plugin4"
