# LukeNet Module Reference

## core.py

The core module implements the main chemical network solver functionality for LukeNet.

### <span style="background-color: #E9F2F9">*class* Lukenet</span>

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

#### <span style="background-color:rgba(215, 217, 219, 0.33)">init_lukenet(*input_file*)</span>

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


#### <span style="background-color:rgba(215, 217, 219, 0.33)">compute_rate_coefficients(*y*)</span>

Computes reaction rate coefficients for all chemical reactions in the network.

**Parameters:**

- `y` (*numpy.ndarray*): Current abundances of all species [cm^-3]

**Updates:**

- `reactions.k` (*numpy.ndarray*): Array of rate coefficients for all reactions
- `disso_H2` (*float*): H2 dissociation rate, used for reaction types 90 & 91

Handles various reaction types including:
- H2 formation on dust grains (Cazaux & Tielens 2002, 2004; Bosman et al. 2022)
- Hydrogenation reactions (Visser et al. 2011)
- Photodesorption processes (Visser et al. 2011)
- Gas-phase reactions with temperature dependencies
- Photodissociation with self-shielding
- Cosmic ray induced reactions (Stauber et al. 2005, Heays et al. 2014, Visser et al. 2018)
- X-ray induced reactions (Stauber et al. 2005, Bruderer et al. 2009b)
- PAH/grain charge exchange
- Thermal desorption and freezeout (Visser et al. 2009a, Visser et al. 2011)
- H2 excitation processes (Tielens & Hollenbach 1985, Visser et al. 2011)


#### <span style="background-color:rgba(215, 217, 219, 0.33)">solve_network()</span>

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



<br/>

## calculus.py



<br/>

## dataclasses.py

The `model_classes.py` module serves as the foundational data structure layer for the LukeNet astrochemical network solver. It implements a comprehensive set of Python dataclasses that define and manage the core components of the chemical network simulation.

### <span style="background-color: #E9F2F9">*class* Elements</span>

A container class for managing chemical elements data within the network.

#### Attributes:
- `name` (List[str]): List of chemical element names

#### Methods:
- `validate()`: Performs validation checks on element data
- `info()`: Displays basic information about the elements

#### Validation Rules:
- Element names must be strings in a list format
- Names cannot be empty
- No duplicate element names allowed

### <span style="background-color: #E9F2F9">*class* Species</span>

Manages chemical species data and their properties within the network.

#### Attributes:
- `name` (List[str]): Chemical species names
- `abundance` (NDArray): Species abundances relative to total H
- `number` (NDArray): Number densities (cm^-3)
- `mass` (NDArray): Masses in atomic mass units (amu)
- `charge` (NDArray): Charges in elementary charge units (e)

#### Methods:
- `validate()`: Validates species data integrity
- `info()`: Displays species information summary

#### Validation Rules:
- All arrays must match the length of name list
- Abundances must be between 0 and 1
- Number densities and masses must be positive
- Charges must be whole numbers between -4 and +4

### <span style="background-color: #E9F2F9">*class* Gas</span>

Defines gas phase properties for the chemical network.

#### Attributes:
- `n_gas` (float): Gas number density (cm^-3)
- `t_gas` (float): Gas temperature (K)
- `h2_col` (float): H2 column density (cm^-2)

#### Methods:
- `validate()`: Validates gas property data
- `info()`: Displays gas property information

#### Validation Rules:
- All properties must be numerical
- Number density and temperature must be positive
- H2 column density must be non-negative

### <span style="background-color: #E9F2F9">*class* Dust</span>

Manages dust grain properties within the chemical network.

#### Attributes:
- `n_dust` (float): Dust grain number density (cm^-3)
- `t_dust` (float): Dust temperature (K)
- `radius` (float): Grain radius (cm)
- `binding_sites` (float): Number of molecular binding sites per grain

#### Methods:
- `validate()`: Validates dust property data
- `info()`: Displays dust property information

#### Validation Rules:
- All properties must be numerical and positive
- Default radius is 1e-5 cm (0.1 micron)
- Default binding sites is 1e6

### <span style="background-color: #E9F2F9">*class* Reactions</span>

Handles chemical reaction network data and properties.

#### Attributes:
- `educts` (List[List[str]]): Reactants for each reaction
- `products` (List[List[str]]): Products for each reaction
- `reaction_id` (NDArray): Unique reaction identifiers
- `itype` (NDArray): Reaction type identifiers
- `a`, `b`, `c` (NDArray): Rate coefficient parameters
- `temp_min`, `temp_max` (NDArray): Temperature range validity
- `pd_data` (NDArray): Photodissociation data
- `k` (NDArray): Calculated rate coefficients
- `labels` (List[str]): Human-readable reaction descriptions

#### Methods:
- `validate()`: Validates reaction network data
- `info()`: Displays reaction network information

#### Validation Rules:
- All arrays must have matching lengths
- Reaction IDs must be unique positive integers
- Temperature limits must be physically reasonable
- Rate coefficients must be non-negative

### <span style="background-color: #E9F2F9">*class* Environment</span>

Manages physical environmental conditions for the simulation.

#### Attributes:
- `gtd` (float): Gas-to-dust mass ratio
- `Av` (float): Visual extinction (magnitudes)
- `G_0` (float): FUV radiation field (Habing units)
- `G_0_unatt` (float): Unattenuated FUV field
- `Zeta_X` (float): X-ray ionization rate (s^-1)
- `Zeta_CR` (float): Cosmic ray ionization rate (s^-1)
- `pah_ism` (float): PAH abundance relative to ISM
- `dg100` (float): Normalized gas-to-dust ratio

#### Methods:
- `validate()`: Validates environmental conditions
- `info()`: Displays environmental parameters

#### Validation Rules:
- All values must be numerical
- Most parameters must be non-negative
- Gas-to-dust ratio must be positive

### <span style="background-color: #E9F2F9">*class* Parameters</span>

Contains simulation parameters and physical constants.

#### Attributes:
- `n_elements` (int): Number of chemical elements
- `n_species` (int): Number of chemical species
- `n_reactions` (int): Number of reactions
- `time_initial` (float): Initial time (seconds)
- `time_final` (float): Final time (seconds)
- `delta_v` (float): Velocity dispersion (km/s)
- `av_nH` (float): Column to extinction conversion
- `self_shielding` (bool): Self-shielding flag
- `column` (bool): Column-based shielding flag
- `k_B` (float): Boltzmann constant (erg/K)
- `yr_sec` (float): Seconds per year
- `m_p` (float): Proton mass (g)
- `validate()`: Validates parameter values
- `info()`: Displays parameter information

#### Validation Rules:
- Network parameters must be non-negative integers
- Time values must be positive with final > initial
- Physical constants must be positive
- Boolean flags must be proper boolean values




<br/>

## selfshielding.py



<br/>

## analysis.py



<br/>

***

## helpers.py
