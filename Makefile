VENV ?= .venv-dev
PY := $(VENV)/bin/python
PRECOMMIT := $(VENV)/bin/pre-commit

.PHONY: setup test lint format organize

setup:
	python3 -m venv $(VENV)
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install -r requirements-dev.txt
	$(PRECOMMIT) install
	$(PRECOMMIT) install --hook-type commit-msg
	git config commit.template .gitmessage

test:
	$(PY) -m pytest -q

lint:
	$(PY) -m ruff check scripts tests

format:
	$(PY) -m ruff format scripts tests

organize:
	$(PY) scripts/organizar.py
	$(PY) scripts/indice.py
