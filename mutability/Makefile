# Variables
TEX = $(wildcard *.tex)          # Finds all .tex files in the directory
PDF = $(TEX:.tex=.pdf)           # Converts .tex filenames to .pdf

# Default target
all: $(PDF) mutability.zip

# Rule to convert .tex to .pdf
%.pdf: %.tex
	pdflatex -shell-escape $<

mutability.zip : $(PDF)
	rm -rf ./mutability
	mkdir -p ./mutability
	cp -r $(PDF) src exercises ./mutability
	zip -r ./mutability.zip ./mutability

# Clean up auxiliary files
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

# Full clean (includes PDFs)
distclean: clean
	rm -f $(PDF)

# Phony targets
.PHONY: all clean distclean
