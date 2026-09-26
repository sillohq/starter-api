.DEFAULT_GOAL := help
.PHONY: help setup install dev test lint format check smoke

PY := uv run
HOST ?= 127.0.0.1
PORT ?= 8000

help: ## Show available commands
	@grep -hE '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-12s %s\\n", $$1, $$2}'

setup: install ## Install dependencies and create .env
	@test -f .env || cp .env.example .env

install: ## Install development dependencies
	uv sync --all-extras

dev: ## Run the local API with reload
	$(PY) sillo dev --host $(HOST) --port $(PORT)

test: ## Run tests
	$(PY) pytest

lint: ## Check lint and formatting
	$(PY) ruff check .
	$(PY) ruff format --check .

format: ## Format and fix lint issues
	$(PY) ruff format .
	$(PY) ruff check --fix .

smoke: ## Exercise the running API
	$(PY) python scripts/smoke.py

check: lint test ## Run local quality checks
