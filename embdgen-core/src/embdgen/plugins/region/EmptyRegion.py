# SPDX-License-Identifier: GPL-3.0-only

from embdgen.core.region.BaseRegion import BaseRegion

class EmptyRegion(BaseRegion):
    """A region without any data

    This can be used to reserve a range (e.g. for the uboot environment)
    This does not generate an entry in the partition table.
    """
    PART_TYPE = 'empty'

    def write(self, out_file):
        pass # Nothing to do for empty region
