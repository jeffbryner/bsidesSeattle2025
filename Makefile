.PHONY: all clean

all: slides.html

slides.html: slides.md
	pandoc -t revealjs -s slides.md -o slides.html \
	--variable theme=black \
	--variable transition=slide \
	--variable revealjs-url=https://unpkg.com/reveal.js \
	--variable controls=true \
	--variable progress=true \
	--variable hash=true

clean:
	rm -f slides.html
