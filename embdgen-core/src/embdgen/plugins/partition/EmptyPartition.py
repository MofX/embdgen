from embdgen.core.partition.BasePartition import BasePartition

class EmptyPartition(BasePartition):
    """A partition without any data

    This can be used to reserve a range (e.g. for the uboot environment)
    This does not generate an entry in the partition table.
    """
    PART_TYPE = 'empty'

    def __init__(self) -> None:
        super().__init__()
        self.is_partition = False

    def write(self, out_file):
        pass # Nothing to do for empty partition
