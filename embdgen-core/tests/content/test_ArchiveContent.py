# SPDX-License-Identifier: GPL-3.0-only

from pathlib import Path
import subprocess

from embdgen.plugins.content.ArchiveContent import ArchiveContent
from embdgen.core.utils.image import get_temp_path

def test_simple(tmp_path: Path):
    get_temp_path.TEMP_PATH = tmp_path
    
    prepare_dir = tmp_path / "prepare"
    archive = tmp_path / "archive.tar"

    prepare_dir.mkdir()
    (prepare_dir / "foo").write_text("foo")
    (prepare_dir / "bar").mkdir()
    (prepare_dir / "bar" / "a").touch()
    (prepare_dir / "bar" / "b").touch()

    subprocess.run([
        "tar",
        "-cf",
        archive,
        "."
    ], check=True, cwd=prepare_dir)


    obj = ArchiveContent()
    obj.archive = archive
    obj.prepare()

    assert sorted(map(lambda x: x.name, obj.files)) == ["bar", "foo"]

