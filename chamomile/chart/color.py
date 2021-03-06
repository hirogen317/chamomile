# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/chart_color.ipynb (unless otherwise specified).

__all__ = ['default_palette', 'color_types', 'palette_contrast2', 'palette_compare3', 'BaseColor', 'ColorDefault',
           'ColorContrast2', 'ColorCompare3']

# Cell
from ..util.dotdict import dotdict
from bokeh.palettes import Category20
from bokeh.transform import factor_cmap

# Cell
default_palette = Category20[20]
color_types = dotdict({'stress': default_palette[6], 'background': default_palette[14],
                       'first': default_palette[0], 'second': default_palette[2], 'third': default_palette[4]})
palette_contrast2 = [color_types.stress, color_types.background]
palette_compare3 = [color_types.first, color_types.second, color_types.stress]

# Cell
class BaseColor():
    MODE_LOOP = 'loop'
    MODE_LAST = 'last'
    def __init__(self, palette=palette_contrast2, mode=None):
        self._palette = palette
        if mode is None:
            self._mode = BaseColor.MODE_LOOP
        else:
            self._mode = mode
        self._cursor = 0

    @property
    def palette(self):
        return self._palette

    @property
    def mode(self):
        return self._mode

    def reset(self):
        self._cursor = 0

    def next_color(self):
        color = self.color_by_cursor()
        self._cursor += 1
        #print(color)
        return color

    def current_color(self):
        return self.color_by_cursor()

    def color_by_cursor(self):
        if self._palette is None and len(self._palette) == 0:
            raise Exception("Color not set")
        if self._cursor < len(self._palette):
            return self._palette[self._cursor]
        elif self._cursor >= len(self._palette):
            if self._mode == BaseColor.MODE_LOOP:
                self._cursor = self._cursor % len(self._palette)
                return self._palette[self._cursor]
            elif self._mode == BaseColor.MODE_LAST:
                return self._palette[-1]

class ColorDefault(BaseColor):
    def __init__(self):
        super().__init__(default_palette, BaseColor.MODE_LOOP)


class ColorContrast2(BaseColor):
    def __init__(self):
        super().__init__(palette_contrast2, BaseColor.MODE_LAST)

class ColorCompare3(BaseColor):
    def __init__(self):
        super().__init__(palette_compare3, BaseColor.MODE_LAST)