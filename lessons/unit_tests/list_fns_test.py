"""Testing list functions."""

from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first_names_output() -> None:
    """Test get first with nanms in a list for output."""
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    assert get_first(names) == "Alyssa"


def test_get_and_remove_first_names_output() -> None:
    """Test get and remove first with names in a list for output."""
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    assert get_and_remove_first(names) == "Alyssa"


def test_remove_first_names_behavior() -> None:
    """Test remove first behavior on names."""
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    remove_first(names)
    assert names == ["Izzi", "Anusha", "Benjamin"]


def test_get_and_remove_first_names_behavior() -> None:
    """Test get and remove first behavior on names."""
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    get_and_remove_first(names)
    assert names == ["Izzi", "Anusha", "Benjamin"]


def test_get_first_names_behavior() -> None:
    """Test get first behavior on names."""
    names: list[str] = ["Alyssa", "Izzi", "Anusha", "Benjamin"]

    get_first(names)
    assert names == ["Alyssa", "Izzi", "Anusha", "Benjamin"]


# python -m pytest lessons/unit_tests/list_fns_test.py
# You can also go to testing on the left hand side!


def test_get_first_empty_output() -> None:
    """."""
    assert get_first([]) == ""
