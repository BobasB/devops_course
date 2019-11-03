import pytest
import requests


@pytest.fixture
def url(request):
    url = request.config.getoption("--url")
    if not url:
        raise ValueError('HITS URL was not provided. Use \'--url\' option to set up')
    return url


def test_default_urls_check(url):
    hits = requests.get(url + '/hits')
    assert len(hits.text) > 0, 'Main page is empty'
    logs = requests.get(url + '/logs')
    assert len(logs.text) > 0, 'Logs are empty'


def test_hits(url):
    response = requests.get(url + '/hits')
    assert response.text is not None, 'No value'


def test_logs(url):
    response = requests.get(url + '/logs')
    assert 'My Hostname is:' in response.text, 'Logs do not have Hostname'


def test_main_page(url):
    response = requests.get(url)
    assert 'You are at main page.' in response.text, 'Main page without text'
