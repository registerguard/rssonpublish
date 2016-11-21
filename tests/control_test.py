# See: http://docs.pytest.org/en/latest/getting-started.html#our-first-test-run

def add(x,y):
    return x + y

def test_answer():
    assert add(1,2) == 3