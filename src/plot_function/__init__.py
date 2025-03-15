import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec

from IPython.display import display


def find_desc(df_desc, tag):
    columns = df_desc.columns.tolist()
    s = df_desc[columns[0]].apply(lambda x: str(x)).str.contains(tag)
    for c in columns[1:]:
        s += df_desc[c].apply(lambda x: str(x)).str.contains(tag)
    display(df_desc[s])


class plot_generator:

    def __init__(self, df_descricao):
        df_descricao.index = df_descricao['NovoNome']
        df_descricao['unit'] = df_descricao['Unidade']
        df_descricao['name'] = df_descricao['Descrição']

        self.dict_desc = df_descricao.to_dict(orient='index')
        self.fig = None
        self.axes = []

    def time_series(self, data_frame, list_tag_main):

        axs = self.create_axs()

        for n, tag in enumerate(list_tag_main):
            label, color = self.get_tag_features(tag)
            color = color if color else f'C{n}'
            axs.plot(data_frame[tag], label=label, color=color)

        if len(list_tag_main) > 1:
            axs.legend(loc=2, framealpha=1)

        else:
            axs.set_ylabel(label)

        self.fix_dimensions()
        axs.grid()

    def create_axs(self):
        if not self.fig:
            self.fig = plt.figure()
            axs = self.fig.add_subplot(1, 1, 1)

        else:
            axs = self.fig.add_subplot(1, 1, 1, sharex=self.axes[0])

        self.axes.append(axs)
        return axs

    def get_tag_features(self, tag):
        if tag in self.dict_desc:
            unit = self.dict_desc[tag].get('unit', '')
            name = self.dict_desc[tag].get('name', tag)
            label = f'{name} ({unit})' if unit else name

            color = self.dict_desc[tag].get('color', None)

        else:
            unit, name, label, color = '', tag, tag, None

        return label, color

    def fix_dimensions(self):
        nrow = len(self.axes)
        gs = gridspec.GridSpec(nrow, 1)

        for i, ax in enumerate(self.axes):
            ax.set_position(gs[i].get_position(self.fig))
            ax.set_subplotspec(gs[i])

        self.fig.set_size_inches(12, 3 * nrow)
        self.fig.tight_layout()
