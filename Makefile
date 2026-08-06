PYTHON ?= python3

.PHONY: check setup test test-all run notebooks

check:
	./scripts/validate_repository.sh

setup:
	./scripts/setup_python.sh --apply

test:
	$(PYTHON) -m unittest discover -s labs/librereserva/tests -v

test-all:
	.venv/bin/python -m pytest labs/librereserva/tests modules/07_pruebas -v

run:
	.venv/bin/python -m uvicorn labs.librereserva.app.main:app --reload

notebooks:
	.venv/bin/jupyter lab modules
