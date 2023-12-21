from  embdgen.core.label import Factory

def test_factory():
    f_types = Factory().types()
    assert 'mbr' in f_types
