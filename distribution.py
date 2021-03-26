import pandas as pd
import plotly.figure_factory as ff

data = pd.read_csv("distributionData.csv")

graph = ff.create_distplot([data["Avg Rating"].tolist()], ["Avg Rating"])
graph.show()