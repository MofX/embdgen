from  embdgen.core.partition import Factory

def test_factory():
    f_types = Factory().types()
    assert 'empty' in f_types
    assert 'ext4' in f_types
    assert 'fat32' in f_types
    assert 'raw' in f_types
