# Project Guide: Getting Started

Hello team! This guide covers the essentials: how to open your workspace, where to put things, and how to save your work using the VS Code interface in your browser-based Codespace.

---

## Opening Your Codespace

1. Go to our repo on GitHub.
2. Click the green **`<> Code`** button.
3. Open the **Codespaces** tab.
4. Click **Create codespace on main**.
5. Wait 1-2 minutes (first launch can take longer).
6. VS Code opens in your browser and loads the project.

**Notebook environment check (important):**
When you open a notebook, use the kernel picker in the top-right and choose **`esiil-stars (Python 3.11.15)`**. Do **not** choose **`base`**.

**To reopen an existing Codespace:** Go to [github.com/codespaces](https://github.com/codespaces) and click your existing Codespace. Do not create a new one each session unless you mean to start fresh.

Please turn off existing codespace usage, e.g. your ESIIL workshop tutorials.

---

## Where Things Go

```
front-range-forest-change/
|
|-- notebooks/        <- Your analysis notebooks go here
|-- scripts/          <- Shared helper functions (utils.py)
|-- tutorials/        <- Learning materials (you are here)
|-- data/             <- Small exported CSVs and tables only
|-- figures/          <- Saved plots and maps (PNG, 300 dpi)
`-- README.md         <- Project overview
```

**Rules of thumb:**
- Write analysis work in `notebooks/`. **Keep your notebooks short. I noticed adding too many cells overwhelms codespace.**
- Save figures to `figures/` (example: `my_plot.png`, 300 dpi).
- Keep only small files in `data/` (CSV, GeoJSON, small tables).
- Do not modify `scripts/utils.py` without checking with teammates first.

---

## Saving Your Work (GUI-Only Git Workflow)

Think of Git as a checkpoint system. In VS Code, you can do this entirely through the Source Control panel.

### How to commit and push from the interface

1. Click the **Source Control** icon in the left sidebar (branch icon).
2. Review changed files under **Changes**.
3. Click a file to preview the diff.
4. Click the **+** next to each file (or **Stage All Changes**) to stage.
5. Type a short commit message in the message box at the top.
6. Click **Commit & Push** (small drop down arrow besides commit button). This directly syncronizes changes into the github. Alternatively you can do this step by step by clicking **Commit** and then clicking **Sync Changes** (or **Push**) to upload to GitHub.

If this is your first commit on a new branch, VS Code may show **Publish Branch** instead of Push. Click it.

**Commit messages should be short and descriptive.** Say what changed.

| Good | Bad |
|---|---|
| "Add NLCD visualization for 2001 and 2021" | "Updated notebook" |
| "Fix elevation band boundaries" | "Changes" |
| "Add figures for presentation" | "Stuff" |

---

## Branches: Keeping Main Clean

**`main` is the shared stable branch.** Keep it clean and working.

**A branch is your personal workspace.** Use branches for experiments and in-progress work.

### When to use a branch

- You are trying something new.
- Work will take more than one session.
- You want review before merging.

### When direct commits to main are okay

- Very small safe edits (for example, typo fixes).
- You have tested and confirmed everything runs.

### Create and use a branch in the GUI

1. Click the branch name in the lower-left status bar (for example, `main`).
2. Select **Create new branch...**
3. Name it using `yourname-topic` (example: `malia-ndvi-analysis`).
4. Make edits and commit from Source Control.
5. Click **Publish Branch** (first time) or **Sync Changes**.
6. Open a Pull Request from the GitHub panel or the PR prompt in VS Code when it appears.

---

## Staying Synced When You Are Behind

You will sometimes see messages like **"Your branch is behind"** or an indicator that incoming changes exist.

### Case 1: Your local `main` is behind remote `main`

1. Switch to `main` using the branch picker in the lower-left.
2. In Source Control, click **Sync Changes** or open **...** menu -> **Pull**.
3. Wait for completion, then confirm no incoming changes remain.

### Case 2: Your feature branch is behind because `main` advanced

1. Switch to `main` and pull/sync latest updates.
2. Switch back to your feature branch.
3. Open the Command Palette (`Ctrl+Shift+P`) and choose **Git: Merge Branch...**
4. Select `main` to merge latest `main` into your branch.
5. If conflicts appear, use the merge editor buttons (**Accept Current**, **Accept Incoming**, or **Accept Both**), then complete the merge commit.
6. Click **Sync Changes** to push your updated branch.

This keeps your branch up to date before opening or updating a Pull Request.

---

## Quick GUI Reference

| I want to... | In VS Code browser UI |
|---|---|
| See what changed | Open **Source Control** and review **Changes** |
| Save work to GitHub | Stage -> Commit -> **Sync Changes** |
| Create a branch | Click branch name in status bar -> **Create new branch...** |
| Switch branches | Click branch name in status bar -> select branch |
| Update local main | Switch to `main` -> **Sync Changes** or **Pull** |
| Bring main updates into my branch | Switch back to your branch -> **Git: Merge Branch...** -> choose `main` |
| Open a notebook | Click any `.ipynb` file in the Explorer |

---

When something looks confusing (especially merge conflicts), ask early. It is much easier to fix Git issues right away than after many commits.
