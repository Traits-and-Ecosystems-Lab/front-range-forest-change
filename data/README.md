# Data Directory

This folder stores **small** exported files only (CSVs, summary tables, small GeoJSONs).

**Do NOT commit large rasters here.** All raster data is accessed server-side via Google Earth Engine. The `.gitignore` blocks `.tif`, `.nc`, and other large formats.

If you need to save an intermediate result, keep it under 10 MB and use descriptive filenames:

```
forest_cover_by_elevation_1985_2023.csv
front_range_aoi.geojson
```
