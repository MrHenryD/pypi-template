PACKAGE=teenytiny
PYTHON_VERSION=3.11.9
CHANGE_TYPE ?= patch

fmt_dir := teenytiny tests utils


export PYTHONPATH=teenytiny


activate:
	pyenv local $(PYTHON_VERSION)

install: activate
	pip install ".[testing]"

style:
	black $(fmt_dir)

test: activate
	pytest -s -v

pre-release:
	python utils/version.py $(CHANGE_TYPE)

build-release:
	rm -rf dist
	rm -rf build
	python setup.py bdist_wheel
	python setup.py sdist

release-pypi-test:
	twine upload --repository testpypi dist/*
