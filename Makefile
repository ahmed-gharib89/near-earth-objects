test_database:
	python3 -m unittest --verbose tests.test_extract tests.test_database

test_query:
	python3 -m unittest --verbose tests.test_query tests.test_limit

test:
	python3 -m unittest --verbose

lint:
	pylint *.py