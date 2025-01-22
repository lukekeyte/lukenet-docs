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

## Chemical Model

The chemical model in `LukeNet` follows the standard rate equation approach to evolve molecular abundances under specified physical conditions. The model solves a system of coupled ordinary differential equations (ODEs) that describe the time evolution of species number densities:

$$
\frac{dn(i,t)}{dt} = \sum_j k_{ij} n(j,t) + \sum_{jl} k_{ijl} n(j,t) n(l,t)
$$
where $n(i,t)$ is the abundance ($\small{\text{cm}}^{-3}$) of species $i$ at time $t$, and $k_{ij}$ and $k_{ijl}$ are the respective destruction and formation rates of a given species.

### Gas-phase process

#### Gas-phase reactions
Gas-phase reactions follow standard temperature-dependent rate coefficients ($\small{k}$) of the modified Arrhenius form:

$$
k = \alpha \left(\frac{T_\text{gas}}{300\,\text{K}}\right)^\beta \exp\left(-\frac{\gamma}{T_\text{gas}}\right)
$$
where $\alpha$, $\beta$, and $\gamma$ are reaction-specific parameters, and $T_\text{gas}$ is the gas temperature. Each reaction has defined temperature limits ($T_\text{min}$ and $T_\text{max}$) that constrain its validity range.

#### Photodissociation and photoionization
Photochemical processes, including direct photodissociation and photoionization, are parametrized using the standard form:

$$
k = \alpha \beta G_0 \exp(-\gamma A_\text{V})
$$
where $\small{G_0}$ is the integrated FUV field strength in Draine units ($\sim 2.7 \times 10^{-3} \; \text{erg s} ^{-3}\text{cm}^{-2}$), $\small{A_\text{V}}$ is the visual extinction, and $\alpha$, $\beta$, and $\gamma$ are reaction-specific parameters. The model can optionally account for self-shielding effects in $\small{\text{CO}}$, $\small{\text{N}}_2$ , $\small{\text{H}}_2$, and atomic $\small{\text{C}}$, following the prescriptions of [Visser et al. (2009)](https://ui.adsabs.harvard.edu/abs/2009A%26A...503..323V/abstract),[Visser et al. (2018)](https://ui.adsabs.harvard.edu/abs/2018A%26A...615A..75V/abstract), [Draine & Bertoldi (1996)](https://ui.adsabs.harvard.edu/abs/1996ApJ...468..269D/abstract), and [Kamp & Bertoldi (2000)](https://ui.adsabs.harvard.edu/abs/2000A%26A...353..276K/abstract), repsectively.

To calculate these self-shielding factors, the code requires the total hydrogen ($\small{H}+{H}_2$) column density between the point of interest and the UV source (denoted $\small{N}_\text{H}$). This can be provided directly by the user, or alternatively, can be approximated using the standard relationship between hydrogen column density and visual extinction eg. [Guver & Ozel (2009)](https://ui.adsabs.harvard.edu/abs/2009MNRAS.400.2050G/abstract):

$$
N_\text{H} \approx 2.21 \times 10^{21} A_\text{V}
$$
The column density of a given species is then inferred from the total hydrogen column using the local fractional abundance:

$$
    N_\text{X} = N_\text{H} \times \frac{X}{n_\text{gas}}
$$
where $\small{X}$ denotes local number density of the species of interest.

The model also includes cosmic-ray and X-ray ionization processes, with both direct ionization and secondary electron effects. Simple PAH chemistry is incorporated through charge exchange and electron attachment/detachment processes, with PAH abundances scaled relative to ISM values.


### Grain processes

Grain-surface chemistry incorporates $\small{\text{H}}_2$ formation, hydrogenation, freeze-out, thermal desorption, and photodesorption processes. The $\small{\text{H}}_2$ formation rate on grains follows a temperature-dependent efficiency formalism that accounts for both physisorption and chemisorption binding sites ([Cazaux & Tielens 2002](https://ui.adsabs.harvard.edu/abs/2002ApJ...575L..29C/abstract), [2004](https://ui.adsabs.harvard.edu/abs/2004ApJ...604..222C/abstract); [Bosman et al. 2022a](https://ui.adsabs.harvard.edu/abs/2022ApJ...930L..26B/abstract)). Hydrogenation, thermal desorption, and photodesorption are implemented following [Visser et al. (2011)](https://ui.adsabs.harvard.edu/abs/2011A%26A...534A.132V/abstract).



## Code Overview

Code overview goes here

## Graphical User Interface (GUI)

To enhance accessibility and user workflow, `LukeNet` includes a graphical interface implemented in React that integrates the core solver with interactive visualization capabilitie. The GUI is included as part of the standard `pip` installation and can be launched locally, facilitating efficient exploration of chemical models by enabling real-time manipulation of physical parameters and visualization of results.

The interface provides dynamic visualization of abundance evolution, reaction rates, and chemical pathways, with comprehensive customization options. Species and reactions can be filtered based on abundance thresholds or selected manually to investigate specific chemical processes. Publication-quality figures can be exported in vector format (SVG), while numerical data can be extracted in standard formats for further analysis.

A key strength of the GUI is its ability to rapidly analyse parameter dependencies without the computational overhead of full multi-dimensional models. While codes like `DALI` [(Bruderer et al. 2012)](https://ui.adsabs.harvard.edu/abs/2012A%26A...541A..91B/abstract) provide comprehensive modelling capabilities, analysing the vast output from high-resolution models (often hundreds of gigabytes) can be cumbersome. The `LukeNet` GUI complements such models by allowing users to efficiently explore chemical evolution under varying conditions at specific points of interest. This makes it particularly valuable for investigating reaction mechanisms, understanding parameter sensitivities, and analysing localized chemical processes.


## Troubleshooting

### Common Issues
1. Import errors
   - Check Python version (3.8+ required)
   - Verify installation with `pip list`

2. Processing errors
   - Ensure data format matches requirements
   - Check available memory

## Support
Report issues on GitHub or contact l.keyte@qmul.ac.uk