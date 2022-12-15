SOURCES=$(wildcard *.wat)
TARGETS=$(SOURCES:%.wat=%.wasm)

WAT2WASM=docker run \
	--rm -it \
	-v $(PWD):/app  \
	--entrypoint /opt/wabt/bin/wat2wasm \
	anandology/wast

default: $(TARGETS)

%.wasm: %.wat
	$(WAT2WASM) $<
