from draymed.codes.code_map_transform import get_code_map


class TestCodeMapTransform:
    def test_get_code_map(self) -> None:

        output_codes = get_code_map()

        assert (
            output_codes["accessibility_considerations"]["82971005"]["long"]
            == "Impaired Mobility"
        )

        assert (
            output_codes["management_type"]["D0000007"]["long"] == "Diet and Exercise"
        )

        assert (
            output_codes["ethnicity"]["315635008"]["long"] == "White and Black African"
        )

        assert output_codes["closed_reason"]["D0000029"]["short"] == "movedOutOfArea"
