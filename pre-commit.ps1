# Define colors and symbols
$GREEN = "`e[32m"
$RED = "`e[31m"
$YELLOW = "`e[33m"
$NC = "`e[0m" # No Color
$CHECK_MARK = [char]0x2714 # ✓
$CROSS_MARK = [char]0x2718 # ✘

# Initialize status and time variables
$STATUS = @{}
$TIME_TAKEN = @{}

# Function to display usage
function Show-Usage {
    Write-Host "Usage: ./script.ps1 [options]"
    Write-Host "Options:"
    Write-Host "  --all           Run all checks (default)"
    Write-Host "  --format        Run formatting checks only (isort, black)"
    Write-Host "  --isort         Run isort only"
    Write-Host "  --black         Run black only"
    Write-Host "  --pylint        Run pylint only"
    Write-Host "  --pytest        Run pytest only"
    Write-Host "  --help          Display this help message"
}

# Parse command-line arguments
$CHECKS = @()
if ($args.Count -eq 0) {
    $CHECKS = @("isort", "black")
} else {
    foreach ($arg in $args) {
        switch ($arg) {
            '--all' { $CHECKS = @("isort", "black", "pylint", "pytest") }
            '--format' { $CHECKS = @("isort", "black") }
            '--isort' { $CHECKS += "isort" }
            '--black' { $CHECKS += "black" }
            '--pylint' { $CHECKS += "pylint" }
            '--pytest' { $CHECKS += "pytest" }
            '--help' { Show-Usage; exit 0 }
            default { Write-Host "${RED}Unknown option: ${arg}${NC}"; Show-Usage; exit 1 }
        }
    }
}

# Remove duplicates
$CHECKS = $CHECKS | Select-Object -Unique

# Function to handle command execution with timing
function Invoke-Command {
    param (
        [string]$Tool,
        [string]$Description,
        [string]$Cmd
    )

    Write-Host "$YELLOW$Description...${NC}"
    
    # Record start time
    $startTime = Get-Date
    
    # Execute the command
    Invoke-Expression $Cmd
    $status1 = $LASTEXITCODE
    
    # Record end time
    $endTime = Get-Date
    
    # Calculate duration
    $duration = [math]::Round(($endTime - $startTime).TotalSeconds, 2)
    
    # Display result
    Write-Host "${YELLOW}Finished in ${duration}s ${NC}"
    
    $STATUS[$Tool] = $status1
    $TIME_TAKEN[$Tool] = $duration
}

# Change to the backend directory
try {
    Set-Location -Path "./backend"
} catch {
    Write-Host "${RED}Failed to navigate to ./backend directory.${NC}"
    exit 1
}

Write-Host "${GREEN}================================${NC}"
Write-Host "${GREEN} Starting Automated Code Checks ${NC}"
Write-Host "${GREEN}================================${NC}`n"

# Execute selected checks
foreach ($check in $CHECKS) {
    switch ($check) {
        "isort" { Invoke-Command -Tool "isort" -Description "Running isort to sort imports" -Cmd "poetry run isort . --quiet" }
        "black" { Invoke-Command -Tool "black" -Description "Running black to format code" -Cmd "poetry run black . --quiet" }
        "pylint" { Invoke-Command -Tool "pylint" -Description "Running pylint to lint code" -Cmd "poetry run pylint ./**/*.py --rcfile=pyproject.toml --disable=all --enable=E,F" }
        "pytest" { Invoke-Command -Tool "pytest" -Description "Running pytest to execute tests" -Cmd "poetry run pytest" }
    }
}

Write-Host "`n${GREEN}================================${NC}"
Write-Host "${GREEN}    Automated Checks Summary    ${NC}"
Write-Host "${GREEN}================================${NC}"

# Summary of results
$allPassed = $true
foreach ($tool in $CHECKS) {
    if ($STATUS[$tool] -eq 0) {
        Write-Host "${GREEN}${CHECK_MARK}  ${tool}: Passed in $($TIME_TAKEN[$tool])s${NC}"
    } else {
        Write-Host "${RED}${CROSS_MARK}  ${tool}: Failed in $($TIME_TAKEN[$tool])s${NC}"
        $allPassed = $false
    }
}

# Change back to the original directory
Set-Location -Path ".."

# Final Status
if ($allPassed) {
    Write-Host "`n${GREEN}All selected checks passed successfully!${NC}"
    exit 0
} else {
    Write-Host "`n${RED}Some checks failed. Please review the errors above.${NC}"
    exit 1
}
