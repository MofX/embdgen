from io import BytesIO
from embdgen.plugins.partition.EmptyPartition import EmptyPartition

class TestEmptyPartition:
    def test_simple(self):
        obj = EmptyPartition()
        obj.prepare()
        assert obj.size.is_undefined
        assert obj.start.is_undefined

        out_file = BytesIO()
        obj.write(out_file)
        assert out_file.tell() == 0
