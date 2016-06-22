.PHONY: test coverage browse-coverage clean

test:
	python3 -m unittest

coverage:
	nosetests3 --with-coverage --cover-package=allbase --cover-erase --cover-tests --cover-inclusive --cover-html --cover-branches

browse-coverage: coverage
	xdg-open cover/index.html

clean:
	- rm -rf allbase.egg-info/
	- rm -rf build/
	- rm -rf cover/
	- rm -rf dist/
	- rm -rf allbase/__pycache__/
	- rm -rf test/__pycache__/
