from  embdgen.core.region import Factory

def test_factory():
    f_types = Factory().types()
    assert 'empty' in f_types
    assert 'partition' in f_types
    assert 'raw' in f_types
