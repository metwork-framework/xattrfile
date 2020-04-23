doc:
	rm -Rf html
	pdoc --html xattrfile

clean:
	rm -Rf html htmlcov
	rm -Rf xattrfile.egg-info
	find . -type d -name __pycache__ -exec rm -Rf {} \; 2>/dev/null || exit 0

test: clean
	pytest tests/

coverage:
	pytest --cov-report html --cov=xattrfile tests/
	pytest --cov=xattrfile tests/
