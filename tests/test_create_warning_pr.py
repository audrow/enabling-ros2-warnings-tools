from enabling_ros2_warnings_tools import create_warning_pr
import pytest


@pytest.mark.parametrize('items, expected', [
    (['-W1'], '-W1'),
    (['-W1', '-W2'], '-W1 and -W2'),
    (['-W1', '-W2', '-W3'], '-W1, -W2, and -W3'),
    (['-W1', '-W2', '-W3', '-W4'], '-W1, -W2, -W3, and -W4'),
])
def test_list_to_str(items, expected):
    assert create_warning_pr.list_to_str(*items) == expected


@pytest.mark.parametrize('items, expected', [
    (['-W1'], '`-W1`'),
    (['-W1', '-W2'], '-`W1` and `-W2`'),
    (['-W1', '-W2', '-W3'], '`-W1`, `-W2`, and `-W3`'),
    (['-W1', '-W2', '-W3', '-W4'], '`-W1`, `-W2`, `-W3`, and `-W4`'),
])
def test_list_to_str_with_ticks(items, expected):
    assert create_warning_pr.list_to_str(*items, is_wrap_in_ticks=True) == expected


def test_list_to_str_no_input():
    with pytest.raises(ValueError):
        create_warning_pr.list_to_str()
