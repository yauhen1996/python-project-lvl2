install:  
	poetry install

package-install: 
	python3 -m pip install --user dist/*.whl --force-reinstall

test: 
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

