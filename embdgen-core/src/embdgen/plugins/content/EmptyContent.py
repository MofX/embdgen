# SPDX-License-Identifier: GPL-3.0-only

import io
from io import BufferedIOBase

from embdgen.core.content.BinaryContent import BinaryContent

class EmptyContent(BinaryContent):
    """Empty content"""
    CONTENT_TYPE = "empty"

    def do_write(self, file: BufferedIOBase):
        file.seek(self.size.bytes, io.SEEK_CUR)
