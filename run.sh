#/bin/bash

# Run API
cd part3
source .venv/bin/activate
python run.py &
API_PID=$!

# Run front
cd ../part4
python3 -m http.server 8000 &
FRONT_PID=$!

echo "API launched with PID $API_PID"
echo "Front launched on http://localhost:8000/ with PID $FRONT_PID"

wait
