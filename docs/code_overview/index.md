# Code Description

## Overview

`LukeNet` is implemented entirely in Python, prioritizing code clarity while achieving acceptable performance through targeted optimization. The code is structured into several modules that handle distinct aspects of the chemical modelling. This modular design improves maintainability by separating distinct functionalities, facilitates testing by isolating components, and allows users to extend individual components without affecting the rest of the codebase. 

The core data structures are implemented using Python's dataclass framework, which provides a concise way to create classes focused on data storage with built-in validation. The primary dataclasses are:

* ```Species```: Contains arrays of abundances, masses, and charges for chemical species, alongside their names
* ```Reactions```: Stores reaction networks including reactants, products, rate coefficient parameters, and temperature limits
* ```Gas``` and ```Dust```: Hold physical properties such as temperatures and densities for each phase
* ```Environment```: Contains parameters describing the local conditions like radiation field strength, extinction, and ionization rates
* ```Parameters```: Stores simulation settings and physical constants

Each dataclass includes validation methods that ensure physical constraints are met (e.g., positive temperatures, valid abundance ranges) and type checking.

Rate coefficients are calculated using a type-based classification system that is deliberately compatible with the established ```DALI``` code [(Bruderer et al. 2012](https://ui.adsabs.harvard.edu/abs/2012A%26A...541A..91B/abstract), [2013](https://ui.adsabs.harvard.edu/abs/2013A%26A...559A..46B/abstract)). By adopting the same reaction type identifiers, ```LukeNet``` can seamlessly use chemical networks developed for \textsc{dali} without requiring reformatting or conversion. This design choice facilitates network validation and comparison of results between codes, and a detailed benchmarking of ```LukeNet``` against ```DALI``` is presented in our code overview paper. While the code currently reads networks in the ```DALI``` format, the modular structure allows users to easily implement additional parsers for other network formats, provided they map the reactions to the appropriate type identifiers. An example network (first presented in [Keyte et al. 2023](https://ui.adsabs.harvard.edu/abs/2023NatAs...7..684K/abstract)) is provided with the code.

The core solver is implemented in the ```LukeNet``` class, which manages the chemical network integration. This class employs the ```scipy.integrate.solve_ivp``` routine with the backward differentiation formula (BDF) method, which is particularly suitable for the stiff systems characteristic of astrochemical networks. Performance-critical numerical routines are optimized using ```numba``` just-in-time compilation. This includes the calculation of chemical derivatives and the Jacobian matrix. The derivatives function computes formation and destruction rates for each species, while the Jacobian calculation is optimized for the typically sparse structure of chemical networks, where most species interact with only a small subset of the total network.

Self-shielding calculations are handled by a dedicated module that pre-loads tabulated shielding factors during initialization. For $\small{\text{CO}}$ and $\small{\text{N}}_2$, this module implements interpolation routines that operate on the tabulated data, while $\small{\text{H}}_2$ and $\small{\text{C}}$ self-shielding are computed using their analytical approximations. 

The code also includes comprehensive analysis and visualization capabilities through a dedicated analysis module and graphical user interface. This provides plotting functions for species abundances and reaction rates over time, as well as tools for investigating chemical pathways and network properties. Data can also be exported in standard formats for further analysis.

```{toctree}
:maxdepth: 2
:caption: Contents

test/index