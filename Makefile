# Makefile for the optimal_retrocession project

.PHONY: concat latex

# Target to concatenate all LaTeX source files into a single file.
# This is useful for providing the full context to an LLM.
# Usage: make concat
concat:
	@echo "Concatenating LaTeX files into memoire_complet.md..."
	@python3 scripts/concat_latex.py memoire/main.tex memoire_complet.md
	@echo "Done."

# Target to compile the LaTeX document.
# Usage: make latex
latex:
	@echo "Compiling LaTeX document..."
	@cd memoire && pdflatex main.tex
	@echo "Done."
