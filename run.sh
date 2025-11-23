#!/bin/bash

# Quit if command fail
set -e

# Check OS
if grep -qi "debian" /etc/os-release; then
  os="debian"
  echo "OS -> Debian"
elif grep -qi "arch" /etc/os-release; then
  os="arch"
  echo "OS -> Arch"
else
  os="other"
  echo "OS -> Other"
fi

# Check package manager
if command -v uv &> /dev/null; then
  package="uv"
  echo "PM -> uv"
elif command -v pip &> /dev/null; then
  package="pip"
  echo "PM -> pip"
else
  package="other"
  echo "PM -> Other"
fi

# Back-end folder
cd part3

# Check and setup package manager
if [ "$package" = "uv" ]; then
  uv sync
  source .venv/bin/activate
elif [ "$package" = "pip" ]; then
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
else
  echo "Nor pip or uv was found, installation in progress ..."
  echo "Install pip and uv ..."
  if [ "$os" = "debian" ]; then
    sudo apt install -y python3-pip
    pip install uv
  elif [ "$os" = "arch" ]; then
    sudo pacman -S --noconfirm python-pip
    pip install uv
  else
    echo "Distribution not supported. Please, install pip or uv manually."
    exit 1
  fi
  # Reload script after install
  exec "$0"
fi

# Run API
echo "Launch API ..."
python run.py &
API_PID=$!

# Run front
cd ../part4
echo "Launch front server ..."
python3 -m http.server 8000 &
FRONT_PID=$!

echo ""
echo "═══════════════════════════════════════"
echo "API launched with PID $API_PID"
echo "Front launched on http://localhost:8000/ with PID $FRONT_PID"
echo "═══════════════════════════════════════"
echo ""

# Cleanup on exit
trap "kill $API_PID $FRONT_PID 2>/dev/null; echo 'Services stopped'" EXIT

wait
