from main import validate_rut


def test_validate_rut():
    assert validate_rut('11.111.111-1') is True
    assert validate_rut('11.111.111-K') is False
