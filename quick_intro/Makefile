TEX := $(wildcard *.tex)
PDF := $(TEX:.tex=.pdf)
FIGS := $(shell find ./figures -type f -name "*.png")
SRC := $(shell find ./src -type f -name "*.py")
TARGETS := $(PDF) quick_intro.zip

all: $(TARGETS)

# Rule to convert .tex to .pdf
%.pdf: %.tex $(SRC) $(FIGS)
	pdflatex -shell-escape $<

# Rule to build zip file
quick_intro.zip : $(PDF) $(SRC)
	rm -rf ./quick_intro
	mkdir -p ./quick_intro
	cp -r $(PDF) src ./quick_intro
	zip -r ./quick_intro.zip ./quick_intro && rm -rf ./quick_intro

# Clean up auxiliary files
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

# Full clean
distclean: clean
	rm -f $(TARGETS)

# Phony targets
.PHONY: all clean distclean
