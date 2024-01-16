from io import BytesIO
from pathlib import Path

from embdgen.core.utils.SizeType import SizeType
from embdgen.plugins.partition.PartitionPartition import PartitionPartition
from embdgen.plugins.content.RawContent import RawContent

class TestPartitionPartition:
    def test_raw(self, tmp_path: Path):
        """
        At the moment Ext4Partition can not create ext4 partitions, it only reuses existing ext4 images
        """
        input = tmp_path / "input"
        input.write_bytes(b"".join([i.to_bytes(1, 'little') for i in range(256)]))
        obj = PartitionPartition()
        obj.content = RawContent()
        obj.content.file = input
        obj.fstype = "ext4"

        obj.start = SizeType(32)
        obj.prepare()
        assert obj.size.bytes == 256


        out_file = BytesIO()
        obj.write(out_file)
        assert out_file.tell() == 256 + 32

        assert out_file.getbuffer()[32:] == input.read_bytes()
