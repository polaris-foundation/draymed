import filecmp
from pathlib import Path


class TestCheckMasterCodes:
    # Check that local copy of master codes file is identical with the source file.
    def test_codes_file_is_consistent(self) -> None:

        source_filepath: Path = (
            Path(__file__).parent.parent.parent / "master_codes.json"
        )

        target_filepath: Path = (
            Path(__file__).parent.parent / "draymed/data/master_codes.json"
        )

        assert filecmp.cmp(source_filepath, target_filepath)
