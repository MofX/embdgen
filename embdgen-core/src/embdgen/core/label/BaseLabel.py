# SPDX-License-Identifier: GPL-3.0-only

import abc
from typing import List
from pathlib import Path
import parted

from embdgen.core.utils.SizeType import SizeType
from embdgen.core.utils.image import create_empty_image
from ..utils.class_factory import Config
from ..region import BaseRegion



@Config('parts')
@Config('boot_partition', optional=True)
class BaseLabel(abc.ABC):
    """Base class for labels (i.e. partition types, e.g. MBR or GPT)"""

    parts: List[BaseRegion]
    """List of regions to be included in the image"""

    boot_partition: str = None
    """Name of the partitions marked as 'bootable'"""

    def __init__(self):
        self.parts = []

    def _prepare(self):
        for part in self.parts:
            part.prepare()
        self.parts.sort(key=lambda x: x.start)
        cur_offset = SizeType(0)
        for part in self.parts:
            if part.start.is_undefined:
                part.start = cur_offset
            cur_offset = part.start + part.size

    def _create_partition_table(self, filename: Path, ptType: str):
        device = parted.getDevice(filename.as_posix())
        disk = parted.freshDisk(device, ptType)

        for part in self.parts:
            # This check is added here to ensure partition tables are not overwritten
            self.check_partition_table_collision(part)

            if not part.is_partition:
                continue
            geometry = parted.Geometry(device, start=part.start.sectors, length=part.size.sectors)
            partition = parted.Partition(
                disk=disk,
                type=parted.PARTITION_NORMAL,
                geometry=geometry,
                fs=parted.FileSystem(part.fstype, geometry=geometry)
            )
            if ptType == "msdos":
                partition.setFlag(parted.PARTITION_LBA)
            disk.addPartition(partition=partition, constraint=parted.Constraint(exactGeom=geometry))
            if part.name == self.boot_partition:
                partition.setFlag(parted.PARTITION_BOOT)
        disk.commit()

    def _create(self, filename: Path):
        size = self.calculate_image_size()
        create_empty_image(filename, size.bytes)

        self.create_partition_table(filename)

        with filename.open("rb+") as f:
            for part in self.parts:
                part.write(f)

    @abc.abstractmethod
    def prepare(self):
        pass

    @abc.abstractmethod
    def create(self, filename: str):
        pass

    @abc.abstractmethod
    def check_partition_table_collision(self, part: BaseRegion):
        pass

    @abc.abstractmethod
    def calculate_image_size(self):
        pass

    @abc.abstractmethod
    def create_partition_table(self, filename: Path):
        pass
