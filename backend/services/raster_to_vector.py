import rasterio
import numpy as np
import geopandas as gpd
from shapely.geometry import shape, Polygon, mapping
from rasterio.features import shapes
import json, os

def raster_to_vector_from_tif(tif_path: str, out_geojson: str = "data/generated/generated.geojson", band=1, threshold=None):
    """
    Simple raster-to-vector conversion by thresholding a band and extracting shapes.
    This is a deterministic, non-AI baseline to produce polygons from raster masks.
    """
    try:
        with rasterio.open(tif_path) as src:
            arr = src.read(band)
            
            if threshold is None:
                threshold = float(arr.mean())
            mask = arr > threshold

            transform = src.transform
            results = []
            for geom, val in shapes(mask.astype('uint8'), mask=mask, transform=transform):
                if val == 1:
                    results.append(geom)

        
        geoms = [shape(g) for g in results]
        gdf = gpd.GeoDataFrame(geometry=geoms, crs=src.crs)
        os.makedirs(os.path.dirname(out_geojson), exist_ok=True)
        gdf.to_file(out_geojson, driver="GeoJSON")
        return {"saved": out_geojson, "features": len(gdf)}
    except Exception as e:
        return {"error": str(e)}
