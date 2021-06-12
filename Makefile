#
# Copyright (C) 2021 Kian Cross
#

COVERAGE_CMD=poetry run coverage
COVERAGE_FILE=.coverage

.PHONY: test
test:
	rm -rf $(COVERAGE_FILE)
	$(COVERAGE_CMD) run --include "cpair/*" -m unittest tests
	$(COVERAGE_CMD) report -m

.PHONY: coverage
coverage:
	$(COVERAGE_CMD) xml

.PHONY: fix-style
fix-style:
	poetry run black .

.PHONY: check-style
check-style:
	poetry run black . --check

.PHONY: lint
lint:
	poetry run mypy --strict cpair
