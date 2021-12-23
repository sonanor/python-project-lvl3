from tempfile import TemporaryDirectory

from page_loader.downloader import download_page


def test_download(requests_mock):
    with TemporaryDirectory() as tmpdir_for_test:
        requests_mock.get('http://endoftheinternet.com', text='data')
        file_path = download_page(tmpdir_for_test, 'http://endoftheinternet.com')
        with open(file_path) as file:
            assert 'data\n' == file.read()
