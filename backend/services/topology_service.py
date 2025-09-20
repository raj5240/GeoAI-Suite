import geopandas as gpd
import networkx as nx
from shapely.geometry import LineString, Point

def build_topology(file_path: str):
    
    try:
        gdf = gpd.read_file(file_path)
        G = nx.Graph()
        for idx, row in gdf.iterrows():
            geom = row.geometry
            if geom is None:
                continue
            if isinstance(geom, LineString):
                coords = list(geom.coords)
                for a, b in zip(coords[:-1], coords[1:]):
                    G.add_edge(tuple(a), tuple(b))
            else:
                # If MultiLineString etc.
                try:
                    for part in geom:
                        coords = list(part.coords)
                        for a, b in zip(coords[:-1], coords[1:]):
                            G.add_edge(tuple(a), tuple(b))
                except Exception:
                    continue
        return {"num_nodes": G.number_of_nodes(), "num_edges": G.number_of_edges()}
    except Exception as e:
        return {"error": str(e)}
