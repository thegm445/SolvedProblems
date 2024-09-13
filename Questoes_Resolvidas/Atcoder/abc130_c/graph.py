import matplotlib.pyplot as plt

i = 1

def plot_rectangle_cut(W, H, x, y):
    """Plota o retângulo e o corte."""
    fig, ax = plt.subplots()

    # Desenhar retângulo
    rectangle = plt.Rectangle((0, 0), W, H, edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(rectangle)

    # Desenhar ponto (x, y)
    plt.plot(x, y, marker='o', markersize=5, color='red')

    # Desenhar linha de corte (apenas para ilustração)
    if 2*x == W and 2*y == H:
        plt.plot([0, W], [H/2, H/2], linestyle='--', color='blue')
        plt.plot([W/2, W/2], [0, H], linestyle='--', color='blue')
    else:
        max_area = max(x * H, W * y, (W - x) * H, W * (H - y))
        if max_area == x * H or max_area == (W - x) * H:
            plt.plot([x, x], [0, H], linestyle='--', color='blue')
        else:
            plt.plot([0, W], [y, y], linestyle='--', color='blue')

    # Configurar gráfico
    plt.xlim(-1, W+1)
    plt.ylim(-1, H+1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Corte do Retângulo')
    plt.grid(True)
    plt.savefig(f"sample{i}.png")

# Exemplos de entrada
plot_rectangle_cut(2, 3, 1, 2)  # Exemplo 1
i+= 1
plot_rectangle_cut(2, 2, 1, 1)  # Exemplo 2