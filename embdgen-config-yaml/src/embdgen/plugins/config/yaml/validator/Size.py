import strictyaml as y
from  strictyaml.parser import YAMLChunk

from embdgen.core.utils.SizeType import SizeType

class Size(y.ScalarValidator):
    RESULT_TYPE = SizeType

    def validate_scalar(self, chunk: YAMLChunk) -> SizeType:
        try:
            return SizeType.parse(chunk.contents)
        except Exception as e:
            chunk.expecting_but_found(f"when expecting a size ({str(e)})")
            raise # Cannot be reached, but without this pylint complaints about inconsistent-return-statements
