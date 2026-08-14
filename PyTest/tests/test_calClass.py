from source.calClass import Cal


class TestCalClass:
    def setup_method(self, method):
        print(f"setting up {method}")
        self.cal = Cal()

    def teardown_method(self, method):
        print(method)

    def test_add(self):
        assert self.cal.add(1, 1) == 2
