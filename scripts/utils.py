"""
Shared utility functions for the Front Range Forest Change project.
Import in any notebook with: from scripts.utils import *
"""

import ee
import geemap
import pandas as pd
import matplotlib.pyplot as plt


# ── Study Area ────────────────────────────────────────────────────────
# Front Range bounding box (approximate)
# Covers the foothills from ~Colorado Springs to ~Fort Collins
FRONT_RANGE_BBOX = ee.Geometry.Rectangle([-105.7, 38.8, -104.8, 40.7])

# Elevation range for the analysis (meters)
ELEV_MIN = 1500
ELEV_MAX = 2800
ELEV_BAND_WIDTH = 100  # meters per band

# NLCD time range
YEAR_START = 1985
YEAR_END = 2023


# ── NLCD Class Definitions ────────────────────────────────────────────
# Grouped into broad categories for cleaner analysis
NLCD_FOREST_CLASSES = [41, 42, 43]       # Deciduous, Evergreen, Mixed
NLCD_DEVELOPED_CLASSES = [21, 22, 23, 24] # Open, Low, Med, High intensity
NLCD_GRASSLAND_CLASSES = [71]             # Grassland/Herbaceous
NLCD_SHRUB_CLASSES = [52]                 # Shrub/Scrub
NLCD_AG_CLASSES = [81, 82]               # Pasture/Hay, Cultivated Crops

NLCD_BROAD_GROUPS = {
    'Forest': NLCD_FOREST_CLASSES,
    'Developed': NLCD_DEVELOPED_CLASSES,
    'Grassland': NLCD_GRASSLAND_CLASSES,
    'Shrub': NLCD_SHRUB_CLASSES,
    'Agriculture': NLCD_AG_CLASSES,
}

# Colors matching the standard NLCD palette
NLCD_COLORS = {
    'Forest': '#1c6330',
    'Developed': '#e8544e',
    'Grassland': '#e3d28e',
    'Shrub': '#ccb879',
    'Agriculture': '#ab7028',
    'Other': '#b3b3b3',
}


# ── Helper Functions ──────────────────────────────────────────────────

def get_elevation_bands(dem, geometry, min_elev, max_elev, band_width):
    """
    Create a list of elevation-band geometries within an AOI.

    Parameters
    ----------
    dem : ee.Image
        Digital elevation model (e.g., USGS/3DEP/10m).
    geometry : ee.Geometry
        Area of interest.
    min_elev : int
        Lower elevation bound (m).
    max_elev : int
        Upper elevation bound (m).
    band_width : int
        Width of each elevation band (m).

    Returns
    -------
    list of dict
        Each dict has 'elev_low', 'elev_high', and 'mask' (ee.Image).
    """
    bands = []
    for low in range(min_elev, max_elev, band_width):
        high = low + band_width
        mask = dem.gte(low).And(dem.lt(high)).selfMask()
        bands.append({
            'elev_low': low,
            'elev_high': high,
            'mask': mask,
        })
    return bands


def classify_nlcd_broad(nlcd_image):
    """
    Reclassify an NLCD image into broad land-cover groups.

    Parameters
    ----------
    nlcd_image : ee.Image
        Single-year NLCD land cover image.

    Returns
    -------
    ee.Image
        Reclassified image with values 1=Forest, 2=Developed,
        3=Grassland, 4=Shrub, 5=Agriculture, 0=Other.
    """
    lc = nlcd_image.select('landcover')

    forest = lc.remap(NLCD_FOREST_CLASSES,
                       [1] * len(NLCD_FOREST_CLASSES), 0)
    developed = lc.remap(NLCD_DEVELOPED_CLASSES,
                          [2] * len(NLCD_DEVELOPED_CLASSES), 0)
    grassland = lc.remap(NLCD_GRASSLAND_CLASSES,
                          [3] * len(NLCD_GRASSLAND_CLASSES), 0)
    shrub = lc.remap(NLCD_SHRUB_CLASSES,
                      [4] * len(NLCD_SHRUB_CLASSES), 0)
    ag = lc.remap(NLCD_AG_CLASSES,
                   [5] * len(NLCD_AG_CLASSES), 0)

    return forest.max(developed).max(grassland).max(shrub).max(ag) \
        .rename('broad_class')


def set_plot_style():
    """Apply a clean matplotlib style for presentation figures."""
    plt.rcParams.update({
        'figure.figsize': (10, 6),
        'figure.dpi': 150,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'font.size': 12,
        'axes.titlesize': 14,
        'axes.labelsize': 12,
    })
