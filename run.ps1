# Runs the whole app: starts the FastAPI server, waits for it to be ready,
# then launches the Go CLI. Stops the server automatically when you exit.

Set-Location $PSScriptRoot

# Activate virtual environment
& "$PSScriptRoot\venv\Scripts\Activate.ps1"

# Start the API in the background
$server = Start-Process -FilePath "uvicorn" -ArgumentList "main:app", "--reload" -PassThru -NoNewWindow

# Wait until the server responds
Write-Host "Waiting for API to start..."
while ($true) {
    try {
        Invoke-WebRequest -Uri "http://127.0.0.1:8000/" -UseBasicParsing -ErrorAction Stop | Out-Null
        break
    } catch {
        Start-Sleep -Milliseconds 500
    }
}
Write-Host "API is up."

# Launch the CLI
try {
    Set-Location "$PSScriptRoot\cli"
    go run main.go
} finally {
    Stop-Process -Id $server.Id -ErrorAction SilentlyContinue
}
