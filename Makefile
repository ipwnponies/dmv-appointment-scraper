.PHONY: debug
debug: virtualenv_run
	python -m pudb ./src/dmv.py

virtualenv_run: requirements.txt
	bin/venv-update venv= -p python3.5 virtualenv_run install= -r requirements.txt
