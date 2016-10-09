.PHONY: debug run development clean

run: virtualenv_run
	python ./src/dmv.py

debug: virtualenv_run
	python -m pudb ./src/dmv.py

virtualenv_run: requirements.txt requirements-dev.txt
	bin/venv-update venv= -p python3.5 virtualenv_run install= -r requirements-dev.txt

development: virtualenv_run
	virtualenv_run/bin/pre-commit autoupdate
	virtualenv_run/bin/pre-commit install

clean:
	find . -iname '*.pyc' | xargs rm -f
	rm -rf ./virtualenv_run
