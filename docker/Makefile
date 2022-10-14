.DEFAULT_GOAL := help
HOST_NAME=$(shell if [ "$(FQN)" = "" ]; then echo $$(hostname); else echo $(FQN); fi)
CONTAINER_NAME=dmasif
CONTAINER_NAME_TEMP=$(CONTAINER_NAME)_temp

CONTAINER_TAG=$(shell echo $(CONTAINER_NAME):0.1)
DMASIF_SRC=$(realpath .)
SRC_ROOT?=$(DMASIF_SRC)/../../predict-interaction-patches/
DATA_ROOT?=$(DMASIF_SRC)/../../predict-interaction-patches/preprocessing/npys/
MOUNTS=-v $(SRC_ROOT):/MaSIF_colab/mycode -v $(DATA_ROOT):/MaSIF_colab/preprocessed_data/
DOCKER_CMD=docker
PYTHON_CMD=python

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


run: ## run container production mode
	$(DOCKER_CMD) run --name $(CONTAINER_NAME) -it \
		$(MOUNTS) \
		$(CONTAINER_TAG)

run_tests_training:
	$(DOCKER_CMD) exec --name $(CONTAINER_NAME) sh benchmark/dMaSIF_search.sh

run_tests_inference:
	$(DOCKER_CMD) exec --name $(CONTAINER_NAME) $(PYTHON_CMD) main_inference.py

build: ## build container
	$(DOCKER_CMD) build . -t $(CONTAINER_TAG)

logs: ## view logs of a local Docker container
	$(DOCKER_CMD) logs -f $(CONTAINER_NAME)

stop: ## stop the local docker cotnainer
	$(DOCKER_CMD) stop $(CONTAINER_NAME)

clean_containers: ## clean the containers
	$(DOCKER_CMD) container rm $(CONTAINER_NAME)

inspect: ## inspect the Docker container
	@$(DOCKER_CMD) exec -it $(CONTAINER_NAME) /bin/bash
