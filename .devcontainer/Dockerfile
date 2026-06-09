FROM condaforge/miniforge3:latest

# ── Codespaces expects a non-root user called 'vscode' ──
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -s /bin/bash \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        sudo git curl ca-certificates \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# ── Build the conda environment (mamba is faster) ──
COPY environment.yml /tmp/environment.yml
RUN mamba env create -f /tmp/environment.yml \
    && mamba clean --all --yes --force-pkgs-dirs

# ── Activate by default in every shell ──
RUN echo "conda activate esiil-stars" >> /etc/bash.bashrc
ENV CONDA_DEFAULT_ENV=esiil-stars
ENV PATH=/opt/conda/envs/esiil-stars/bin:$PATH

USER $USERNAME
WORKDIR /workspaces
