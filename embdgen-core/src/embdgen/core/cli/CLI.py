# SPDX-License-Identifier: GPL-3.0-only

import sys
from typing import Optional, Sequence
from pathlib import Path
from dataclasses import dataclass
from argparse import ArgumentParser

from ..config.Factory import Factory
from ..utils.image import get_temp_path

@dataclass(init=False)
class Arguments:
    format: Optional[str]
    output: Path
    tempdir: Path
    filename: Path

class CLI:
    factory = Factory()

    def register_config_loaders(self, parser: ArgumentParser):
        loaders = []
        for name, _ in self.factory.class_map().items():
            loaders.append(name)
        parser.add_argument("-x", "--format", choices=loaders,
                            help="Select the config format (default is autodetect)")

    def build_parser(self) -> ArgumentParser:
        parser = ArgumentParser(
            description = "embdgen - EMBedded Disk GENerator"
        )
        self.register_config_loaders(parser)
        parser.add_argument("-o", "--output", default="image.raw", type=Path,
                            help="Output file name (default: image.raw)")
        parser.add_argument("-t", "--tempdir", default="tmp", type=Path,
                            help="Temporary directory (default: tmp)")
        parser.add_argument("filename", type=Path, help="Config file name")
        return parser

    def run(self, args: Sequence[str] = None):
        options = self.build_parser().parse_args(args, namespace=Arguments())
        if not options.filename.exists():
            self.fatal(f"The config file {options.filename} does not exist")

        if options.format is None:
            options.format = self.probe_format(options.filename)
            if options.format is None:
                self.fatal("Unable to detect the format of the config file")

        get_temp_path.TEMP_PATH = options.tempdir
        get_temp_path.TEMP_PATH.mkdir(parents=True, exist_ok=True)

        label = self.factory.by_type(options.format)().load(options.filename)

        print("Preparing...")
        label.prepare()

        print("\nThe final layout:")
        print(label)

        print(f"\nWriting image to {options.output}")
        label.create(options.output)

    def probe_format(self, filename: Path):
        for name, typ in self.factory.class_map().items():
            if typ.probe(filename):
                return name
        return None


    def fatal(self, msg: str):
        sys.exit(f"FATAL: {msg}")
