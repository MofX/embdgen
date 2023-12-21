from pathlib import Path
import strictyaml as y

from embdgen.core.config.BaseConfig import BaseConfig
from embdgen.core.label.BaseLabel import BaseLabel

from embdgen.plugins.config.yaml.validator.Label import Label as LabelValidator

__version__ = "0.0.1"

class YAML(BaseConfig):
    CONFIG_TYPE = "yaml"

    @classmethod
    def probe(cls, filename: Path) -> bool:
        try:
            with filename.open("r", encoding="utf-8") as f:
                res = y.load(f.read())
                return not isinstance(res.value, (str, int))
        except (UnicodeDecodeError, y.YAMLError):
            return False
        return True

    def load(self, filename: Path) -> BaseLabel:
        with filename.open(encoding="utf-8") as f:
            conf = y.load(f.read(), LabelValidator())
        return conf.value
