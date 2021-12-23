from tempfile import TemporaryDirectory

from page_loader.downloader import download_page, download_additional_sources


def test_download(requests_mock):
    with TemporaryDirectory() as tmpdir_for_test:
        requests_mock.get('http://endoftheinternet.com', text='data')
        file_path = download_page(tmpdir_for_test, 'http://endoftheinternet.com')
        with open(file_path) as file:
            assert 'data\n' == file.read()


def test_image_download(requests_mock):
    with TemporaryDirectory() as tmpdir_for_test:
        requests_mock.get('http://endoftheinternet.com/xkcd_book.png', text='data')
        file_paths = download_additional_sources(['http://endoftheinternet.com/xkcd_book.png'],
                                                 'http://endoftheinternet.com/', tmpdir_for_test)
        for file_path in file_paths:
            with open(file_path) as file:
                assert 'data' == file.read()

