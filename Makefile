.PHONY: setup lint format format-fix typecheck test test-fast test-unit test-doctest coverage coverage-check security check mutation docs export validate-stdlib clean

# Setup
setup:
	uv sync

# Linting
lint:
	uv run ruff check src/ tests/

format:
	uv run ruff format --check src/ tests/

format-fix:
	uv run ruff format src/ tests/
	uv run ruff check --fix src/ tests/

# Type checking
typecheck:
	uv run ty check src/

# Stdlib-only validation (Gate 0)
validate-stdlib:
	uv run python scripts/validate_stdlib_only.py

# Testing
test:
	uv run pytest

test-fast:
	uv run pytest tests/unit/ -x -q --no-cov

test-unit:
	uv run pytest tests/unit/ -v

test-doctest:
	uv run pytest --doctest-modules src/

# Coverage
coverage:
	uv run pytest --cov-report=html
	@echo "Coverage report: htmlcov/index.html"

coverage-check:
	uv run pytest --cov-fail-under=95

# Security
security:
	uv run bandit -r src/ -ll

# Full quality check (Jidoka 5-gate + stdlib gate)
check: validate-stdlib lint format typecheck security coverage-check
	@echo "All quality gates passed."

# Mutation testing
mutation:
	uv run mutmut run --paths-to-mutate=src/reprorusted_std_only/

# Documentation
docs:
	uv run pdoc -o docs/api src/reprorusted_std_only
	@echo "API documentation generated in docs/api/"

# Export corpus to parquet
export:
	uv run python -m reprorusted_std_only.export_corpus

# Clean
clean:
	rm -rf .pytest_cache .ruff_cache .hypothesis htmlcov .coverage
	rm -rf __pycache__ src/**/__pycache__ tests/**/__pycache__
	rm -rf dist/ build/ *.egg-info
