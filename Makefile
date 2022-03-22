build:
	docker build --tag python-base .
	docker run --rm -v "/${PWD}:/data" python-base
	docker run --rm -v "/${PWD}/dist:/data" blang/latex:ubuntu lualatex resume.tex | tail -n2

present:
	docker run --rm --init -v ${PWD}/docs:/home/marp/app -e LANG=$LANG -p 8080:8080 -p 37717:37717 marpteam/marp-cli -s .
