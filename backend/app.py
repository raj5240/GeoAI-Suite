from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from services.vector_service import load_vector_data, save_vector
from services.raster_service import process_raster_data, calculate_ndvi
from services.topology_service import build_topology
from services.raster_to_vector import raster_to_vector_from_tif

app = FastAPI(title="GeoAI Suite Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "GeoAI Suite Backend Running"}

@app.get("/vector/info")
def vector_info(file_path: str):
    return load_vector_data(file_path)

@app.post("/vector/upload")
async def upload_vector(file: UploadFile = File(...)):
    contents = await file.read()
    # Save under data/raw
    out_path = f"../data/raw/{file.filename}"
    with open(out_path, "wb") as f:
        f.write(contents)
    return {"saved": out_path}

@app.get("/raster/ndvi")
def raster_ndvi(file_path: str):
    return calculate_ndvi(file_path)

@app.get("/raster/process")
def raster_stats(file_path: str):
    return process_raster_data(file_path)

@app.get("/raster2vector")
def raster_to_vector(file_path: str, output_geojson: str = "generated.geojson"):
    return raster_to_vector_from_tif(file_path, output_geojson)

@app.get("/topology")
def topology(file_path: str):
    return build_topology(file_path)
