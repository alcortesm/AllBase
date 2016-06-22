.PHONY: test, coverage, clean

test:
	python3 -m unittest

coverage:
	nosetests3 --cover-erase --with-coverage --cover-branch --cover-html --cover-inclusive

browse-coverage:
	xdg-open cover/index.html

clean:
	- rm -rf allbase.egg-info/
	- rm -rf build/
	- rm -rf cover/
	- rm -rf dist/
	- rm -rf allbase/__pycache__/
	- rm -rf test/__pycache__/
