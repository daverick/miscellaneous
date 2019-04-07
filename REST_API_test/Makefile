NS ?= daverick
VERSION ?= 1

IMAGE_NAME ?= api-verse

.PHONY: test build run API-test

build:
	docker build -t $(NS)/$(IMAGE_NAME):$(VERSION) -f Dockerfile .

run:
	docker run --rm -p 5000:5000 --name $(IMAGE_NAME)-$(VERSION) $(NS)/$(IMAGE_NAME):$(VERSION)

API-test:
	docker run --rm -p 6000:5000 --name $(IMAGE_NAME)-$(VERSION)-api-test $(NS)/$(IMAGE_NAME):$(VERSION)  &
	sleep 1
	-docker run  --rm -v "`pwd`":/usr/app -w /usr/app daverick/pytest pytest test/API --tb=short
	docker kill $(IMAGE_NAME)-$(VERSION)-api-test

test:
	docker run  --rm -v "`pwd`":/usr/app -w /usr/app daverick/pytest pytest test/API


build-and-run: build run
