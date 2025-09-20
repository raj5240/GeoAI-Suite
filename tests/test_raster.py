from backend.services.raster_service import process_raster_data
def test_raster():
    res = process_raster_data("data/raw/sample.tif")
    assert "shape" in res or "error" in res
