import io
import abc
from .BaseContent import BaseContent

class BinaryContent(BaseContent):
    """
    Base class for content, that support writing directly to an image file
    """

    @abc.abstractmethod
    def write(self, file: io.BufferedIOBase):
        pass
