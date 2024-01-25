# SPDX-License-Identifier: GPL-3.0-only

from io import BufferedIOBase

from embdgen.core.utils.class_factory import Config
from embdgen.core.region.BaseContentRegion import BaseContentRegion
from embdgen.core.content import BinaryContent


@Config('content')
class RawRegion(BaseContentRegion):
    """Raw region

    Writes some BinaryContent directly to the image
    without any partition table entry.
    """
    PART_TYPE = 'raw'

    content: BinaryContent
    """Content of this region"""

    def __init__(self) -> None:
        super().__init__()
        self.is_partition = False

    def write(self, out_file: BufferedIOBase):
        out_file.seek(self.start.bytes)
        self.content.write(out_file)
