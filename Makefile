run-server:
	poetry run python core/manage.py runserver


migrations:
	poetry run python core/manage.py makemigrations


migrate:
	poetry run python core/manage.py migrate


shell:
	poetry run python core/manage.py shell

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run

.PHONY: test
test:
	poetry run python core/manage.py test

.PHONY: flake8
flake8:
	 flake8 .

