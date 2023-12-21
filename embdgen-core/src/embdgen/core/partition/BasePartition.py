import abc
import io
from ..utils.SizeType import SizeType

from ..utils.class_factory import Config

@Config('name')
@Config('start', optional=True)
@Config('size', optional=True)
class BasePartition(abc.ABC):
    """Base class for partitions

    A partition is not necessarily part of the partition table.
    It is just a part of the final image with a start and a size.
    """

    name: str #: Name of the partition
    start: SizeType
    """Start of the partition

    This can either be specified or should be calculated automatically
    by the label implementation.
    """
    size: SizeType
    """Size of the partition

    This can either be specified or should be calculated automatically
    by the label or the content
    """
    is_partition: bool = True
    """Set to false to exclude this from the partition table"""

    def __init__(self) -> None:
        self.start = SizeType()
        self.size = SizeType()

    def __repr__(self) -> str:
        return f"{self.start.hex_bytes} - {(self.start + self.size).hex_bytes} Part {self.name}"

    def prepare(self) -> None:
        """Prepare for writing to the image file.

        Depending on the implementation, this calculates missing attributes (e.g. size)
        or even prepares a temporary file.
        """

    @abc.abstractmethod
    def write(self, out_file: io.BufferedIOBase):
        """Writes this partition to the current position in ``out_file``"""
