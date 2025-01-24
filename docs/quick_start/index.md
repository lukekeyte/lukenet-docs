## Quick Start
```python
import lukenet

# Create the input file
lukenet.create_input("path/to/save/input_file.dat")  # then open and set parameter values

# Run LukeNet
network = Lukenet("path/to/input_file.dat")          # create an instance of LukeNet
network.init_lukenet()                               # initialise the network
result = network.solve_network()                     # run the solver

# Plot some results
analysis = lukenet.Analysis(result)
analysis.plot_abundance(['CO', 'H2O', 'CH4'])
```