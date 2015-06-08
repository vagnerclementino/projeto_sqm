NAME=proj_sqm_vagner_clementino
BIBLIOGRAPHY=./bib/proposta-ref.bib
DIR_PDF_NAME=.
all: aspell compile clean
compile: $(NAME).tex #$(BIBLIOGRAPHY).bib	
	@pdflatex -shell-escape $(NAME).tex
	@bibtex $(NAME)
	@pdflatex $(NAME).tex
	@pdflatex $(NAME).tex
	@evince $(NAME).pdf
	@echo Gerado o arquivo $(NAME).pdf no diretório $(DIR_PDF_NAME)
clean:
	@rm ${NAME}.aux ${NAME}.blg ${NAME}.bbl ${NAME}.dvi ${NAME}.ps ${NAME}.log ${NAME}.toc ${NAME}.out ${NAME}.nav ${NAME}.snm ${NAME}.synctex.gz
aspell: $(NAME).tex
	aspell --encoding="utf-8" -c -t=tex --lang="pt_BR" $(NAME).tex
