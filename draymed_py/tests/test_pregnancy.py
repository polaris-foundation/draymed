import datetime

import pytest

from draymed import pregnancy


class TestPregnancy:
    def test_return_type(self) -> None:
        date = datetime.date.today()
        value = pregnancy.stage(date)
        assert isinstance(value, tuple)

    def test_return_fields(self) -> None:
        date = datetime.date.today()
        value = pregnancy.stage(date)
        assert hasattr(value, "weeks")
        assert hasattr(value, "days")

    def test_null_delivery_date(self) -> None:
        with pytest.raises(ValueError):
            pregnancy.stage(None)  # type: ignore

    def test_delivery_date_today(self) -> None:
        date = datetime.date.today()
        value = pregnancy.stage(date)
        assert value.weeks == 40
        assert value.days == 0

    def test_delivery_date_280_days(self) -> None:
        date = datetime.date.today() + datetime.timedelta(days=280)
        value = pregnancy.stage(date)
        assert value.weeks == 0
        assert value.days == 0

    def test_delivery_date_in_past(self) -> None:
        date = datetime.date.today() - datetime.timedelta(days=10)
        value = pregnancy.stage(date)
        assert value.weeks == 40
        assert value.days == 0

    def test_normal_return_values(self) -> None:
        date = datetime.date.today() + datetime.timedelta(days=15)
        value = pregnancy.stage(date)
        assert value.weeks == 37
        assert value.days == 6

        date = datetime.date.today() + datetime.timedelta(days=150)
        value = pregnancy.stage(date)
        assert value.weeks == 18
        assert value.days == 4
