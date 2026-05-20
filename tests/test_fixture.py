import pytest

from iil_demo_fixture import apply_demo_fixture


def test_should_import_apply_demo_fixture():
    assert callable(apply_demo_fixture)


def test_should_raise_not_implemented_until_implemented():
    with pytest.raises(NotImplementedError):
        apply_demo_fixture(env="staging")


def test_should_raise_not_implemented_for_local_env():
    with pytest.raises(NotImplementedError):
        apply_demo_fixture(env="local")
