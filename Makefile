.PHONY: debug run clean
run: virtualenv_run
	python ./src/dmv.py

debug: virtualenv_run
	python -m pudb ./src/dmv.py

virtualenv_run: requirements.txt
	bin/venv-update venv= -p python3.5 virtualenv_run install= -r requirements.txt

clean:
	find . -iname '*.pyc' | xargs rm -f
	rm -rf ./virtualenv_run
