[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mlund/KEMM30.git/master)

# KEMM30

Course files for KEMM30. To run this on a remote Jupyter server, click _launch binder_ above.

## Usage (MacOS / Linux)

To open the Notebooks, install python via [Miniconda](https://conda.io/miniconda.html) and
make sure all required packages are loaded by issuing the following terminal commands

``` bash
    conda env create -f environment.yml
    conda activate KEMM30
    jupyter nbextension enable rubberband/main
    jupyter nbextension enable exercise2/main
    jupyter nbextension enable --py widgetsnbextension
    jupyter-notebook
```
