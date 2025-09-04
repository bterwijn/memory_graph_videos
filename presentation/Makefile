TEX := $(wildcard *.tex)
PDF := $(TEX:.tex=.pdf)
FIGS := $(shell find ./figures -type f -name "*.png")
SRC := $(shell find ./src -type f -name "*.py")
TARGETS := $(PDF)

all: $(TARGETS)

# Rule to convert .tex to .pdf
%.pdf: %.tex $(SRC) $(FIGS)
	pdflatex -shell-escape $<

# Clean up auxiliary files
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

# Full clean
distclean: clean
	rm -f $(TARGETS)

# Phony targets
.PHONY: all clean distclean
