# LabelMyTextWidget

LabelMyTextWidget is an iPythonWidget to quickly label text data.

This goal of this project is to speed up and simplify the process of manual labeling.

The widget provides a minimalist interface to review each row of a pandas dataframe and apply a label to it.

![GIF showing the widget](https://github.com/tchambon/LabelMyTextWidget/blob/master/LabelMyTextWidget.gif "GIF Widget")


## How to use the widget

A Jupyter notebook is at the root of the repository, and it contains an example.

## How to install it

For the time being, you have to download the folder LabelMyTextWidget and put it in your project folder.
Better installation options and packaging will come soon.


## Dependancy 

A python environnement with Jupyter notebook, pandas and numpy is required.
The best is to use the Anaconda distribution with Python 3.

Besides that, the following should be installed:

```shell
pip install ipywidgets

jupyter nbextension enable --py widgetsnbextension
```