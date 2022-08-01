import draymed


class TestNhsNumber:

    good_strings = ("1234567890", "0987654321", "6482749500")

    bad_strings = (
        "123-456-7890",
        "098 765 4321",
        "648274950",
        "64827495034",
        None,
        "",
        "a1b2c3d4e5",
    )

    def test_validate_good_nhs_number(self) -> None:
        for s in self.good_strings:
            assert draymed.validate_nhs_number(s) is True

    def test_validate_bad_nhs_number(self) -> None:
        for s in self.bad_strings:
            assert draymed.validate_nhs_number(s) is False  # type:ignore
