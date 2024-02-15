# SPDX-License-Identifier: GPL-3.0-only

from pathlib import Path

from embdgen.plugins.content.FilesContent import FilesContent


class TestFilesContent():
    def test_init(self):
        obj = FilesContent()
        obj.prepare()
        assert obj.size.is_undefined, "There is nothing to calculate size from"

    def test_glob(self):
        obj = FilesContent()
        obj.files = [
            Path(__file__).parent / "data/test_content/*"
        ]

        assert list((Path(__file__).parent / "data/test_content/").iterdir()) == obj.files
