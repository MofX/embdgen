YAML Config Interface
=====================

The configuration interfaces using a YAML file is implemented in the plugin embdgen-config-yaml.
This can load a configuration file and run embdgen, to generate an image.

The config file structure directly relates to the reference below. With the root element being a "Label".

Every element in the tree is YAML sequence, that contains a scalar ``type``, that identifies the implementation.

.. literalinclude:: examples/simple.yml
    :language: YAML
    :linenos:
    :caption: simple example
    :lines: 8-

The example above would create a master boot record partition table, with one real partition (boot).
This fat32 partition is created by embdgen and contains a single file (fitimage).
Three additional partitions are created, that are not recorded in the partition table.
This setup is an example for the bootloader requirements at the NXP's S32 series of SoCs:

 - uboot part 1 and 2: They write NXP specific code (i.e. the image vector table with it's payload uboot and atf) around
   the partition table (between byte 256 and 512)
 - uboot.env: This creates an unused range (type: empty) between 0x1e0000 and 0x1e2000, which is the default area, where
   NXP's u-boot writes its environment


To generate the image, the embdgen can be executed from the directory where the config file is stored and the files directory with the referenced files exist.
Assuming the yaml config is save as config.yml::

    $ embdgen config.yml
    Preparing...

    The final layout:
    MBR:
    0x00000000 - 0x00000100 Part u-boot part 1
        RawContent(files/fip.s32@0x00000000)
    0x000001b8 - 0x00000200 Part MBR Header
    0x00000200 - 0x000fead0 Part u-boot part 2
        RawContent(files/fip.s32@0x00000200)
    0x001e0000 - 0x001e2000 Part uboot.env
    0x001e2000 - 0x065e2000 Part boot
        FilesContent(files/fitimage)

    Writing image to image.raw

The tool prints out the final layout of all Regions.
There is now one more region than defined in the config file ("MBR Header").
This is inserted by the MBR label, to reserve the area where the partition table is written to.
For the boot partition no start address was defined in the config file, so this address is calculated automatically to the next free offset in the image.

Reference
=========

This configuration reference is generated with all plugins loaded.

Label Types
-----------

.. embdgen-config:: embdgen.core.label.Factory


Region Types
---------------

.. embdgen-config:: embdgen.core.region.Factory


Content Types
-------------

.. embdgen-config:: embdgen.core.content.Factory
