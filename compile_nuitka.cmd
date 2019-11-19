del /f /s /q dist 1>nul
rmdir /s /q dist
mkdir dist

python -m nuitka --follow-imports sshauto.py --standalone --show-progress -j 8 --recurse-all
