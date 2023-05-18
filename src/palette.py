# https://sophisticated-palette.streamlit.app/

# dawn sky
import matplotlib as mpl
from cycler import cycler

palette = ['#05050a', '#0a0c12', '#13151f', '#22222e', '#3f4355', '#515162', '#625b6b', '#726470', '#816976', '#946f7b', '#a07781', '#ab7b82', '#b38783', '#c08d85', '#d18f84', '#e19787', '#f7a185', '#feb884', '#fec587', '#ffe7c3']
mpl.rcParams["axes.prop_cycle"] = cycler(color=palette)

# natural

import matplotlib as mpl
from cycler import cycler

palette = ['#0f1a0b', '#1d373b', '#384209', '#47623d', '#4c7405', '#325b6e', '#806002', '#7ca007', '#6f8eb2', '#a1977e', '#428fcc', '#e4a756', '#10a3fc', '#fba612', '#a6bac1', '#47bdf9', '#ffed16', '#f0d899', '#8be2f8', '#dffaec']
mpl.rcParams["axes.prop_cycle"] = cycler(color=palette)

import plotly.io as pio
import plotly.graph_objects as go
pio.templates["sophisticated"] = go.layout.Template(
    layout=go.Layout(
    colorway=['#0f1a0b', '#1d373b', '#384209', '#47623d', '#4c7405', '#325b6e', '#806002', '#7ca007', '#6f8eb2', '#a1977e', '#428fcc', '#e4a756', '#10a3fc', '#fba612', '#a6bac1', '#47bdf9', '#ffed16', '#f0d899', '#8be2f8', '#dffaec']
    )
)
pio.templates.default = 'sophisticated'