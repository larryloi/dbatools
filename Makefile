#!make
include RELEASE
export $(shell sed 's/=.*//' RELEASE)
#IMAGE := docker-repos:8123/i2/cnfas:0.2.37
#IMAGE := cnfas:0.2.3
#CONTAINER := cnfas
#APP_SRC_PATH := $(realpath ../)
WORKDIR := ./
#ENV_FILE := bundler.env
SSHKEY_PATH := /root/.ssh

build:
	docker build -f Dockerfile ${WORKDIR} -t ${REPO_PATH}$(IMAGE):$(TAG) || make bash IMAGE=$$(docker images -aq | head -1)

push:
	docker push ${REPO_PATH}${IMAGE}:${TAG}

image.rm:
	docker rmi $$(docker images|grep ${REPO_PATH}${IMAGE} | grep ${TAG} |head -1 |awk '{print $$3}')


