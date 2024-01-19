from io import BytesIO
from pathlib import Path

from embdgen.core.utils.SizeType import SizeType
from embdgen.plugins.region.RawRegion import RawRegion
from embdgen.plugins.content.RawContent import RawContent

class TestEmptyRegion:
    def test_simple(self, tmp_path: Path):
        input = tmp_path / "input"
        input.write_bytes(b"".join([i.to_bytes(1, 'little') for i in range(256)]))
        obj = RawRegion()
        obj.content = RawContent()
        obj.content.file = input

        obj.start = SizeType(32)
        obj.prepare()
        assert obj.size.bytes == 256


        out_file = BytesIO()
        obj.write(out_file)
        assert out_file.tell() == 256 + 32

        assert out_file.getbuffer()[32:] == input.read_bytes()
