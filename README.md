[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/luchem/KEMM30.git/master)
<a target="_blank" href="https://colab.research.google.com/github/luchem/KEMM30/blob/master/lectures/01-introduction.ipynb">
<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

# KEMM30

Course files for KEMM30.

## Running

There are three ways to run the notebooks:

1. **Conda** — create and activate the `KEMM30` environment as described in [Using the Conda environment](#using-the-conda-environment).
2. **uv** — create the project environment with `uv sync` and launch JupyterLab as described in [Using the uv environment](#using-the-uv-environment).
3. **Google Colab** — open a notebook using the Colab badge at the top of this page, as described in [Using Google Colab](#using-google-colab).

## Usage without environment

The first (lecture) notebooks only use the standard scientific packages and you can start working directly.
only for the last notebook you will need an additional package that you can install from within any notebook
with `!pip install lmfit` (and then restart the kernel to use it)

For the project notebooks you will need a number of extra packages. If you run from within any notebook this
command you will install the in one go your installation folder (or the user folder in case of lacking rights)

`!pip install lmfit ipympl lxml nglview ipywidgets brewer2mpl rdkit ffmpeg nmrglue`.

## Usage with environment

### Using the `uv` environment (recommended for local install)

First install `uv` by following instructions
[here](https://docs.astral.sh/uv/getting-started/installation/).
Then, go to the KEMM30 directory in a terminal and type:

```bash
uv sync
uv run jupyter lab
```

### Using the Conda environment

At Lund installing an environement is very slow. So we recommend to install only the minimum using conda and then
install the rest via pip. To do this run the following commands:

```bash
conda env create -f environment_mini.yml
conda activate KEMM30
pip install lmfit ipympl lxml nglview ipywidgets brewer2mpl rdkit ffmpeg nmrglue
jupyter nbextension enable rubberband/main
jupyter nbextension enable exercise2/main
jupyter nbextension enable --py widgetsnbextension
jupyter-notebook
```

At home you can install all packages automatically. Install python via [Miniconda](https://conda.io/miniconda.html)
or the full anaconda from [Anaconda](https://www.anaconda.com/download) and
then make sure all required packages are loaded by issuing the following terminal commands:

```bash
conda env create -f environment.yml
conda activate KEMM30
jupyter nbextension enable rubberband/main
jupyter nbextension enable exercise2/main
jupyter nbextension enable --py widgetsnbextension
jupyter-notebook
```

The before each usage you must "activate" the environment by typing `activate KEMM30`.

### Using Google Colab

Open the desired notebook in Google Colab using the Colab badge at the top of this page, or upload a notebook manually. Colab provides a temporary Python environment, so run the notebook's Colab setup cells before starting the analysis. The project notebooks are located in [`projects/`](projects/).
