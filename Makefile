# `make` or `make all` will render the Quarto file to Markdown
all:
	quarto render README.qmd

# `make env` will update the Conda/Mamba environment file
env:
	mamba env export --no-builds | grep -v "prefix" > environment.yml
