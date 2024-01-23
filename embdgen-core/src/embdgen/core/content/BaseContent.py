import abc

from ..utils.SizeType import SizeType

class BaseContent(abc.ABC):
    """Base class for content (i.e. region content)
    """

    size: SizeType

    def __init__(self):
        "Create a new empty content"
        self.size = SizeType()

    def prepare(self) -> None:
        """Prepare content

        This should calculate the size of the content
        and generate any files / information required by
        the owning class.
        """
