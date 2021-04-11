#!/bin/sh

echo "This is automated script for run python flask creation"  
echo ""
py -m venv env
echo ""
echo "Wait for 5 seconds"
echo ""
sleep 5
cd env/Scripts
./activate.bat
cd ../..
echo ""
pip install flask
echo ""
read -p "Create a .py file: " file
echo "
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'" > "$file"
echo ""
read -p "Enter app filename e.g app.py: " filename
set FASK_APP=$filename
export FASK_APP=$filename
echo "FASK_APP has been set to $filename"
echo ""
echo "After completing writing code run this -> python -m flask run"
echo ""
python -m flask run