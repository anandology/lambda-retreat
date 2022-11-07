.PHONY: build deploy

build:
	ln -sf $(PWD)/website /var/www/anandology.com/lambda-retreat
	mkdocs build

deploy:
	ssh -A anandology.com make --directory lambda-retreat git-pull build

git-pull:
	git pull
