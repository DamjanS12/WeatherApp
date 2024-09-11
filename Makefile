.PHONY: envsetup envsetup_common envsetup_mac envsetup_linux shell docker-server migrate upgrade downgrade tests tests-report logo

OS := $(shell uname)

ifeq ($(OS),Darwin)  # macOS
envsetup: logo envsetup_mac
else
envsetup: logo envsetup_linux
endif

poetry:
	python3 -m venv .poetry_venv && \
	.poetry_venv/bin/pip install -U pip setuptools && \
	.poetry_venv/bin/pip install poetry==1.6.1 && \
	ln -s $$(realpath .poetry_venv/bin/poetry) ./poetry

.env:
	cp .sample.env .env

envsetup_common: .env
	# Run poetry install
	@./poetry config virtualenvs.in-project true
	@./poetry install
	@./poetry run pre-commit install
	# Build email templates
	@./build-templates.sh

mac_libs:
	brew install graphviz
	# Install pygraphviz with custom include and library paths for graphviz installed by Homebrew
	./poetry run pip install pygraphviz \
    --config-settings=--global-option=build_ext \
    --config-settings=--global-option="-I$(shell brew --prefix graphviz)/include" \
    --config-settings=--global-option="-L$(shell brew --prefix graphviz)/lib"

linux_libs:
	sudo apt install gcc g++ python3-dev graphviz graphviz-dev

envsetup_mac: poetry mac_libs envsetup_common

envsetup_linux: poetry linux_libs envsetup_common

shell: logo
	@./poetry shell

seed: logo
	python -m app.initial_data

generate_openapi_spec: logo
	ENV=dev PYTHONPATH=$(shell pwd) \
	./poetry run python app/core/utils/generate_openapi_spec.py

generate_models_doc: logo
	ENV=dev PYTHONPATH=$(shell pwd) \
	./poetry run python app/core/utils/generate_models_doc.py

generate_models_graph: logo
	ENV=dev PYTHONPATH=$(shell pwd) \
	./poetry run python app/core/utils/generate_models_graph.py

generate_schemas_doc: logo
	ENV=dev PYTHONPATH=$(shell pwd) \
	./poetry run python app/core/utils/generate_schemas_doc.py

generate_test_coverage: logo
	ENV=dev PYTHONPATH=$(shell pwd) \
	./poetry run coverage run -m pytest && ./poetry run coverage report -i && \
	mkdir -p public/coverage && \
	./poetry run coverage report --format=markdown > public/coverage/README.md

docker-server: logo
	docker-compose up -d

k8s-apply: logo
	eval $(minikube docker-env)
	docker build --no-cache -f Dockerfile -t fastapi-boilerplate .
	docker build --no-cache -f Worker.Dockerfile -t fastapi-worker-boilerplate .
	kubectl apply -f k8s/ --recursive

k8s-delete: logo
	kubectl delete -f k8s/ --recursive

migrate: logo
	@read -p "Enter migration message: " message; \
	./poetry run alembic revision --autogenerate -m "$$message"

upgrade: logo
	@./poetry run alembic upgrade head

downgrade: logo
	@./poetry run alembic downgrade -1

reset-database: logo
	@./poetry run alembic downgrade base

tests: logo
	@./poetry run coverage run -m pytest
	@./poetry run coverage html
	@./poetry run coverage report -i #--fail-under=90

tests-report: logo
	@./poetry run coverage report

format: logo
	@./poetry run pre-commit run --all-files

mypy: logo
	@./poetry run pre-commit run mypy -a

templates: logo
	./build-templates.sh

check-lockfile: logo ## Compares lock file with pyproject.toml
	@./poetry check --lock

logo:  ## prints the logo
	@cat logo.txt; echo "\n"
