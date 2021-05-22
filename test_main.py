import main


class TestMain:

    def test_add(self):
        assert 4 == main.add(1, 3)

    def test_subtract(self):
        assert 4 == main.subtract(10, 6)
