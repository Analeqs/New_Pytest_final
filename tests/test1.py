import pytest


@pytest.fixture(scope="function")
def fixture_sample():
    print("Fixture run")


@pytest.fixture(scope="class", autouse=True)
def fixture_sample_class():
    print("Class fixture run")
    yield
    print("Finishing class fixture run")


def test_print(fixture_sample):
    print("Running test print")


@pytest.mark.negative
def test_fail():
    number = 3
    assert number == 3


@pytest.mark.skip("Skpi my bug")
def test_skip():
    assert False


@pytest.mark.negative
@pytest.mark.xfail  # xpass this test case will pass
def test_xfail():
    assert True


@pytest.mark.xfail  # xfail this test case will fail
def test_xfail2():
    assert False


@pytest.mark.run(order=1)
@pytest.mark.parametrize("num, output", [(1, 8), (2, 16), (3, 24), (4, 32)])
def test_multiplication(num, output):
    assert 8 * num == output


@pytest.mark.usefixtures("fixture_sample_class")
class TestClassCase:
    def test_1(self):
        assert True

    def test_2(self):
        assert True

    def test_31(self, fixture_auto):
        assert True


