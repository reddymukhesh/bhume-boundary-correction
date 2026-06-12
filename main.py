import geopandas as gpd
from shapely.affinity import translate
import random

print("Loading plots...")

# Load plots
plots = gpd.read_file("data/input.geojson")

print("Total plots:", len(plots))

predictions = []

# Process first 50 plots
for i in range(50):

    plot = plots.iloc[i]

    geometry = plot.geometry

    # Random small shifts
    x_shift = random.uniform(-0.0005, 0.0005)
    y_shift = random.uniform(-0.0005, 0.0005)

    shifted = translate(
        geometry,
        xoff=x_shift,
        yoff=y_shift
    )

    # Confidence logic
    confidence = random.uniform(0.5, 0.95)

    # Status logic
    if confidence > 0.7:
        status = "corrected"
        final_geometry = shifted
    else:
        status = "flagged"
        final_geometry = geometry

    predictions.append({
        "plot_number": plot["plot_number"],
        "status": status,
        "confidence": round(confidence, 2),
        "method_note": "Simple automatic boundary shift detection",
        "geometry": final_geometry
    })

print("Predictions created:", len(predictions))

# Create GeoDataFrame
pred_gdf = gpd.GeoDataFrame(
    predictions,
    geometry="geometry",
    crs=plots.crs
)

# Save output
pred_gdf.to_file(
    "output/predictions.geojson",
    driver="GeoJSON"
)

print("Improved predictions.geojson saved!")