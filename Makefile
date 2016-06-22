.PHONY: test

test:
	python3 -m unittest

coverage:
	nosetests3 --cover-erase --with-coverage --cover-branch --cover-html --cover-inclusive
