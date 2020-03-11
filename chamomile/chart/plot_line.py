# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/chart_plot_line.ipynb (unless otherwise specified).

__all__ = ['PlotLine']

# Cell
from .chart import Chart
from .data_model import construct_categorical_data
from .base_plot import BasePlot

import pandas as pd
from bokeh.io import output_notebook

from bokeh.models.ranges import FactorRange, Range1d
from bokeh.io import show

# Cell
class PlotLine(BasePlot):
    def __init__(self, chart=None, x_axis_type='linear'):
        super().__init__(chart=chart, x_axis_type=x_axis_type)


    def line(self, df = None, x: str = None, y = None, color: str = None, text: str = None, color_order: list=None):
        p = self._chart.figure

        data = df.copy()
        if data[x].dtype == object:
            data[x] = pd.to_datetime(data[x])
            p.xaxis.formatter = self.tick_formater('datetime')

            N = 30

            p.x_range = Range1d(data[x].min() - pd.Timedelta(days=0.1*N), data[x].max() + pd.Timedelta(days=0.1*N))

        p.y_range = Range1d(data[y].min(), data[y].max())
        p.yaxis.formatter = self.tick_formater('integer')
        if isinstance(y, str):
            if color is not None:
                data = pd.pivot_table(data, index=x, columns=color, values=y).reset_index()
                #text_data = pd.pivot_table(data, index=x, columns=color, values=text).reset_index()
                y = df[color].unique()
                #text = df[color].unique()
            else:
                y = [y]
                #text = [text]
            #data = data.merge(text_data)
        elif isinstance(y, list):
            if color is None:
                color = y
            else:
                if not isinstance(color, list) or set(color) != set(y):
                    raise Exception("Wrong set of y and color")

        if color_order is not None:
            y = color_order
        for sy in y:

            p.line(data[x], data[sy], line_width=2, line_color=self.next_color(), legend_label=sy)
        if color:
            p.legend.title = color
        p.legend.location = "top_left"
        p.yaxis.visible=True

        #print(p.yaxis.__dict__())
        print(p.y_range.start)
        return self
