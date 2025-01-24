# LukeNet

`LukeNet` is a Python software package that numerically solves time-dependent chemical reaction networks for astrophysical environments. The code is optimized for modeling complex chemical evolution in settings such as the interstellar medium (ISM), molecular clouds, and protoplanetary disks.

## Installation

`LukeNet` can be installed using pip:
```bash
pip install lukenet
```

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



## Code Overview

Code overview goes here

## Graphical User Interface (GUI)

To enhance accessibility and user workflow, `LukeNet` includes a graphical interface implemented in React that integrates the core solver with interactive visualization capabilitie. The GUI is included as part of the standard `pip` installation and can be launched locally, facilitating efficient exploration of chemical models by enabling real-time manipulation of physical parameters and visualization of results.

The interface provides dynamic visualization of abundance evolution, reaction rates, and chemical pathways, with comprehensive customization options. Species and reactions can be filtered based on abundance thresholds or selected manually to investigate specific chemical processes. Publication-quality figures can be exported in vector format (SVG), while numerical data can be extracted in standard formats for further analysis.

A key strength of the GUI is its ability to rapidly analyse parameter dependencies without the computational overhead of full multi-dimensional models. While codes like `DALI` [(Bruderer et al. 2012)](https://ui.adsabs.harvard.edu/abs/2012A%26A...541A..91B/abstract) provide comprehensive modelling capabilities, analysing the vast output from high-resolution models (often hundreds of gigabytes) can be cumbersome. The `LukeNet` GUI complements such models by allowing users to efficiently explore chemical evolution under varying conditions at specific points of interest. This makes it particularly valuable for investigating reaction mechanisms, understanding parameter sensitivities, and analysing localized chemical processes.



```{toctree}
:maxdepth: 2
:caption: Contents

chemical_model/index
code_overview
gui