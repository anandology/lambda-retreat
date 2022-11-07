.PHONY: build deploy

build:
	ln -sf $(PWD)/website /var/www/anandology.com/lambda-retreat
	./venv/bin/mkdocs build

deploy:
	ssh -A anandology.com make --directory lambda-retreat git-pull build

git-pull:
	git pull

init:
	python3 -m venv venv
	./venv/bin/pip install -U pip
	./venv/bin/pip install -r requirements.txt