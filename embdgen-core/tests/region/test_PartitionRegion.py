# SPDX-License-Identifier: GPL-3.0-only

from io import BytesIO
from pathlib import Path

from embdgen.core.utils.SizeType import SizeType
from embdgen.plugins.region.PartitionRegion import PartitionRegion
from embdgen.plugins.content.RawContent import RawContent

class TestPartitionRegion:
    def test_raw(self, tmp_path: Path):
        """
        At the moment PartitionRegion can not create ext4 regions, it only reuses existing ext4 images
        """
        input = tmp_path / "input"
        input.write_bytes(b"".join([i.to_bytes(1, 'little') for i in range(256)]))
        obj = PartitionRegion()
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
