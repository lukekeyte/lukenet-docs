# LukeNet Module Reference

## core.py

The core module implements the main chemical network solver functionality for LukeNet.

### class Lukenet()

Base class containing all functionality for solving astrochemical networks. LukeNet is designed to model and simulate complex chemical processes in various cosmic settings such as the ISM, molecular clouds, and protoplanetary disks.

#### Key Features
- Initialization of chemical species, reactions, and environmental parameters
- Efficient solving of stiff ODEs representing chemical reactions
- Support for various reaction types including gas-phase, grain-surface, and photochemistry
- Integration of self-shielding factors for specific molecules (H2, CO, N2, C)
- Optimization using Numba JIT compilation for performance-critical functions
- Comprehensive logging and progress tracking

#### Class Attributes

- `elements` (*model_classes.Elements*): Container for element-related data
- `species` (*model_classes.Species*): Container for chemical species data
- `gas` (*model_classes.Gas*): Gas phase properties and parameters
- `dust` (*model_classes.Dust*): Dust grain properties and parameters
- `environment` (*model_classes.Environment*): Environmental conditions
- `reactions` (*model_classes.Reactions*): Chemical reaction network data
- `parameters` (*model_classes.Parameters*): Solver parameters and constants
- `abundance_history` (*list*): Time evolution of species abundances

#### Methods

#### init_lukenet(input_file)

Initialize the LukeNet chemical network solver with parameters from an input file.

**Parameters:**

- `input_file` (*str*): Path to the input parameter file

The input file should contain the following parameters:
- `n_gas`: Gas number density [cm^-3]
- `t_gas`: Gas temperature [K]  
- `n_dust`: Dust number density [cm^-3]
- `t_dust`: Dust temperature [K]
- `gtd`: Gas-to-dust ratio
- `Av`: Visual extinction [mag]
- `G_0`: UV field strength [Habing]
- `Zeta_X`: X-ray ionization rate [s^-1]
- `Zeta_CR`: Cosmic ray ionization rate [s^-1]
- `pah_ism`: PAH abundance relative to ISM
- `t_chem`: Chemical evolution time [years]
- `self_shielding`: Enable molecular self-shielding [bool]
- `column`: Enable column density calculations [bool]
- `h2_col`: H2 column density [cm^-2] (if column=True)

#### compute_rate_coefficients(y)

Computes reaction rate coefficients for all chemical reactions in the network.

**Parameters:**

- `y` (*numpy.ndarray*): Current abundances of all species [cm^-3]

**Updates:**

- `reactions.k` (*numpy.ndarray*): Array of rate coefficients for all reactions
- `disso_H2` (*float*): H2 dissociation rate, used for reaction types 90 & 91

Handles various reaction types including:
- H2 formation on dust grains (Cazaux & Tielens 2002/04, Bosman+22)
- Hydrogenation reactions (Visser+11)
- Photodesorption processes (Visser+11)
- Gas-phase reactions with temperature dependencies
- Photodissociation with self-shielding
- Cosmic ray induced reactions (Stauber+05, Heays+14, Visser+18)
- X-ray induced reactions (Stauber+05, Bruderer+09b)
- PAH/grain charge exchange
- Thermal desorption and freezeout (Visser+09a, Visser+11)
- H2 excitation processes (Tielens & Hollenbach 1985, Visser+18)

#### solve_network()

Solves the chemical reaction network using a stiff ODE solver.

This method integrates the system of ordinary differential equations that govern the chemical reaction network using SciPy's `solve_ivp` function with the backward differentiation formula (BDF) method.

**Returns:**

Dictionary containing:
- `time` (*numpy.ndarray*): Time points of the solution
- `abundances` (*numpy.ndarray*): Species abundances over time
- `rates` (*numpy.ndarray*): Reaction rates over the evaluated time points
- `success` (*bool*): Whether the integration was successful
- `message` (*str*): Solver message (success or error)
- `species` (*list*): Names of the chemical species
- `reaction_labels` (*list*): List of formatted strings describing each reaction

If the solver fails, returns a dictionary with:
- `success`: False
- `message`: Error message describing the failure
- `last_time`: Last successful integration time (if any)

## calculus.py

## dataclasses.py

## selfshielding.py

## analysis.py

## helpers.py
