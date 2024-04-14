#!/bin/bash

# Удаление файлов внутри папки output

# OUTPUT_DIR="output"
# if [ -d "$OUTPUT_DIR" ]; then
#   rm -f "$OUTPUT_DIR"/*
# fi

# Запуск тестов
pytest -s -v tests/*