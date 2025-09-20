import React, { useEffect } from "react";
import 'leaflet/dist/leaflet.css';
import { MapContainer, TileLayer, GeoJSON } from "react-leaflet";

export default function MapViewer(){
  const [geojson, setGeojson] = React.useState(null);

  useEffect(()=> {
   
    fetch("/data/generated/sample.geojson").then(res=>{
      if(res.ok) return res.json()
      else return null
    }).then(js=>{
      if(js) setGeojson(js)
    }).catch(()=>{})
  },[])

  return (
    <MapContainer center={[20.5937,78.9629]} zoom={5} style={{height:"100vh"}}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      {geojson && <GeoJSON data={geojson} />}
    </MapContainer>
  );
}
