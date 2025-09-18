import geopandas as gpd
from shapely.geometry import mapping
import os

def load_vector_data(file_path: str):
    
    try:
        gdf = gpd.read_file(file_path)
        return {
            "crs": str(gdf.crs),
            "columns": list(gdf.columns),
            "num_features": int(len(gdf))
        }
    except Exception as e:
        return {"error": str(e)}

def save_vector(gdf, out_path: str):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    gdf.to_file(out_path, driver="GeoJSON")
    return out_path
