import abc
from . import BaseRegion
from ..content import BaseContent

from ..utils.class_factory import Config

@Config('content')
class BaseContentRegion(BaseRegion, abc.ABC):
    content: BaseContent = None

    def prepare(self) -> None:
        if not self.size.is_undefined:
            self.content.size = self.size
        self.content.prepare()

        if self.size.is_undefined:
            self.size = self.content.size

        super().prepare()


    def __repr__(self) -> str:
        return (f"{self.start.hex_bytes} - {(self.start + self.size).hex_bytes} Part {self.name}\n" +
                f"    {self.content}")
