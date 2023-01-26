import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import plotly.express as px
import plotly.graph_objects as go


base_salario = np.array([[21, 1000], [23, 1100], [27, 1250], [32, 1700], [34, 1500],
                         [38, 3900], [41, 1980], [46, 5100], [
                             48, 5500], [48, 7000],
                         [50, 2500], [53, 3500], [57, 2200], [59, 4100], [60, 6500]])

scaler_salario = StandardScaler()
base_salario = scaler_salario.fit_transform(base_salario)

kmeans_salario = KMeans(n_clusters=3)
kmeans_salario.fit(base_salario)

centroide = kmeans_salario.cluster_centers_
# print(centroide)

scaler_salario.inverse_transform(kmeans_salario.cluster_centers_)

rotulos = kmeans_salario.labels_
print(rotulos)

grafico1 = px.scatter(x=base_salario[:, 0],
                      y=base_salario[:, 1], color=rotulos)
grafico2 = px.scatter(x=centroide[:, 0], y=centroide[:, 1], size=[8, 8, 8])
grafico3 = go.Figure(data=grafico1.data + grafico2.data)
grafico3.show()


# print(base_salario)
