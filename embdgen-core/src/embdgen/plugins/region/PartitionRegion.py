from io import BufferedIOBase

from embdgen.core.utils.class_factory import Config
from embdgen.core.region.BaseContentRegion import BaseContentRegion
from embdgen.core.content import BinaryContent

@Config('content')
@Config('fstype')
class PartitionRegion(BaseContentRegion):
    """Partition region

    Currently this can only be generated from a BinaryContent,
    that already contains an ext4 filesystem.
    """
    PART_TYPE = 'partition'

    content: BinaryContent
    """Content of this Region"""

    fstype: str
    """FS type of this region"""

    def write(self, out_file: BufferedIOBase):
        out_file.seek(self.start.bytes)
        self.content.write(out_file)
