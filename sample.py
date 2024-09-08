import streamlit as st
import pandas as pd
import sqlite3

import plotly.express as px
from streamlit_plotly_events import plotly_events


st.title('Sample Streamlit App')

st.write('This is a sample Streamlit app.')

# df = pd.read_csv("./aggreagted_data.csv")


conn = sqlite3.connect('aggregated_data.db')

df = pd.read_sql_query("SELECT * FROM aggregated_data", conn)

conn.close()

selected_wafer_name = st.selectbox('Select a wafer', df['wID'].unique())

# st.dataframe(df)


# ヒートマップの作成 (x と y に対して pf を可視化)
# fig = px.density_heatmap(df, x='x', y='y', z='pf', color_continuous_scale='Viridis')
fig = px.density_heatmap(df[df["wID"] == selected_wafer_name], x='x', y='y', z='pf', color_continuous_scale='Viridis')
# st.plotly_chart(fig)

selected_points = plotly_events(fig, click_event=True, hover_event=False)

# クリックされたセルの x, y の値を表示
if selected_points:
    clicked_point = selected_points[0]  # 最初のクリックイベントの情報
    st.write(clicked_point)
    # st.write(f"Clicked x: {clicked_point['x']}, y: {clicked_point['y']}")
    # ここで他のアクションを定義できます（例えば、x, y 値をコピーなど）
