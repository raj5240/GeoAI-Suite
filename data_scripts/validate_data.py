import geopandas as gpd
import rasterio
from utils.file_ops import list_files

PROCESSED_DIR = "data/processed"

def validate_vector(file_path: str):
    gdf = gpd.read_file(file_path)
    if gdf.crs is None or gdf.crs.to_epsg() != 4326:
        print(f"[WARNING] {file_path} CRS is not EPSG:4326")
    else:
        print(f"[OK] {file_path} valid CRS")

def validate_raster(file_path: str):
    with rasterio.open(file_path) as src:
        if src.width <= 0 or src.height <= 0:
            print(f"[ERROR] {file_path} invalid dimensions")
        else:
            print(f"[OK] {file_path} valid raster")

def run_validation():
    vector_files = list_files(PROCESSED_DIR, extensions=[".shp", ".geojson"])
    raster_files = list_files(PROCESSED_DIR, extensions=[".tif", ".tiff"])

    for vf in vector_files:
        validate_vector(vf)
    for rf in raster_files:
        validate_raster(rf)

if __name__ == "__main__":
    run_validation()
