# Setup instructions (Linux)

1. Clone repo:
   git clone https://github.com/<your>/GeoAI-Suite.git
   cd GeoAI-Suite

2. Backend:
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r ../requirements.txt
   uvicorn app:app --reload --host 0.0.0.0 --port 8000

3. Frontend:
   cd frontend
   npm install
   npm start

4. Data:
   Put input rasters and vectors under data/raw/
