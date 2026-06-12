# Bhume Boundary Correction Project

## Overview

This project attempts to improve agricultural land boundaries using simple geospatial correction techniques.

The system reads:
- input.geojson
- satellite imagery
- boundary hints

and generates:
- predictions.geojson

## Approach

The current approach uses:

1. GeoJSON plot loading
2. Polygon translation (small shifts)
3. Confidence-based correction
4. Automatic flagging of uncertain plots

Plots with higher confidence are marked as:
- corrected

Plots with lower confidence are:
- flagged

## Technologies Used

- Python
- GeoPandas
- Shapely
- Rasterio
- Matplotlib

## Current Logic

For each plot:
- Apply a small random shift
- Assign confidence score
- If confidence > 0.7:
  - corrected
- Else:
  - flagged

## Output

The system generates:
- predictions.geojson

## Future Improvements

- Image edge detection
- Better alignment scoring
- Automatic field matching
- ML-based correction