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

security:
	bandit -r $(PACKAGE)

test: activate
	pytest --cov=$(PACKAGE) -s -v

pre-release: security test
	python utils/version.py $(CHANGE_TYPE)

build-release:
	rm -rf dist
	rm -rf build
	python setup.py bdist_wheel
	python setup.py sdist

release-pypi-test:
	twine upload --repository testpypi dist/*
