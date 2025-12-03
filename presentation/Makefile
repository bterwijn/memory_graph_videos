TEX := $(wildcard *.tex)
PDF := $(TEX:.tex=.pdf)
FIGS := $(shell find ./figures -type f -name "*.png")
SRC := $(shell find ./src -type f -name "*.py")
TARGETS := $(PDF)

DIA  = $(shell find -name '*.dia')
EPS  = $(patsubst %.dia,%.eps,$(DIA))
PDFS = $(patsubst %.dia,%.pdf,$(DIA))


all: $(PDFS) $(TARGETS)

# Rule to convert .tex to .pdf
%.pdf: %.tex $(SRC) $(FIGS)
	pdflatex -shell-escape $<

%.pdf: %.eps
	epstopdf $<

%.eps: %.dia
	dia --export $@ $<


# Clean up auxiliary files
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

# Full clean
distclean: clean
	rm -f $(TARGETS)

# Phony targets
.PHONY: all clean distclean
