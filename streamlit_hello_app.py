import streamlit as st
import numpy as np
import pandas as pd

st.title('Hello World!')
st.balloons()

# highlight some elements in a table
st.title('Highlight some elements in a interactive table')
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

# display data points on a map
st.title('Display data points on a map')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
