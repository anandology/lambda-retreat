.PHONY: build deploy

build:
	ln -sf $(PWD)/website /var/www/anandology.com/lambda-retreat
	mkdocs build

deploy:
	ssh anandology.com bash -c 'cd lambda-retreat && git pull && make build'