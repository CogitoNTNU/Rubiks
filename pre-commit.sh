#!/bin/bash

# Define colors and symbols
GREEN='\033[32m'
RED='\033[31m'
YELLOW='\033[33m'
NC='\033[0m' # No Color
CHECK_MARK="\xE2\x9C\x94" # ✓
CROSS_MARK="\xE2\x9C\x98" # ✘

# Initialize status and time variables
declare -A STATUS
declare -A TIME_TAKEN

# Function to display usage
usage() {
    echo -e "Usage: $0 [options]"
    echo -e "Options:"
    echo -e "  --all           Run all checks (default)"
    echo -e "  --format        Run formatting checks only (isort, black)"
    echo -e "  --isort         Run isort only"
    echo -e "  --black         Run black only"
    echo -e "  --pylint        Run pylint only"
    echo -e "  --pytest        Run pytest only"
    echo -e "  --help          Display this help message"
}

# Function to hide the cursor
hide_cursor() {
    tput civis
}

# Function to show the cursor
show_cursor() {
    tput cnorm
}

# Function to handle cleanup on exit or interrupt
cleanup() {
    show_cursor
    echo -e "\n${RED}Script interrupted. Exiting...${NC}"
    exit 1
}

# Trap signals to ensure the cursor is shown again
trap cleanup SIGINT SIGTERM

# Parse command-line arguments
CHECKS=()
if [ $# -eq 0 ]; then
    CHECKS=("isort" "black" )
else
    for arg in "$@"; do
        case $arg in
            --all)
                CHECKS=("isort" "black" "pylint" "pytest")
                ;;
            --format)
                CHECKS=("isort" "black")
                ;;
            --isort)
                CHECKS+=("isort")
                ;;
            --black)
                CHECKS+=("black")
                ;;
            --pylint)
                CHECKS+=("pylint")
                ;;
            --pytest)
                CHECKS+=("pytest")
                ;;
            --help)
                usage
                exit 0
                ;;
            *)
                echo -e "${RED}Unknown option: $arg${NC}"
                usage
                exit 1
                ;;
        esac
    done
fi

# Remove duplicates
mapfile -t CHECKS < <(printf "%s\n" "${CHECKS[@]}" | sort -u)

# Function to handle command execution with timing
run_command() {
    local tool="$1"
    local description="$2"
    local cmd="$3"

    echo -e "${YELLOW}${description}...${NC}"
    
    # Record start time
    local start_time
    start_time=$(date +%s)
    
    # Execute the command
    eval "$cmd"
    local status=$?
    
    # Record end time
    local end_time
    end_time=$(date +%s)
    
    # Calculate duration
    local duration=$((end_time - start_time))
    
    # Display result
   echo -e "${YELLOW}Finished in ${duration}s${NC}"
    
    STATUS["$tool"]=$status
    TIME_TAKEN["$tool"]=$duration
}

# Change to the backend directory
cd ./backend || { echo -e "${RED}Failed to navigate to ./backend directory.${NC}"; exit 1; }

echo -e "${GREEN}================================${NC}"
echo -e "${GREEN} Starting Automated Code Checks ${NC}"
echo -e "${GREEN}================================${NC}\n"

# Execute selected checks
for check in "${CHECKS[@]}"; do
    case $check in
        isort)
            run_command "isort" "Running isort to sort imports" "poetry run isort . --quiet"
            ;;
        black)
            run_command "black" "Running black to format code" "poetry run black . --quiet"
            ;;
        pylint)
            run_command "pylint" "Running pylint to lint code" "poetry run pylint ./**/*.py --rcfile=pyproject.toml --disable=all --enable=E,F"
            ;;
        pytest)
            run_command "pytest" "Running pytest to execute tests" "poetry run pytest"
            ;;
    esac
done

echo -e "\n${GREEN}================================${NC}"
echo -e "${GREEN}    Automated Checks Summary    ${NC}"
echo -e "${GREEN}================================${NC}"

# Summary of results
ALL_PASSED=true
for tool in "${CHECKS[@]}"; do
    if [ "${STATUS[$tool]}" -eq 0 ]; then
        echo -e "${GREEN}${CHECK_MARK}  ${tool}: Passed in ${TIME_TAKEN[$tool]}s${NC}"
    else
        echo -e "${RED}${CROSS_MARK}  ${tool}: Failed in ${TIME_TAKEN[$tool]}s${NC}"
        ALL_PASSED=false
    fi
done

# Final Status
if $ALL_PASSED ; then
    echo -e "\n${GREEN}All selected checks passed successfully!${NC}"
    exit 0
else
    echo -e "\n${RED}Some checks failed. Please review the errors above.${NC}"
    exit 1
fi
