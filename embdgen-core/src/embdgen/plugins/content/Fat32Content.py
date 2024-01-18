import io
import subprocess

from embdgen.core.utils.class_factory import Config
from embdgen.core.content.BinaryContent import BinaryContent
from embdgen.plugins.content.FilesContent import FilesContent
from embdgen.core.utils.image import create_empty_image, copy_sparse

@Config("content")
class Fat32Content(BinaryContent):
    """Fat32 Content

    Currently this can only be created using a FilesContent,
    that contains a list of files, that are copied to the root
    of a newly created fat32 filesystem.
    """
    CONTENT_TYPE = "fat32"

    content: FilesContent
    """Content of this partition"""

    def prepare(self) -> None:
        super().prepare()
        if self.size.is_undefined:
            raise Exception("Fat32 partitions require a fixed size at the moment")


    def _prepare_result(self):
        create_empty_image(self.result_file, self.size.bytes)

        subprocess.run([
                "mkfs.vfat",
                self.result_file
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

        for file in self.content.files:
            subprocess.run(
                [
                    "mcopy",
                    "-i", self.result_file,
                    file, "::"
                ],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )


    def do_write(self, file: io.BufferedIOBase):
        with open(self.result_file, "rb") as in_file:
            copy_sparse(file, in_file, self.size.bytes)


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(map(str, self.content.files))})"
