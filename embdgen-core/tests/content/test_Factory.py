from  embdgen.core.content import Factory

def test_factory():
    f_types = Factory().types()
    assert 'files' in f_types
    assert 'raw' in f_types
    assert 'verity' in f_types
