import matplotlib.pyplot as plt

x = range(1, 10, 2)
y = [1, 3, 2, 4, 3]

x2 = range(2, 11, 2)
y2 = [6, 7, 8, 9, 10]

titulo = "Gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Títulos Linha
plt.title("Titulo do Grafico")
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Plot Linha
plt.plot(x, y, label="Grupo 1")
plt.plot(x2, y2, label="Grupo 2")

# Plot Legenda
plt.legend()
# Mostra o Gráfico
plt.show()

# Barras
plt.title("Grafico de Barra")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x, y, label="Grupo 1")
plt.bar(x2, y2, label="Grupo 2")
plt.legend()
plt.show()
