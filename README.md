# Run service with docker 
1. Navigate under root directory

# Env file for local testing
Create `.env` file in root directory and copy following statments
```
ENV=local
HOST=http://127.0.0.1:8081/
API_NAME=Oolka API Service
VERSION=1.1.0
DB_URL=sqlite:///./sql_app.db
GOOGLE_MAP_API_KEY=XXXXXXXXXXXXXX
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
