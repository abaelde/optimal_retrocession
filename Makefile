# Makefile for the optimal_retrocession project

.PHONY: concat

# Target to concatenate all LaTeX source files into a single file.
# This is useful for providing the full context to an LLM.
# Usage: make concat
concat:
	@echo "Concatenating LaTeX files into memoire_complet.md..."
	@python3 scripts/concat_latex.py memoire/main.tex memoire_complet.md
	@echo "Done."
