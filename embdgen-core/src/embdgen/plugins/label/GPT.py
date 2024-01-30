# SPDX-License-Identifier: GPL-3.0-only

import io
from pathlib import Path

from embdgen.core.region.BaseRegion import BaseRegion
from embdgen.core.utils.SizeType import SizeType
from embdgen.core.label.BaseLabel import BaseLabel

class PMBRHeader(BaseRegion):

    def __init__(self) -> None:
        super().__init__()
        self.name = "PMBR Header"
        self.is_partition = False
        self.start = SizeType(0x1b8)
        self.size = SizeType(0x48)

    def write(self, out_file: io.BufferedIOBase):
        return


class GPTHeader(BaseRegion):

    def __init__(self) -> None:
        super().__init__()
        self.name = "GPT Header"
        self.is_partition = False
        self.start = SizeType(0x200)
        self.size = SizeType(512*33)

    def write(self, out_file: io.BufferedIOBase):
        return

class GPT(BaseLabel):
    """GUID Partition Table (GPT) partition type"""
    LABEL_TYPE = 'gpt'

    GPT_DISK_ID_OFFSET = 0x238

    pmbr_header: PMBRHeader = None
    gpt_header: GPTHeader = None

    def __init__(self) -> None:
        super().__init__()
        self.pmbr_header = PMBRHeader()
        self.gpt_header = GPTHeader()
        self.parts.append(self.pmbr_header)
        self.parts.append(self.gpt_header)

    def check_partition_table_collision(self, part: BaseRegion):
        if self.LABEL_TYPE == "gpt":
            if part.name in ('GPT Header', 'PMBR Header'):
                return
            part_end = part.start + part.size
            if part.start <= self.pmbr_header.start:
                if part_end > self.pmbr_header.start:
                    raise Exception (f"The region starting at {part.start} overwrites PMBR region")
            elif part.start < (self.gpt_header.start + self.gpt_header.size):
                raise Exception (f"The region starting at {part.start} overwrites PMBR or GPT region")


    def prepare(self):
        if self.pmbr_header not in self.parts:
            self.parts.append(self.pmbr_header)
        if self.gpt_header not in self.parts:
            self.parts.append(self.gpt_header)
        super()._prepare()


    def calculate_image_size(self) -> SizeType:
        # For GPT, size of backup GPT Partition table is added to the image size
        return self.parts[-1].start + self.parts[-1].size + self.gpt_header.size


    def create_partition_table(self, filename: Path):
        self._create_partition_table(filename, "gpt")

    def create(self, filename: Path):
        super()._create(filename)

    def __repr__(self) -> str:
        return "GPT:\n  " + "\n  ".join(map(repr, self.parts))
