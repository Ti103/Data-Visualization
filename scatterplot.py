import matplotlib.pyplot as plt

x = range(1, 10, 2)
y = [1, 3, 2, 4, 3]

x2 = range(2, 11, 2)
y2 = [6, 7, 8, 9, 10]

titulo = "Scatterplot: grafico de dispersão"
eixo_x = "Eixo X"
eixo_y = "Eixo Y"

plt.title("Titulo do Grafico")
plt.xlabel(eixo_x)
plt.ylabel(eixo_y)

# Plot dispersão
plt.scatter(x, y, label="Meus Pontos", color="r")
plt.scatter(x2, y2, label="Meus outros pontos")
# Plot de linhas que liga os pontos
plt.plot(x, y)
plt.legend()
plt.show()
