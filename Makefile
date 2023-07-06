.PHONY: run mypy build

run-python:
	python main.py

run:
	python -c "import main"

mypy:
	mypy main.py

build:
	mypyc main.py

compile:
	pyinstaller --onedir --noconsole --noconfirm --clean main.py
	move dist\main\main.exe main.exe

clear:
	if exist build (rmdir /s /q build)
	if exist dist (rmdir /s /q dist)
	if exist *.spec (del /q *.spec)
	if exist *.pyd (del /q *.pyd)
	if exist *.exe (del /q *.exe)

clear-full: clear
	if exist .mypy_cache (rmdir /s /q .mypy_cache)
	if exist .vscode (rmdir /s /q .vscode)
