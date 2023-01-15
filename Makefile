all: install lint test

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

lint:
	pylint app.py

test:
	python3 -m unittest discover -s . -p "*_test.py" -v