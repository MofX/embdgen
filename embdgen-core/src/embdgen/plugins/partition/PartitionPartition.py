from io import BufferedIOBase

from embdgen.core.utils.class_factory import Config
from embdgen.core.partition.BaseContentPartition import BaseContentPartition
from embdgen.core.content import BinaryContent

@Config('content')
@Config('fstype')
class PartitionPartition(BaseContentPartition):
    """Partition partition
    
    Currently this can only be generated from a BinaryContent,
    that already contains an ext4 filesystem.
    """
    PART_TYPE = 'partition'

    content: BinaryContent
    """Content of this partition"""

    fstype: str
    """FS type of this partition"""

    def write(self, out_file: BufferedIOBase):
        out_file.seek(self.start.bytes)
        self.content.write(out_file)
