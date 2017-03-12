.PHONY: run_email run clean

run: virtualenv_run
	./virtualenv_run/bin/python -m dmv_appointment_scraper

run_email:
	./virtualenv_run/bin/python -m dmv_appointment_scraper --email

virtualenv_run: requirements.txt requirements-dev.txt
	bin/venv-update venv= -p python3 virtualenv_run install= -r requirements-dev.txt
	virtualenv_run/bin/pre-commit autoupdate
	virtualenv_run/bin/pre-commit install

clean:
	find . -iname '*.pyc' | xargs rm -f
	rm -rf ./virtualenv_run
