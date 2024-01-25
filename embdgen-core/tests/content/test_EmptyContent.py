# SPDX-License-Identifier: GPL-3.0-only

from pathlib import Path

from embdgen.core.utils.SizeType import SizeType
from embdgen.plugins.content.EmptyContent import EmptyContent

def test_EmptyContent(tmp_path: Path):
    image = tmp_path / "image.raw"

    obj = EmptyContent()
    obj.size = SizeType(2048)

    obj.prepare()

    assert obj.size.bytes == 2048

    with image.open("wb+") as f:
        obj.write(f)

        assert f.tell() == 2048
        # Allow EmptyContent to only seek, not write anything
        f.write(b"\1")
    
    assert image.read_bytes() == (b"\0" * 2048) + b"\1"

