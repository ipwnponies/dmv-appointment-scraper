.DEFAULT_GOAL := help

.PHONY: help
help:  # Print help
	@grep -E -v -e '^\s' -e '^\.' $(MAKEFILE_LIST) | \
		grep -E '^\S+( \S+)*:.*#' | \
		sort | \
		awk 'BEGIN {FS = ":.*# "}; {printf "\033[1;32m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: run
run: venv ## Run script
	./venv/bin/python -m dmv_appointment_scraper

.PHONY: run_email
run_email: ## Run script and send email output
	./venv/bin/python -m dmv_appointment_scraper --email

.PHONY: venv
venv: requirements.txt requirements-dev.txt ## Create virtualenv
	./bin/venv-update venv= -p python3 venv/ install= -r requirements-dev.txt -r requirements.txt --quiet
	./venv/bin/pre-commit install

.PHONY: clean
clean: ## Clean working directory
	find . -iname '*.pyc' | xargs rm -f
	rm -rf ./venv/
