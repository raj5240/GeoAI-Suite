from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.vector_service import load_vector_data
from services.raster_service import process_raster_data
from services.topology_service import build_topology

app = FastAPI(title="GeoAI Suite Backend")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "GeoAI Suite Backend Running"}

@app.get("/vector")
def vector_analysis(file_path: str):
    return load_vector_data(file_path)

@app.get("/raster")
def raster_analysis(file_path: str):
    return process_raster_data(file_path)

@app.get("/topology")
def topology_analysis(file_path: str):
    return build_topology(file_path)
