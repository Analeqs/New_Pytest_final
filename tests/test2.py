import pytest


@pytest.mark.xfail  # xfail this test case will fail
def test_xfail2():
    assert False
