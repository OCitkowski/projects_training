Activate

    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip

fastapi

    pip install fastapi
    pip install "uvicorn[standard]"
---
    Go to 
1. http://127.0.0.1:8000/docs
2. http://127.0.0.1:8000/redoc
3. http://127.0.0.1:8000/openapi.json
___

Save to requirements.txt

    pip freeze > requirements.txt
