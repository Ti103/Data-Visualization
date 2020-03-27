import matplotlib.pyplot as plt

x = range(1, 10, 2)
y = [1, 3, 2, 4, 3]

x2 = range(2, 11, 2)
y2 = [6, 7, 8, 9, 10]

titulo = "Scatterplot: grafico de dispersão"
titulo_x = "Eixo X"
titulo_y = "Eixo Y"

plt.title("Titulo do Grafico")
plt.xlabel(titulo_x)
plt.ylabel(titulo_y)

# Plot dispersão
plt.scatter(x, y, label="Meus Pontos", color="r")
plt.scatter(x2, y2, label="Meus outros pontos", color='y', marker='h', s=200)
# Plot de linhas que liga os pontos
plt.plot(x, y)
plt.plot(x2, y2)
plt.legend()
plt.show()
