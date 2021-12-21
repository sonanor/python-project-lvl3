from tempfile import TemporaryDirectory

from page_loader.downloader import download, create_filepath_output

FILE_NAME_CORRECT = '/var/tmp/ru-hexlet-io-courses.html'


def test_make_file_path():
    file_name = create_filepath_output('https://ru.hexlet.io/courses',
                                       '/var/tmp')
    assert FILE_NAME_CORRECT == file_name


def test_download(requests_mock):
    with TemporaryDirectory() as tmpdir_for_test:
        requests_mock.get('https://ru.hexlet.io/courses', text='data')
        file_path = download(tmpdir_for_test, 'https://ru.hexlet.io/courses')
        with open(file_path) as file:
            assert 'data' == file.read()
