install:  
	poetry install

build: 
	poetry build

package-install: 
	python3 -m pip install --user dist/*.whl --force-reinstall

lint: 
	poetry run flake8 gendiff

pytest: 
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

