SHELL := /bin/bash

help:
	@echo "###"
	@echo "# Build targets for Yomogi"
	@echo "###"
	@echo
	@echo "  make build: Builds the fonts and places them in the fonts/ directory"
	@echo

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

venv: venv/touchfile

build: venv
	. venv/bin/activate; gftools builder sources/config.yaml;