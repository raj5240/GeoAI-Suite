from backend.services.vector_service import load_vector_data
def test_vector_load():
    res = load_vector_data("data/raw/sample.geojson")
    assert "num_features" in res or "error" in res
