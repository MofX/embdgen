import pytest
from pathlib import Path

from embdgen.core.utils.SizeType import SizeType
from embdgen.core.utils.image import create_empty_image
from embdgen.plugins.content.RawContent import RawContent


class TestRawContent():
    def test_assign_invalid_file(self):
        with pytest.raises(Exception):
            RawContent().file = "i-do-not-exist"

    def test_assign_file_and_offset(self, tmp_path: Path):
        tmp_file = tmp_path / "test.raw"
        tmp_file2 = tmp_path / "test2.raw"
        create_empty_image(tmp_file, 1024)
        create_empty_image(tmp_file2, 512)

        content = RawContent()
        content.file = tmp_file
        with pytest.raises(Exception):
            content.offset = SizeType(1025)
        assert content.offset == SizeType(0)

        content.offset = SizeType(1024)
        with pytest.raises(Exception):
            content.file = tmp_file2
        assert content.file == tmp_file


    def test_prepare(self, tmp_path: Path):
        tmp_file = tmp_path / "test.raw"
        create_empty_image(tmp_file, 1024)

        content = RawContent()
        content.file = tmp_file
        content.prepare()

        assert content.size == SizeType(1024)
        content.offset = SizeType(512)
        content.prepare()

        # TODO: This is the behavior right now. Does it make sense to not recalculate?
        assert content.size == SizeType(1024)

        content.size = SizeType()
        content.prepare()
        assert content.size == SizeType(512)


    def test_write(self, tmp_path: Path):
        input_file = tmp_path / "input.raw"
        target_file = tmp_path / "target.raw"
        create_empty_image(target_file, 1024)

        in_data = b"".join([i.to_bytes(1, 'little') for i in range(256)])

        with input_file.open("wb") as f:
            f.write(in_data)

        obj = RawContent()
        obj.file = input_file

        obj.prepare()
        with target_file.open("rb+") as f:
            f.seek(128)
            obj.write(f)
        
        with target_file.open("rb") as f:
            assert f.read() == (b"\0" * 128) + in_data + (b"\0" * (1024 - 128 - len(in_data)))
            

        create_empty_image(target_file, 1024)
        obj.offset = SizeType(128)
        obj.size = SizeType()
        obj.prepare()
        with target_file.open("rb+") as f:
            f.seek(128)
            obj.write(f)

        with target_file.open("rb") as f:
            assert f.read() == (b"\0" * 128) + in_data[128:] + (b"\0" * (1024 - 128 - len(in_data[128:])))

