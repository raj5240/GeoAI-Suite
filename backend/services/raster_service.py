import rasterio
import numpy as np

def process_raster_data(file_path: str):
    
    try:
        with rasterio.open(file_path) as src:
            shape = src.shape
            count = src.count
            dtype = str(src.dtypes[0])
        return {"shape": shape, "band_count": count, "dtype": dtype}
    except Exception as e:
        return {"error": str(e)}

def calculate_ndvi(file_path: str, red_band=1, nir_band=2):
    
    try:
        with rasterio.open(file_path) as src:
            red = src.read(red_band).astype("float32")
            nir = src.read(nir_band).astype("float32")
            denom = (nir + red)
            denom[denom == 0] = 1e-6
            ndvi = (nir - red) / denom
        
        return {
            "shape": ndvi.shape,
            "min": float(np.nanmin(ndvi)),
            "max": float(np.nanmax(ndvi)),
            "mean": float(np.nanmean(ndvi))
        }
    except Exception as e:
        return {"error": str(e)}
