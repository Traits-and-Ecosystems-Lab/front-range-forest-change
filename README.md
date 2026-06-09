# Front Range Forest Cover Change Along an Elevation Gradient (1985–2023)

**ESIIL STARS 2026 · Traits and Ecosystems Lab**

## Research Question

How has forest cover changed in Colorado's Front Range along an elevation gradient over 39 years, and to what extent are these changes associated with climate-driven shifts and urbanization?

## Study Area

Colorado Front Range foothills — from the eastern plains (~1,500 m) through the montane zone (~2,800 m), spanning the forest–grassland ecotone and the expanding urban corridor.

## Datasets

| Dataset | Source | Resolution | Access |
|---------|--------|-----------|--------|
| NLCD Annual Land Cover | USGS/MRLC | 30 m, 1985–2023 | GEE: `USGS/NLCD_RELEASES/2021_REL/NLCD` |
| 3DEP Digital Elevation Model | USGS | 10 m | GEE: `USGS/3DEP/10m` |
| gridMET Climate | UofI | 4 km daily | GEE: `IDAHO_EPSCOR/GRIDMET` |

## Quick Start

1. **Open in Codespaces** — Click the green `<> Code` button → `Codespaces` → `Create codespace on main`. The environment builds automatically (~5–8 min on first launch).
2. **Authenticate to GEE** — Open `notebooks/00-setup-gee-auth.ipynb` and run the authentication cell.
3. **Start exploring** — Work through the notebooks in order (00 → 01 → 02 → 03).

## Project Structure

```
├── .devcontainer/          # Codespace environment config
│   ├── devcontainer.json
│   └── Dockerfile
├── environment.yml         # Conda package list
├── notebooks/              # Analysis notebooks (one per pipeline stage)
│   ├── 00-setup-gee-auth.ipynb
│   ├── 01-data-acquisition.ipynb
│   ├── 02-elevation-analysis.ipynb
│   └── 03-visualization.ipynb
├── scripts/                # Shared helper functions
│   └── utils.py
├── data/                   # Small exported CSVs / tables only
├── figures/                # Saved plots for presentation
└── README.md
```

## Team

| Role | Name | Focus |
|------|------|-------|
| Faculty Mentor | Saif | Project design, code review |
| Intern 1 | TBD | Data acquisition & AOI definition |
| Intern 2 | TBD | NLCD change analysis by elevation |
| Intern 3 | TBD | Visualization & climate context |

## Lab

[Traits and Ecosystems Lab](https://traitsandecosystems.com/) · ESIIL · CU Boulder / CIRES

## License

This project is developed for educational purposes under the ESIIL STARS 2026 program.
