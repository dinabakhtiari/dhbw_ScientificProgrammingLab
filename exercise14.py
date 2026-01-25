import pandas as pd
import numpy as np

def haversine_np(lat1, lon1, lat2, lon2):
    R = 6371.0  
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2) ** 2
    )
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c

city_pairs = pd.DataFrame({
    "City1": ["Tokyo", "Tokyo", "Los Angeles"],
    "City2": ["Los Angeles", "London", "London"],
    "Lat1": [35.6895, 35.6895, 34.0522],
    "Lon1": [139.6917, 139.6917, -118.2437],
    "Lat2": [34.0522, 51.5074, 51.5074],
    "Lon2": [-118.2437, -0.1278, -0.1278],
})

city_pairs["Distance_KM"] = haversine_np(
    city_pairs["Lat1"], city_pairs["Lon1"], 
    city_pairs["Lat2"], city_pairs["Lon2"]
)

print("final reult:")
print(city_pairs[["City1", "City2", "Distance_KM"]])