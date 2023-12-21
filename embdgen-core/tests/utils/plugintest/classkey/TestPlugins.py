from typing import List

from . import BaseTestPlugin

class CustomClass:
    pass

class CustomSubClass1(CustomClass):
    pass

class CustomSubClass2(CustomClass):
    pass

class CustomSubClass3(CustomClass):
    pass

class TestPlugin1(BaseTestPlugin):
    TEST_CLASS_TYPE = str

class TestPlugin2(BaseTestPlugin):
    TEST_CLASS_TYPE = List[int]

class TestPlugin3(BaseTestPlugin):
    TEST_CLASS_TYPE = CustomClass

class TestPlugin4(TestPlugin3):
    TEST_CLASS_TYPE = CustomSubClass1

class TestPlugin5(TestPlugin3):
    TEST_CLASS_TYPE = CustomSubClass2
