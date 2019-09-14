import pytest
from lab_2.__main__ import main


class TestClass:
    def test_request_lib_work(self):
        assert main('http://time.jsontest.com/')

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
