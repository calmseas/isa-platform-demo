.PHONY: install test run scan fmt

install:
	python3 -m pip install -r requirements.txt

test:
	python3 -m pytest

run:
	python3 -m uvicorn app.main:app --reload

scan:
	python3 security/scan_invisible.py $$(git ls-files '*.md' 'SKILL.md' '**/SKILL.md')

fmt:
	python3 -m ruff check --fix . && python3 -m black .
