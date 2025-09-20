import geopandas as gpd
import rasterio
import numpy as np
import os
from utils.file_ops import list_files, ensure_dir

PROCESSED_DIR = "data/processed"
GENERATED_DIR = "data/generated"

def generate_raster_calculation(file_path: str, output_path: str):
    """Simple NDVI-like calculation (fake for demo)."""
    with rasterio.open(file_path) as src:
        band = src.read(1).astype("float32")
        norm = (band - band.min()) / (band.max() - band.min() + 1e-6)
        profile = src.profile
        ensure_dir(os.path.dirname(output_path))
        with rasterio.open(output_path, "w", **profile) as dst:
            dst.write(norm, 1)
    print(f"Generated raster → {output_path}")

def digitize_vector(file_path: str, output_path: str):
    """Mock AI digitizer: add centroid points."""
    gdf = gpd.read_file(file_path)
    gdf["centroid"] = gdf.centroid
    gdf_out = gdf.copy()
    gdf_out.set_geometry("centroid", inplace=True)
    ensure_dir(os.path.dirname(output_path))
    gdf_out.to_file(output_path)
    print(f"Generated vector (digitized) → {output_path}")

def run_generation():
    vector_files = list_files(PROCESSED_DIR, extensions=[".shp", ".geojson"])
    raster_files = list_files(PROCESSED_DIR, extensions=[".tif", ".tiff"])

    for rf in raster_files:
        out = os.path.join(GENERATED_DIR, "ndvi_" + os.path.basename(rf))
        generate_raster_calculation(rf, out)

    for vf in vector_files:
        out = os.path.join(GENERATED_DIR, "digitized_" + os.path.basename(vf))
        digitize_vector(vf, out)

if __name__ == "__main__":
    run_generation()
