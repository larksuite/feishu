SHELL = bash

all: install_dev isort isort_check lint test
check: install_dev isort isort_check lint
all-cov: install_dev isort isort_check lint test-cov

install_dev:
	@pip install -e .[dev]

isort:
	@isort -s venv -s venv_py -s .tox -s docs -rc --atomic .

isort_check:
	@isort -rc -s venv -s venv_py -s .tox -s docs -c .

lint:
	@flake8

test:
	./.github/test.sh

test-cov:
	./.github/test.sh cov

clean:
	@rm -rf .pytest_cache .tox bytedmypackage.egg-info
	@rm -rf tests/*.pyc tests/__pycache__

.IGNORE: install_dev
.PHONY: all check install_dev isort isort_check lint test test-cov
