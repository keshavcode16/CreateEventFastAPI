# Run service with docker 
1. Navigate under root directory

# Env file for local testing
Create `.env` file in root directory and copy following statments
```
ENV=local
REDIS_HOST=localhost
REDIS_PORT=6379
LOCAL_DB_URL=sqlite:///./sql_app.db
REFERENCE_SERVICE_URL=http://127.0.0.1:9000/
PROCESS_SERVICE_URL=http://127.0.0.1:9001/
```

# Run the following commands to build and up the docker containers in detach mode
2. docker compose -f docker-compose.yml up --build -d --remove-orphans
# Another way to install it locally
```
python -m venv projectenv
source projectenv/bin/activate  
cd CreateEventFastAPI/
pip install -r requirements.txt
uvicorn app.main:app --port=8081 --host 0.0.0.0
```

# To Run test cases just run below command
```
pytest
```

# Run fastapi swagger on browser
 - http://0.0.0.0:8000/docs
