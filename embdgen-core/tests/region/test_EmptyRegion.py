from io import BytesIO
from embdgen.plugins.region.EmptyRegion import EmptyRegion

class TestEmptyRegion:
    def test_simple(self):
        obj = EmptyRegion()
        obj.prepare()
        assert obj.size.is_undefined
        assert obj.start.is_undefined

        out_file = BytesIO()
        obj.write(out_file)
        assert out_file.tell() == 0
