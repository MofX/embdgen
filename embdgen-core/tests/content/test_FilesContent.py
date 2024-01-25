# SPDX-License-Identifier: GPL-3.0-only

from embdgen.plugins.content.FilesContent import FilesContent

class TestFilesContent():
    def test_init(self):
        obj = FilesContent()
        obj.prepare()
        assert obj.size.is_undefined, "There is nothing to calculate size from"
