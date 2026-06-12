# Bhume Boundary Correction Project

## Overview

This project is developed for the Bhume geospatial boundary correction challenge.

The system loads:
- GeoJSON plot boundaries
- Satellite imagery (.tif)
- Boundary hints

It performs:
- Plot visualization
- Boundary correction
- Confidence-based prediction
- GeoJSON output generation

---

## Technologies Used

- Python
- GeoPandas
- Rasterio
- Matplotlib
- GeoJSON

---

## Workflow

1. Load agricultural plot boundaries
2. Load satellite imagery
3. Visualize land parcels
4. Detect shifted boundaries
5. Correct confident plots
6. Flag uncertain plots
7. Export predictions.geojson

---

## Output

The system generates:
- predictions.geojson

---

## Current Logic

- High confidence plots are corrected
- Low confidence plots are flagged
- Simple boundary shifting is used as baseline correction

---

## Future Improvements

- ML-based alignment
- Edge detection
- Automatic boundary extraction
- Deep learning segmentation

---

## Author

Chegireddy Venkata Mukhesh Reddy