#!/bin/bash
# Runs the whole app: starts the FastAPI server, waits for it to be ready,
# then launches the Go CLI. Stops the server automatically when you exit.

set -e
cd "$(dirname "$0")"
source venv/bin/activate

# Start the API in the background
uvicorn main:app --reload &
SERVER_PID=$!

# Make sure the server is killed when this script exits (Ctrl-C, CLI quit, etc.)
trap "kill $SERVER_PID 2>/dev/null" EXIT

# Wait until the server responds before starting the CLI
echo "Waiting for API to start..."
until curl -s http://127.0.0.1:8000/ >/dev/null 2>&1; do
  sleep 0.5
done
echo "API is up."

# Launch the CLI in the foreground
cd cli && go run main.go
