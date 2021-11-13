test_database:
	python3 -m unittest --verbose tests.test_extract tests.test_database

lint:
	pylint *.py