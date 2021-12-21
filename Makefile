build:
	poetry build

install:
	poetry install

publish:
	poetry publish --dry-run

page-loader:
	poetry run page-loader

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 page_loader tests

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build