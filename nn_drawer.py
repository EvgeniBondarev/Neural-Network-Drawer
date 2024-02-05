import matplotlib.pyplot as plt

max_n_layers_size = 6
max_layer_size = 6

def draw_neural_net(ax, layer_sizes, left=.1, right=.9, bottom=.1, top=.9):
    """
    Рисует диаграмму нейронной сети на переданном графике.

    Parameters:
    - ax (matplotlib.axes._axes.Axes): Объект для отображения графика.
    - left (float): Координата левого края графика.
    - right (float): Координата правого края графика.
    - bottom (float): Координата нижнего края графика.
    - top (float): Координата верхнего края графика.
    - layer_sizes (list): Список, представляющий размеры слоев нейронной сети.

    Returns:
    None
    """
    n_layers = len(layer_sizes)

    if n_layers > max_n_layers_size:
        layer_sizes = [*layer_sizes[:3], 0, *layer_sizes[-3:]]

    v_spacing = (top - bottom) / max(layer_sizes)
    h_spacing = (right - left) / (n_layers - 1)

    for n, layer_size in enumerate(layer_sizes):
        if layer_size == 0:
            __draw_vertical_dots(ax, n * h_spacing + left, (top + bottom) / 2.)
        else:
            __draw_neurons(ax, n, layer_size, v_spacing, h_spacing, left, top, bottom)

    for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        __draw_connections(ax, n, layer_size_a, layer_size_b, v_spacing, h_spacing, left, top, bottom)

def __draw_vertical_dots(ax, x, y):
    """
    Рисует вертикальные точки на графике.

    Parameters:
    - ax (matplotlib.axes._axes.Axes): Объект для отображения графика.
    - x (float): Координата x для точек.
    - y (float): Координата y для точек.

    Returns:
    None
    """
    ax.text(x, y, '⁞', fontsize=30, verticalalignment='center', ha='center')

def __draw_neurons(ax, n, layer_size, v_spacing, h_spacing, left, top, bottom):
    """
    Рисует нейроны на графике.

    Parameters:
    - ax (matplotlib.axes._axes.Axes): Объект для отображения графика.
    - n (int): Номер слоя.
    - layer_size (int): Размер текущего слоя.
    - v_spacing (float): Вертикальное расстояние между нейронами.
    - h_spacing (float): Горизонтальное расстояние между слоями.
    - left (float): Координата левого края графика.
    - top (float): Координата верхнего края графика.
    - bottom (float): Координата нижнего края графика.

    Returns:
    None
    """
    layer_top = v_spacing * (layer_size - 1) / 2. + (top + bottom) / 2.
    neurons_to_draw = range(layer_size) if layer_size <= max_n_layers_size else [*range(3), '…', *range(layer_size - 3, layer_size)]

    for m in neurons_to_draw:
        if m == '…':
            ax.text(n * h_spacing + left, (top + bottom) / 2., '…', fontsize=25, verticalalignment='center')
        else:
            __draw_neuron(ax, n, m, layer_top, v_spacing, h_spacing, left)

def __draw_neuron(ax, n, m, layer_top, v_spacing, h_spacing, left):
    """
    Рисует нейрон на графике.

    Parameters:
    - ax (matplotlib.axes._axes.Axes): Объект для отображения графика.
    - n (int): Номер слоя.
    - m (int): Номер нейрона в слое.
    - layer_top (float): Верхняя граница слоя.
    - v_spacing (float): Вертикальное расстояние между нейронами.
    - h_spacing (float): Горизонтальное расстояние между слоями.
    - left (float): Координата левого края графика.

    Returns:
    None
    """
    circle = plt.Circle((n * h_spacing + left, layer_top - m * v_spacing), v_spacing / 4., color='w', ec='k', zorder=4)
    ax.add_artist(circle)

def __draw_connections(ax, n, layer_size_a, layer_size_b, v_spacing, h_spacing, left, top, bottom):
    """
    Рисует соединения между нейронами на графике.

    Parameters:
    - ax (matplotlib.axes._axes.Axes): Объект для отображения графика.
    - n (int): Номер слоя.
    - layer_size_a (int): Размер текущего слоя.
    - layer_size_b (int): Размер следующего слоя.
    - v_spacing (float): Вертикальное расстояние между нейронами.
    - h_spacing (float): Горизонтальное расстояние между слоями.
    - left (float): Координата левого края графика.
    - top (float): Координата верхнего края графика.
    - bottom (float): Координата нижнего края графика.

    Returns:
    None
    """
    neurons_to_draw_a = range(layer_size_a) if layer_size_a <= max_layer_size else [*range(3), *range(layer_size_a - 3, layer_size_a)]
    neurons_to_draw_b = range(layer_size_b) if layer_size_b <= max_layer_size else [*range(3), *range(layer_size_b - 3, layer_size_b)]
    layer_top_a = v_spacing * (layer_size_a - 1) / 2. + (top + bottom) / 2.
    layer_top_b = v_spacing * (layer_size_b - 1) / 2. + (top + bottom) / 2.

    for m in neurons_to_draw_a:
        for o in neurons_to_draw_b:
            if m != '...' and o != '...':
               __draw_connection(ax, n, m, o, layer_top_a, layer_top_b, v_spacing, h_spacing, left)

def __draw_connection(ax, n, m, o, layer_top_a, layer_top_b, v_spacing, h_spacing, left):
    """
    Рисует соединение между двумя нейронами на графике.

    Parameters:
    - ax (matplotlib.axes._axes.Axes): Объект для отображения графика.
    - n (int): Номер слоя.
    - m (int): Номер нейрона в текущем слое.
    - o (int): Номер нейрона в следующем слое.
    - layer_top_a (float): Верхняя граница текущего слоя.
    - layer_top_b (float): Верхняя граница следующего слоя.
    - v_spacing (float): Вертикальное расстояние между нейронами.
    - h_spacing (float): Горизонтальное расстояние между слоями.
    - left (float): Координата левого края графика.

    Returns:
    None
    """
    line = plt.Line2D([n * h_spacing + left, (n + 1) * h_spacing + left],
                      [layer_top_a - m * v_spacing, layer_top_b - o * v_spacing], c='k')
    ax.add_artist(line)
