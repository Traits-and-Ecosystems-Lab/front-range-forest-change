FROM condaforge/miniforge3:latest

# ── Codespaces expects a non-root user called 'vscode' ──
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN existing_group="$(getent group "$USER_GID" | cut -d: -f1 || true)" \
    && if ! id -u "$USERNAME" >/dev/null 2>&1; then \
        if getent passwd "$USER_UID" >/dev/null; then \
            existing_user="$(getent passwd "$USER_UID" | cut -d: -f1)"; \
            usermod --login "$USERNAME" --move-home --home "/home/$USERNAME" --shell /bin/bash "$existing_user"; \
        else \
            if [ -z "$existing_group" ]; then \
                groupadd --gid "$USER_GID" "$USERNAME"; \
                existing_group="$USERNAME"; \
            fi; \
            useradd --uid "$USER_UID" --gid "$existing_group" -m "$USERNAME" -s /bin/bash; \
        fi; \
    fi \
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
