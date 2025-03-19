#!/bin/bash
echo "Running tests..."

# Exit if any test fails
set -e

# Run unit tests
echo "Running unit tests..."
pytest tests/unit

# Run integration tests
echo "Running integration tests..."
pytest tests/integration

echo "All tests passed successfully!"
