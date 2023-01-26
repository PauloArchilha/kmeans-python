import numpy as np
import plotly.express as px


base_salario = np.array([])


x = [21, 23, 27, 32, 34, 41, 50, 53, 57, 59, 38, 46, 48, 48, 60]
y = [1000, 1100, 1250, 1700, 1500, 1980, 2500,
     3500, 2200, 4100, 3900, 5100, 5500, 7000, 6500]

grafico = px.scatter(x=x, y=y)
grafico.show()

