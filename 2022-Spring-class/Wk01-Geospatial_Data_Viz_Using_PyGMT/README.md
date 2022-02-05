## Geospatial Data Visualization using PyGMT
This notebook has been created for the BSL talk on Feb 02, 2022 at McCone Hall, University of California, Berkeley

## Install libraries

### Using python env
```
python -m venv geoviz
source geoviz/bin/activate
pip install pygmt
```

- Try:
```
python -c "import pygmt"
```
if there's no `ImportError`, then you are good to go.

__NOTE:__
If there's any pygmt import problem, install GMT separately and link the `libgmt.dylib` file to the file python is looking for!

- One way to install GMT is `conda install gmt -c conda-forge`

```
ln -s ~/miniconda3/envs/boxgmt/lib/libgmt.dylib ~/miniconda3/envs/geoviz/lib/libgmt.dylib
```

### Using conda env (recommended)
```
conda create --name geoviz --channel conda-forge pandas pygmt jupyter notebook
```
