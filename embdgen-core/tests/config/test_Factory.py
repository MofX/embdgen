from  embdgen.core.config.Factory import Factory

def test_factory():
    assert isinstance(Factory().types(), list)
