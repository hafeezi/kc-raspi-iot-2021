# RASPBERRY PI IOT WORKSHOP BY KINABALU CODERS

## PYTHON TEMPERATURE WEB APPLICATION DEMO

### SETUP INSTRUCTIONS

1. Create virtual environment `python3 -m venv env`
2. Activate environment `source ./env/bin/activate` (Linux/Raspberry Pi) or `.\env\Scripts\activate.bat` (Windows Command Prompt) or `.env\Scripts\activate.ps1` (Windows PowerShell)
3. Install required Pip Packages `pip3 install -r requirements.txt`
4. Set the path for FLASK_APP `set FLASK_APP=app` (Windows Command Prompt) or `$env:FLASK_APP="app"` (Windows PowerShell) or `export FLASK_APP=app` (Linux/Raspberry Pi Terminal)
5. Run the server `flask run` (Only Accessible on the same machine)
6. Run the server to public `flask run --host=0.0.0.0`