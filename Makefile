PYTHON ?= python3

.PHONY: check setup test test-all test-sesion12 run notebooks

check:
	./scripts/validate_repository.sh

setup:
	./scripts/setup_python.sh --apply

test:
	$(PYTHON) -m unittest discover -s labs/librereserva/tests -v

test-all:
	.venv/bin/python -m pytest labs/librereserva/tests modules/07_pruebas -v

test-sesion12:
	LIBRERESERVA_REPOSITORY=memory .venv/bin/python -m pytest \
		labs/librereserva/tests/test_domain.py \
		modules/07_pruebas/test_http.py \
		modules/07_pruebas/test_consulta_segura.py -v

run:
	.venv/bin/python -m uvicorn labs.librereserva.app.main:app --reload

notebooks:
	.venv/bin/jupyter lab modules
