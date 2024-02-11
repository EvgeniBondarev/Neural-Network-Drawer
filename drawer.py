import matplotlib.pyplot as plt

class NeuralNetworkDiagram:
    def __init__(self, max_n_layers_size=12, max_layer_size=6, show_neuron_numbers=True):
        """
        Example Usage:
        import matplotlib.pyplot as plt
        
        fig = plt.figure(figsize=(12, 12))
        ax = fig.gca()
        ax.axis('off')
        
        nn_diagram = NeuralNetworkDiagram()
        nn_diagram.draw_neural_net(ax, [7, 5, 4, 3, 4, 2, 1])
        
        plt.show()
                
        Parameters:
        - max_n_layers_size: Maximum number of neurons displayed per layer.
        - max_layer_size: Maximum number of neurons displayed in the network.
        - show_neuron_numbers: Display neuron numbers on the layer.
        
        Returns:
        None
        """
        self.max_n_layers_size = max_n_layers_size
        self.max_layer_size = max_layer_size
        self.show_neuron_numbers = show_neuron_numbers

    def draw_neural_net(self, ax, layer_sizes, left=.1, right=.9, bottom=.1, top=.9):
        """
        Draws the neural network diagram on the given axis.
        
        Parameters:
        - ax (matplotlib.axes._axes.Axes): Object to display the plot.
        - left (float): Left coordinate of the plot.
        - right (float): Right coordinate of the plot.
        - bottom (float): Bottom coordinate of the plot.
        - top (float): Top coordinate of the plot.
        - layer_sizes (list): List representing the sizes of neural network layers.
        
        Returns:
        None
        """

        n_layers = len(layer_sizes)
    
        if n_layers > self.max_n_layers_size:
            layer_sizes = [*layer_sizes[:int(self.max_n_layers_size / 2)], 0, *layer_sizes[-int(self.max_n_layers_size / 2):]]

        layers_data = []
        for layer_size in layer_sizes:
            if layer_size > self.max_layer_size:
                tmp = []
                for i in range(1, int(self.max_layer_size / 2)+1):
                    tmp.append(i)
                tmp.append(-1)
                for i in range(int(self.max_layer_size / 2), 0, -1):
                    tmp.append(layer_size-i+1)
                layers_data.append(tmp)
            else:
                layers_data.append([i for i in range(1, layer_size+1)])
                
        v_spacing = (top - bottom) / max([len(i) for i in layers_data])
        h_spacing = (right - left) / (len(layers_data) - 1)

        for n, layer_data in enumerate(layers_data):
            if len(layer_data) == 0:
                self.__draw_vertical_dots(ax, n * h_spacing + left, (top + bottom) / 2.)
            else:
                self.__draw_neurons(ax, n, layer_data, v_spacing, h_spacing, left, top, bottom)

        layer_sizes = [len(i) for i in layers_data]
        for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
            self.__draw_connections(ax, n, layer_size_a, layer_size_b, v_spacing, h_spacing, left, top, bottom)

    def __draw_vertical_dots(self, ax, x, y):
        """
        Draws vertical dots on the plot.
        
        Parameters:
        - ax (matplotlib.axes._axes.Axes): Object to display the plot.
        - x (float): x coordinate for the dots.
        - y (float): y coordinate for the dots.
        
        Returns:
        None
        """
        ax.text(x, y, '⁞', fontsize=30, verticalalignment='center', ha='center')

    def __draw_neurons(self, ax, n, layer_data, v_spacing, h_spacing, left, top, bottom):
        """
        Draws neurons on the plot.
        
        Parameters:
        - ax (matplotlib.axes._axes.Axes): Object to display the plot.
        - n (int): Layer number.
        - layer_size (int): Size of the current layer.
        - v_spacing (float): Vertical spacing between neurons.
        - h_spacing (float): Horizontal spacing between layers.
        - left (float): Left coordinate of the plot.
        - top (float): Top coordinate of the plot.
        - bottom (float): Bottom coordinate of the plot.
        
        Returns:
        None
        """
        layer_top = v_spacing * (len(layer_data) - 1) / 2. + (top + bottom) / 2.
 
        for i, m in enumerate(layer_data):
            if m == -1:
                ax.text(n * h_spacing + left, (top + bottom) / 2., '…', fontsize=10, verticalalignment='center')
            else:
                self.__draw_neuron(ax, n, i, layer_top, v_spacing, h_spacing, left)
                if self.show_neuron_numbers:
                    ax.text(n * h_spacing + left - len(str(m))/200, layer_top - (i * v_spacing - 1/200), str(m), fontsize=8, zorder=5)

    def __draw_neuron(self, ax, n, m, layer_top, v_spacing, h_spacing, left):
        """
        Draws a neuron on the plot.
        
        Parameters:
        - ax (matplotlib.axes._axes.Axes): Object to display the plot.
        - n (int): Layer number.
        - m (int): Neuron number in the layer.
        - layer_top (float): Top boundary of the layer.
        - v_spacing (float): Vertical spacing between neurons.
        - h_spacing (float): Horizontal spacing between layers.
        - left (float): Left coordinate of the plot.
        
        Returns:
        None
        """
        circle = plt.Circle((n * h_spacing + left + 0.001, layer_top - m * v_spacing + 0.01), v_spacing / 4., color='w', ec='k', zorder=4)
        ax.add_artist(circle)

    def __draw_connections(self, ax, n, layer_size_a, layer_size_b, v_spacing, h_spacing, left, top, bottom):
        """
        Draws connections between neurons on the plot.
        
        Parameters:
        - ax (matplotlib.axes._axes.Axes): Object to display the plot.
        - n (int): Layer number.
        - layer_size_a (int): Size of the current layer.
        - layer_size_b (int): Size of the next layer.
        - v_spacing (float): Vertical spacing between neurons.
        - h_spacing (float): Horizontal spacing between layers.
        - left (float): Left coordinate of the plot.
        - top (float): Top coordinate of the plot.
        - bottom (float): Bottom coordinate of the plot.
        
        Returns:
        None
        """
        neurons_to_draw_a = range(layer_size_a) if layer_size_a <= self.max_layer_size else [*range(3), *range(layer_size_a - 3, layer_size_a)]
        neurons_to_draw_b = range(layer_size_b) if layer_size_b <= self.max_layer_size else [*range(3), *range(layer_size_b - 3, layer_size_b)]
        layer_top_a = v_spacing * (layer_size_a - 1) / 2. + (top + bottom) / 2.
        layer_top_b = v_spacing * (layer_size_b - 1) / 2. + (top + bottom) / 2.

        for m in neurons_to_draw_a:
            for o in neurons_to_draw_b:
                if m != '...' and o != '...':
                    self.__draw_connection(ax, n, m, o, layer_top_a, layer_top_b, v_spacing, h_spacing, left)

    def __draw_connection(self, ax, n, m, o, layer_top_a, layer_top_b, v_spacing, h_spacing, left):
        """
        Draws a connection between two neurons on the plot.
        
        Parameters:
        - ax (matplotlib.axes._axes.Axes): Object to display the plot.
        - n (int): Layer number.
        - m (int): Neuron number in the current layer.
        - o (int): Neuron number in the next layer.
        - layer_top_a (float): Top boundary of the current layer.
        - layer_top_b (float): Top boundary of the next layer.
        - v_spacing (float): Vertical spacing between neurons.
        - h_spacing (float): Horizontal spacing between layers.
        - left (float): Left coordinate of the plot.
        
        Returns:
        None
        """
        line = plt.Line2D([n * h_spacing + left, (n + 1) * h_spacing + left],
                          [layer_top_a - m * v_spacing, layer_top_b - o * v_spacing], c='k')
        ax.add_artist(line)