import pytest
import add


@pytest.mark.parametrize(
    "x, y, z, expected", [
        (1, 2, (3, ), 6),
        (2, 3, (), 5),
        (43, 65, (21, 32, 22), 183)
    ]
)
def test_add(x, y, z, expected):
    assert add.add(x, y, *z) == expected