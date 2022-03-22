build:
	docker build --tag python-base .
	docker run --rm -v "/${PWD}:/data" python-base
	docker run --rm -v "/${PWD}/dist:/data" blang/latex:ubuntu lualatex resume.tex | tail -n2
