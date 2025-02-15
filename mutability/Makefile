TEX := $(wildcard *.tex)
PDF := $(TEX:.tex=.pdf)
SRC := $(shell find ./src -type f -name "*.py")
EXERCISES := $(shell find ./exercises -type f -name "*.py")
TARGETS := $(PDF) mutability.zip

all: $(TARGETS)

# Rule to convert .tex to .pdf
%.pdf: %.tex
	pdflatex -shell-escape $<

# Rule to build zip file
mutability.zip : $(PDF) $(SRC) $(EXERCISES)
	rm -rf ./mutability
	mkdir -p ./mutability
	cp -r $(PDF) src exercises ./mutability
	zip -r ./mutability.zip ./mutability && rm -rf ./mutability

# Clean up auxiliary files
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

# Full clean
distclean: clean
	rm -f $(TARGETS)

# Phony targets
.PHONY: all clean distclean
