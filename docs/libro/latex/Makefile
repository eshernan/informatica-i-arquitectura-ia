TEX=pdflatex
JOB=Libro_Informatica_I_2026

.PHONY: all clean

all:
	mkdir -p build/chapters
	$(TEX) -interaction=nonstopmode -halt-on-error -jobname=$(JOB) -output-directory=build main.tex
	$(TEX) -interaction=nonstopmode -halt-on-error -jobname=$(JOB) -output-directory=build main.tex
	$(TEX) -interaction=nonstopmode -halt-on-error -jobname=$(JOB) -output-directory=build main.tex

clean:
	rm -f build/*.aux build/*.log build/*.out build/*.toc build/*.lof build/*.lot
