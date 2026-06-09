# Project Guide: Getting Started

Welcome to the Front Range Forest Change project! This guide covers the essentials: how to open your workspace, where to put things, and how to save your work.

---

## Opening Your Codespace

1. Go to our repo on GitHub (your mentor will share the link).
2. Click the green **`<> Code`** button → **Codespaces** tab → **Create codespace on main**.
3. Wait 1–2 minutes (first time takes longer — it's building your Python environment).
4. You'll see VS Code in your browser. The terminal at the bottom should show ✅ Environment ready.

**To reopen an existing Codespace:** Go to [github.com/codespaces](https://github.com/codespaces) and click on your Codespace. Don't create a new one each time!

---

## Where Things Go

```
front-range-forest-change/
│
├── notebooks/        ← Your analysis notebooks go here
├── scripts/          ← Shared helper functions (utils.py)
├── tutorials/        ← Learning materials (you are here!)
├── data/             ← Small exported CSVs and tables only
├── figures/          ← Saved plots and maps (PNG, 300 dpi)
└── README.md         ← Project overview
```

**Rules of thumb:**
- Write your analysis code in `notebooks/`.
- Save figures to `figures/` using `plt.savefig('figures/my_plot.png', dpi=300, bbox_inches='tight')`.
- The `data/` folder is for small files only (CSVs, GeoJSONs). We access all large raster data through Google Earth Engine — no downloading needed.
- Don't modify files in `scripts/utils.py` without checking with your teammates first — everyone imports from it.

---

## Saving Your Work with Git

Think of Git as a "save checkpoint" system. Every time you reach a working state, you save a checkpoint (called a **commit**) that you and your team can always go back to.

### The three commands you'll use most

Open the **Terminal** at the bottom of VS Code (or press `` Ctrl+` ``):

```bash
git add .                          # Stage all your changes
git commit -m "Add NDVI analysis"  # Save a checkpoint with a message
git push                           # Upload to GitHub so others can see it
```

**Commit messages should be short and descriptive.** Say *what* you did, not *that* you did something.

| ✅ Good | ❌ Bad |
|---------|--------|
| "Add NLCD visualization for 2001 and 2021" | "Updated notebook" |
| "Fix elevation band boundaries" | "Changes" |
| "Add figures for presentation" | "Stuff" |

---

## Branches: Keeping Main Clean

**`main` is the team's shared, working copy.** Think of it as the "clean room" — only code that runs without errors and is ready for your teammates should go here.

**A branch is your personal workspace.** You can experiment, break things, and iterate without affecting anyone else.

### When to use a branch

- You're trying something new and aren't sure it'll work.
- You're working on a feature that takes more than one sitting.
- You want feedback before merging into main.

### When to commit directly to main

- Small, safe changes (fixing a typo, adding a comment).
- You've tested the code and it runs end-to-end.

### How to use a branch

```bash
# Create and switch to your branch
git checkout -b maria-ndvi-analysis

# Work, commit, push as normal
git add .
git commit -m "Draft NDVI time series"
git push -u origin maria-ndvi-analysis

# When ready, open a Pull Request on GitHub
# Your mentor will review and merge it into main
```

**Branch naming:** Use your name + what you're working on.
Examples: `james-dem-analysis`, `alex-nlcd-timeseries`, `maria-figures`.

### Getting updates from main

When a teammate's work gets merged into main:

```bash
git checkout main        # Switch to main
git pull                 # Get the latest changes
git checkout my-branch   # Go back to your branch
git merge main           # Bring main's updates into your branch
```

---

## Quick Reference

| I want to... | Command |
|---|---|
| See what I've changed | `git status` |
| Save my work | `git add .` → `git commit -m "message"` → `git push` |
| Create a branch | `git checkout -b name-feature` |
| Switch branches | `git checkout branch-name` |
| Go back to main | `git checkout main` |
| Get teammates' updates | `git pull` |
| Open a notebook | Click any `.ipynb` file in the left sidebar |

---

**When in doubt, ask!** It's much easier to fix a Git problem early than after several commits. If you see a merge conflict or something unexpected, message your mentor before trying to resolve it.
