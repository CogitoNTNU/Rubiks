#!/bin/bash

# Define colors for better readability
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Initialize status and time variables
ISORT_STATUS=0
BLACK_STATUS=0
PYLINT_STATUS=0
PYTEST_STATUS=0

ISORT_TIME=0
BLACK_TIME=0
PYLINT_TIME=0
PYTEST_TIME=0

DURATION=0

# Function to handle command execution with timing
run_command() {
    local description="$1"
    shift
    local cmd=$*

    echo -e "${GREEN}${description}...${NC}"
    
    # Record start time
    local start_time
    start_time=$(date +%s)
    
    # Execute the command
    $cmd
    local status=$?
    
    # Record end time
    local end_time
    end_time=$(date +%s)
    
    # Calculate duration
    DURATION=$((end_time - start_time))
    
    if [ $status -ne 0 ]; then
        echo -e "${RED}${description} failed with status ${status}. (Time: ${DURATION}s)${NC}"
    else
        echo -e "${GREEN}${description} completed successfully in ${DURATION}s.${NC}"
    fi
    
    return $status 
}

# Change to the backend directory
cd ./backend || { echo -e "${RED}Failed to navigate to ./backend directory.${NC}"; exit 1; }

echo -e "${GREEN}Starting automated code checks...${NC}"

# 1. Sort imports with isort
run_command "Running isort to sort imports" poetry run isort . --quiet
ISORT_STATUS=$?
ISORT_TIME=$DURATION

# 2. Format code with black
run_command "Running black to format code" poetry run black . --quiet
BLACK_STATUS=$?
BLACK_TIME=$DURATION

# 3. Lint code with pylint
run_command "Running pylint to lint code" poetry run pylint ./**/*.py --rcfile=pyproject.toml --disable=all --enable=E,F
PYLINT_STATUS=$?
PYLINT_TIME=$DURATION

# 4. Run tests with pytest (Uncomment if needed)
# run_command "Running pytest to execute tests" "poetry run pytest -"
# PYTEST_STDURATION# PYTEST_TIME=$DURATION

echo -e "\n${GREEN}Automated code checks completed.${NC}\n"

# Summary function
Summary_element() {
    local status=$1
    local time=$2
    local description=$3
    
    if [ $status -eq 0 ]; then
        echo -e "${GREEN}- ${description}: Passed in ${time}s${NC}"
    else
        echo -e "${RED}- ${description}: Failed in ${time}s${NC}"
    fi
}

# Summary of results
echo -e "${GREEN}Summary:${NC}"
Summary_element $ISORT_STATUS $ISORT_TIME "isort"
Summary_element $BLACK_STATUS $BLACK_TIME "black"
Summary_element $PYLINT_STATUS $PYLINT_TIME "pylint"

# pytest Summary (Uncomment if needed)
# Summary_element $PYTEST_STATUS $PYTEST_TIME "pytest"

# Overall status
if [ $ISORT_STATUS -eq 0 ] && [ $BLACK_STATUS -eq 0 ] && [ $PYLINT_STATUS -eq 0 ]; then
    echo -e "\n${GREEN}All checks passed successfully!${NC}"
    exit 0
else
    echo -e "\n${RED}Some checks failed. Please review the errors above.${NC}"
    exit 1
fi
