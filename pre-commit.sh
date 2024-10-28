#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define colors for better readability
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

cd ./backend
echo -e "${GREEN}Starting automated code checks...${NC}"

# 1. Sort imports with isort
echo -e "${GREEN}Running isort to sort imports...${NC}"
poetry run isort . --quiet
echo -e "${GREEN}isort completed successfully.${NC}"

# 2. Format code with black
echo -e "${GREEN}Running black to format code...${NC}"
poetry run black . --quiet
echo -e "${GREEN}black formatting completed successfully.${NC}"

# 3. Lint code with pylint
echo -e "${GREEN}Running pylint to lint code...${NC}"
# You can specify directories or files; here, it's set to the current directory
poetry run pylint ./**/*.py  --rcfile=pyproject.toml --disable=all --enable=E,F
echo -e "${GREEN}pylint completed successfully.${NC}"

# # 4. Run tests with pytest
# echo -e "${GREEN}Running pytest to execute tests...${NC}"
# poetry run pytest -
# echo -e "${GREEN}pytest completed successfully.${NC}"

echo -e "${GREEN}All checks passed successfully!${NC}"
