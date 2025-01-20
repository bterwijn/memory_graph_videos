# Variables
TEX = $(wildcard *.tex)          # Finds all .tex files in the directory
PDF = $(TEX:.tex=.pdf)           # Converts .tex filenames to .pdf

# Default target
all: $(PDF)

# Rule to convert .tex to .pdf
%.pdf: %.tex
	pdflatex -shell-escape $<

# Clean up auxiliary files
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

# Full clean (includes PDFs)
distclean: clean
	rm -f $(PDF)

# Phony targets
.PHONY: all clean distclean
