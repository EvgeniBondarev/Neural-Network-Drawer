<div class="cell code" collapsed="false">

``` python
# Install the neural-net-drawer package via pip
pip install neural_net_drawer

```

</div>

<div class="cell code" collapsed="false">

``` python
# Import necessary libraries
import matplotlib.pyplot as plt
from neural-net-drawer.drawer import NeuralNetworkDiagram

```

</div>

<div class="cell code" execution_count="5"
ExecuteTime="{&quot;end_time&quot;:&quot;2024-02-07T08:56:55.425789900Z&quot;,&quot;start_time&quot;:&quot;2024-02-07T08:56:55.153634700Z&quot;}"
collapsed="false">

``` python
# Example usage
fig = plt.figure(figsize=(9, 9))
ax = fig.gca()
ax.axis('off')

# Create an instance of the NeuralNetworkDiagram class
nn_diagram = NeuralNetworkDiagram()

# Call the method to draw the neural network diagram
nn_diagram.draw_neural_net(ax, [7, 5, 4, 3, 4, 2, 1])

plt.show()

```

<div class="output display_data">

![](https://raw.githubusercontent.com/EvgeniBondarev/Neural-Network-Drawer/master/img/1.png)

</div>

</div>

<div class="cell code" execution_count="13"
ExecuteTime="{&quot;end_time&quot;:&quot;2024-02-07T09:03:39.420467900Z&quot;,&quot;start_time&quot;:&quot;2024-02-07T09:03:39.268470Z&quot;}"
collapsed="false">

``` python
# Example usage with customizations
fig = plt.figure(figsize=(9, 9))
ax = fig.gca()
ax.axis('off')

# Create an instance of the NeuralNetworkDiagram class
nn_diagram = NeuralNetworkDiagram()

# Set maximum number of layers to display
nn_diagram.max_n_layers_size = 3

# Set maximum number of neurons per layer to display
nn_diagram.max_layer_size = 10

# Call the method to draw the neural network diagram
nn_diagram.draw_neural_net(ax, [7, 5, 4, 3, 4, 2, 1])

plt.show()
```

<div class="output display_data">

![](https://raw.githubusercontent.com/EvgeniBondarev/Neural-Network-Drawer/master/img/2.png)

</div>

</div>

<div class="cell code" execution_count="12"
ExecuteTime="{&quot;end_time&quot;:&quot;2024-02-07T09:01:57.191557900Z&quot;,&quot;start_time&quot;:&quot;2024-02-07T09:01:56.936069200Z&quot;}"
collapsed="false">

``` python
# Example usage with further customizations
fig = plt.figure(figsize=(9, 9))
ax = fig.gca()
ax.axis('off')

# Create an instance of the NeuralNetworkDiagram class
nn_diagram = NeuralNetworkDiagram()

# Set maximum number of layers to display
nn_diagram.max_n_layers_size = 3

# Hide neuron numbers
nn_diagram.show_neuron_numbers = False

# Call the method to draw the neural network diagram
nn_diagram.draw_neural_net(ax, [7, 5, 4, 3, 4, 2, 1])

plt.show()
```

<div class="output display_data">

![](https://raw.githubusercontent.com/EvgeniBondarev/Neural-Network-Drawer/master/img/3.png)

</div>

</div>
