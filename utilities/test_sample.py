# See: http://docs.pytest.org/en/latest/getting-started.html#our-first-test-run

def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5