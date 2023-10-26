IMAGE ?= sep-image
IMAGE_TAG ?= latest

.PHONY: venv install format lint test local_launch build run

venv:
	python3 -m venv .venv

install: setup.py
	. ./.venv/bin/activate && \
	pip install --upgrade pip &&\
	pip install .[dev]

format:
	. ./.venv/bin/activate && \
	black .

lint: venv install
	. ./.venv/bin/activate && \
	black --check . && \
	pylint -j 0 --disable=C,W ./src/

test: venv install
	. ./.venv/bin/activate && \
	pytest .

local_launch: venv install
	. .venv/bin/activate && \
	uvicorn --port 8080 --reload src.main:app 

build:
	docker build --tag $(IMAGE):$(IMAGE_TAG) .

push:
	docker push $(IMAGE):$(IMAGE_TAG)

run:
	docker run -p 8080:8080 --rm $(IMAGE):$(IMAGE_TAG)
