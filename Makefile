# DevOps Makefile for Taiwan Transport TDX Mega Hub

PYTHON = python3
PIP = pip3
VENV = .venv
APP_ENTRY = src/taiwan_transport_tdx_mega/server.py

.PHONY: setup run-stdio run-http clean docker-build docker-run test

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

run-stdio:
	$(VENV)/bin/python $(APP_ENTRY) --mode stdio

run-http:
	$(VENV)/bin/python $(APP_ENTRY) --mode http --port 8001

test:
	PYTHONPATH=src $(VENV)/bin/pytest tests/

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +

docker-build:
	docker build -t taiwan-transport-tdx-mega .

docker-run:
	docker run -p 8001:8001 taiwan-transport-tdx-mega
