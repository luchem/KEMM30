[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/luchem/KEMM30.git/master)
<a target="_blank" href="https://colab.research.google.com/github/luchem/KEMM30/blob/master/lectures/01-introduction.ipynb">
<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

# KEMM30

Course files for KEMM30.

## Running

Pick one of these methods. The `uv` approach installs a Python environment on your
computer and can be used independently of any web service.

### Using Google Colab in a Web Browser

Open the desired notebook in [Google Colab](https://colab.research.google.com)
using the Colab badge at the top of this page, or upload a notebook manually.
Colab provides a temporary Python environment, so run the notebook's Colab setup cells before starting the analysis. The project notebooks are located in [`projects/`](projects/).

### Using the `uv` - recommended for local install

First install `uv` by following the instructions
[here](https://docs.astral.sh/uv/getting-started/installation/).
Then, in a terminal:

```bash
cd KEMM30/
uv sync
uv run jupyter lab
```

