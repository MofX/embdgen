from io import BufferedIOBase

from embdgen.core.utils.class_factory import Config
from embdgen.core.partition.BaseContentPartition import BaseContentPartition
from embdgen.core.content import BinaryContent


@Config('content')
class RawPartition(BaseContentPartition):
    """Raw partition
    
    Writes some BinaryContent directly to the image
    without any partition table entry.
    """
    PART_TYPE = 'raw'

    content: BinaryContent
    """Content of this partition"""

    def __init__(self) -> None:
        super().__init__()
        self.is_partition = False

    def write(self, out_file: BufferedIOBase):
        out_file.seek(self.start.bytes)
        self.content.write(out_file)
