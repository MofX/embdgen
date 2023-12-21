import io
import subprocess

from embdgen.core.utils.class_factory import Config
from embdgen.core.partition.BaseContentPartition import BaseContentPartition
from embdgen.plugins.content.FilesContent import FilesContent
from embdgen.core.utils.image import create_empty_image, copy_sparse, get_temp_path

@Config('content')
class Fat32Partition(BaseContentPartition):
    """Fat32 partition
    
    Currently this can only be created using a FilesContent,
    that contains a list of files, that are copied to the root
    of a newly created fat32 filesystem.
    """
    PART_TYPE = 'fat32'

    content: FilesContent
    """Content of this partition"""

    def prepare(self) -> None:
        super().prepare()
        if self.size.is_undefined:
            raise Exception("Fat32 partitions require a fixed size at the moment")

    def write(self, out_file: io.BufferedIOBase):
        tmp_name = get_temp_path() / (self.name + ".tmp")
        create_empty_image(tmp_name, self.size.bytes)
        subprocess.run([
                "mkfs.vfat",
                tmp_name
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        for file in self.content.files:
            subprocess.run(
                [
                    "mcopy",
                    "-i", tmp_name,
                    file, "::"
                ],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )

        out_file.seek(self.start.bytes)
        with open(tmp_name, "rb") as in_file:
            copy_sparse(out_file, in_file, self.size.bytes)
