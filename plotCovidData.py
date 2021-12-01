import pandas as pd
import plotly.express as px

DF = pd.read_csv("CovidData.csv")
figure = px.scatter(DF, x = "date", y = "cases", color = "country")
figure.show()