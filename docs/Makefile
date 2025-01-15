BUILDDIR=build
FILENAME=paper

<command>:
	mkdir $(BUILDDIR) -p
	pandoc $(FILENAME).md \
	--filter pandoc-citeproc \
	--from=markdown+tex_math_single_backslash+tex_math_dollars \

pdf:
	mkdir $(BUILDDIR) -p
	pandoc $(FILENAME).md \
	--filter pandoc-citeproc \
	--from=markdown+tex_math_single_backslash+tex_math_dollars \
	--to=latex \
	--output=$(BUILDDIR)/$(FILENAME).pdf \
	--pdf-engine=xelatex \