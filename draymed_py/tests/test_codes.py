import pytest

import draymed.codes


class TestDraymedCodes:

    # Description From Code / Name

    def test_description_from_code(self) -> None:
        assert draymed.codes.description_from_code("386359008") == "Oral meds"

    def test_description_from_name(self) -> None:
        assert draymed.codes.description_from_name("oralMeds") == "Oral meds"

    def test_description_from_name_with_category(self) -> None:
        assert (
            draymed.codes.description_from_name("oralMeds", category="management_type")
            == "Oral meds"
        )

    def test_description_from_code_with_category(self) -> None:
        assert (
            draymed.codes.description_from_code(
                "1761000175102", category="routine_sct_code"
            )
            == "Lunch"
        )

    def test_description_from_code_with_non_existent_category(self) -> None:
        with pytest.raises(KeyError):
            draymed.codes.description_from_code("1761000175102", category="abcdefg")

    def test_name_from_code_with_wrong_category(self) -> None:
        with pytest.raises(KeyError):
            draymed.codes.description_from_code(
                "1761000175102",
                category="observable_entity",
            )

    def test_name_from_null_code(self) -> None:
        with pytest.raises(ValueError):
            draymed.codes.description_from_code(None)  # type:ignore

    def test_name_from_empty_code(self) -> None:
        with pytest.raises(ValueError):
            draymed.codes.description_from_code("")

    def test_name_from_non_existent_code(self) -> None:
        with pytest.raises(KeyError):
            draymed.codes.description_from_code("abcdefg")

    # Code From Name

    def test_code_from_name(self) -> None:
        assert draymed.codes.code_from_name("oralMeds") == "386359008"

    def test_code_from_name_with_category(self) -> None:
        assert (
            draymed.codes.code_from_name("lunch", category="routine_sct_code")
            == "1761000175102"
        )

    def test_code_from_name_with_non_existent_category(self) -> None:
        with pytest.raises(KeyError):
            draymed.codes.description_from_code("lunch", category="abcdefg")

    def test_code_from_name_with_wrong_category(self) -> None:
        with pytest.raises(KeyError):
            draymed.codes.code_from_name("lunch", category="neonatal_complications")

    def test_code_from_null_name(self) -> None:
        with pytest.raises(ValueError):
            draymed.codes.description_from_code(None)  # type:ignore

    def test_code_from_empty_name(self) -> None:
        with pytest.raises(ValueError):
            draymed.codes.description_from_code("")

    def test_code_from_non_existent_name(self) -> None:
        with pytest.raises(KeyError):
            draymed.codes.description_from_code("abcdefg")

    def test_code_from_description(self) -> None:
        assert draymed.codes.code_from_description("Type 1") == "46635009"

    def test_code_from_description_with_category(self) -> None:
        assert (
            draymed.codes.code_from_description("Type 1", category="diabetes_type")
            == "46635009"
        )

    # Category From Code

    def test_category_from_code(self) -> None:
        assert draymed.codes.category_from_code("1761000175102") == "routine_sct_code"

    def test_category_from_null_code(self) -> None:
        with pytest.raises(ValueError):
            draymed.codes.category_from_code(None)  # type:ignore

    def test_category_from_empty_code(self) -> None:
        with pytest.raises(ValueError):
            draymed.codes.category_from_code("")

    def test_category_non_existent_code(self) -> None:
        with pytest.raises(KeyError):
            draymed.codes.category_from_code("abcdefg")

    # Category From Name

    def test_category_from_name(self) -> None:
        assert draymed.codes.category_from_name("lunch") == "routine_sct_code"

    def test_category_from_null_name(self) -> None:
        with pytest.raises(ValueError):
            draymed.codes.category_from_name(None)  # type:ignore

    def test_category_from_empty_name(self) -> None:
        with pytest.raises(ValueError):
            draymed.codes.category_from_name("")

    def test_category_non_existent_name(self) -> None:
        with pytest.raises(KeyError):
            draymed.codes.category_from_name("abcdefg")

    # Code Exists

    def test_exists(self) -> None:
        assert draymed.codes.code_exists("1761000175102")

    def test_exists_with_category(self) -> None:
        assert draymed.codes.code_exists("17369002", category="outcome_for_baby")

    def test_exists_with_wrong_category(self) -> None:
        assert draymed.codes.code_exists("17369002", category="birth_outcome") == False

    def test_exists_with_non_existent_category(self) -> None:
        with pytest.raises(KeyError):
            draymed.codes.code_exists("17369002", category="some_category")

    def test_exists_with_null_code(self) -> None:
        with pytest.raises(ValueError):
            draymed.codes.code_exists(None)  # type:ignore

    def test_exists_with_empty_code(self) -> None:
        with pytest.raises(ValueError):
            draymed.codes.code_exists("")

    def test_exists_with_non_existent_code(self) -> None:
        assert draymed.codes.code_exists("a1b2c3d4e5") == False

    # Category

    def test_list_category(self) -> None:
        category = draymed.codes.list_category("birth_outcome")
        assert isinstance(category, dict)

    def test_list_category_with_null_category(self) -> None:
        with pytest.raises(ValueError):
            draymed.codes.list_category(None)  # type:ignore

    def test_list_category_with_empty_category(self) -> None:
        with pytest.raises(ValueError):
            draymed.codes.list_category("")

    def test_list_category_with_wrong_category(self) -> None:
        with pytest.raises(KeyError):
            draymed.codes.list_category("some_non_category")

    # Find Or None

    def test_find_or_none_with_code(self) -> None:
        assert (
            draymed.codes.find_or_none(draymed.codes.description_from_code, "169826009")
            == "Live birth"
        )

    def test_find_or_none_with_code_category(self) -> None:
        assert (
            draymed.codes.find_or_none(
                draymed.codes.description_from_code,
                "52767006",
                category="neonatal_complications",
            )
            == "Hypoglycemia"
        )

    def test_find_or_none_with_wrong_code(self) -> None:
        assert (
            draymed.codes.find_or_none(
                draymed.codes.description_from_code, "a1b2c3d4e5f6"
            )
            is None
        )

    def test_find_or_none_with_null_code(self) -> None:
        code: str = None  # type:ignore
        assert (
            draymed.codes.find_or_none(draymed.codes.description_from_code, code)
            is None
        )

    def test_find_or_none_with_empty_code(self) -> None:
        assert (
            draymed.codes.find_or_none(draymed.codes.description_from_code, "") is None
        )

    def test_find_or_none_with_name(self) -> None:
        assert (
            draymed.codes.find_or_none(draymed.codes.code_from_name, "hypoglycemia")
            == "52767006"
        )

    def test_find_or_none_with_name_category(self) -> None:
        assert (
            draymed.codes.find_or_none(
                draymed.codes.code_from_name, "other", category="education_level"
            )
            == "365460000"
        )

    def test_find_or_none_with_null_name(self) -> None:
        code: str = None  # type:ignore
        assert (
            draymed.codes.find_or_none(draymed.codes.description_from_code, code)
            is None
        )

    def test_find_or_none_with_empty_name(self) -> None:
        assert (
            draymed.codes.find_or_none(draymed.codes.description_from_name, "") is None
        )
