# SPDX-License-Identifier: GPL-3.0-only

import io
import struct
from pathlib import Path
import parted

from embdgen.core.utils.class_factory import Config
from embdgen.core.region.BaseRegion import BaseRegion
from embdgen.core.utils.SizeType import SizeType
from embdgen.core.utils.image import create_empty_image
from embdgen.core.label.BaseLabel import BaseLabel

class MBRHeader(BaseRegion):
    diskid: int = None

    def __init__(self) -> None:
        super().__init__()
        self.name = "MBR Header"
        self.is_partition = False
        self.start = SizeType(0x1b8)
        self.size = SizeType(0x48)

    def write(self, out_file: io.BufferedIOBase):
        if self.diskid:
            out_file.seek(MBR.DISK_ID_OFFSET)
            out_file.write(struct.pack("I", self.diskid))

@Config('diskid', optional=True)
@Config('boot_partition', optional=True)
class MBR(BaseLabel):
    """Master Boot Record (DOS) partition type"""
    LABEL_TYPE = 'mbr'

    DISK_ID_OFFSET = 0x1B8

    boot_partition: str = None
    """Name of the partitions marked as 'bootable'"""

    mbr_header: MBRHeader = None

    def __init__(self) -> None:
        super().__init__()
        self.mbr_header = MBRHeader()
        self.parts.append(self.mbr_header)

    @property
    def diskid(self) -> int:
        """Diskid value (part of the partition table metadata)"""
        return self.mbr_header.diskid

    @diskid.setter
    def diskid(self, value: int):
        self.mbr_header.diskid = value

    def prepare(self):
        if self.mbr_header not in self.parts:
            self.parts.append(self.mbr_header)
        for part in self.parts:
            part.prepare()
        self.parts.sort(key=lambda x: x.start)
        cur_offset = SizeType(0)
        for part in self.parts:
            if part.start.is_undefined:
                part.start = cur_offset
            cur_offset = part.start + part.size

    def _create_partition_table(self, filename: Path):
        device = parted.getDevice(filename.as_posix())
        disk = parted.freshDisk(device, "msdos")

        for part in self.parts:
            if not part.is_partition:
                continue
            geometry = parted.Geometry(device, start=part.start.sectors, length=part.size.sectors)
            partition = parted.Partition(
                disk=disk,
                type=parted.PARTITION_NORMAL,
                geometry=geometry,
                fs=parted.FileSystem(part.fstype, geometry=geometry)
            )
            partition.setFlag(parted.PARTITION_LBA)
            disk.addPartition(partition=partition, constraint=parted.Constraint(exactGeom=geometry))
            if part.name == self.boot_partition:
                partition.setFlag(parted.PARTITION_BOOT)
        disk.commit()


    def create(self, filename: Path):
        size = self.parts[-1].start + self.parts[-1].size
        create_empty_image(filename, size.bytes)

        self._create_partition_table(filename)

        with filename.open("rb+") as f:
            for part in self.parts:
                part.write(f)

    def __repr__(self) -> str:
        return "MBR:\n  " + "\n  ".join(map(repr, self.parts))
