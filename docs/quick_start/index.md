## Quick Start

Running a ```LukeNet``` model is simple: 
1. Import the model and create an input file
2. Adjust the value in the input file to suit your needs
3. Initialise the network using the full path to the input file
4. Run the solver

Results (abundances, reaction rates etc) are stored in a dictionary. These can be plotted using the functions in the ```analysis module```, or using your own code. A simple implementation is shown below.

```python
import lukenet

# Create the input file
lukenet.create_input("path/to/save/input_file.dat")  # then open and set parameter values

# Run LukeNet
network = lukenet.Lukenet()                          # create an instance of LukeNet
network.init_lukenet("path/to/input_file.dat")       # initialise the network
result = network.solve_network()                     # run the solver

# Plot some results
analysis = lukenet.Analysis(result)
analysis.plot_abundance(['CO', 'H2O', 'CH4'])
```