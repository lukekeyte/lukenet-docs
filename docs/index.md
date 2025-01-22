# LukeNet Documentation

## Installation

LukeNet can be installed using pip:
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

The chemical model in \textsc{lukenet} follows the standard rate equation approach to evolve molecular abundances under specified physical conditions. The model solves a system of coupled ordinary differential equations (ODEs) that describe the time evolution of species number densities:

$$
\frac{dn(i,t)}{dt} = \sum_j k_{ij} n(j,t) + \sum_{jl} k_{ijl} n(j,t) n(l,t)
$$
where $n(i,t)$ is the abundance (cm$^{-3}$) of species $i$ at time $t$, and $k_{ij}$ and $k_{ijl}$ are the respective destruction and formation rates of a given species.

### Gas-phase process

#### Gas-phase reactions
Gas-phase reactions follow standard temperature-dependent rate coefficients of the modified Arrhenius form:

$$
k(T) = \alpha \left(\frac{T_\text{gas}}{300\,\text{K}}\right)^\beta \exp\left(-\frac{\gamma}{T_\text{gas}}\right)
$$
where $\alpha$, $\beta$, and $\gamma$ are reaction-specific parameters, and $T_\text{gas}$ is the gas temperature. Each reaction has defined temperature limits ($T_\text{min}$ and $T_\text{max}$) that constrain its validity range.

#### Photodissociation and photoionization
Photochemical processes, including direct photodissociation and photoionization, are parametrized using the standard form:
$$
k_\text{ph} = \alpha \beta G_0 \exp(-\gamma A_\text{V})
$$
where $G_0$ is the FUV field strength in Draine units $\sim 2.7 \times 10^{-3} \; \text{erg s} ^{-3}\text{cm}^{-2}$, integrated between $911-2067 \AA$, $A_\text{V}$ is the visual extinction, and $\alpha$, $\beta$, and $\gamma$ are reaction-specific parameters. The model can optionally account for self-shielding effects in $\small{\text{CO}}$, $\small{\text{N}}_2$ , $\small{\text{H}}_2$, and atomic $\small{\text{C}}$, following the prescriptions of Visser et al. (2009),Visser et al. (2018), Draine & Bertoldi (1996), and Kamp & Bertoldi (2000), repsectively.

To calculate these self-shielding factors, the code requires the total hydrogen ($\small{H}+{H}_2$) column density between the point of interest and the UV source (denoted $\small{N}_\text{H}$). This can be provided directly by the user, or alternatively, can be approximated using the standard relationship between hydrogen column density and visual extinction eg. Guver & Ozel (2009):
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

Grain-surface chemistry incorporates $\small{\text{H}}_2$ formation, hydrogenation, freeze-out, thermal desorption, and photodesorption processes. The $\small{\text{H}}_2$ formation rate on grains follows a temperature-dependent efficiency formalism that accounts for both physisorption and chemisorption binding sites (Cazaux & Tielens 2002, 2004; Bosman et al. 2022a). Hydrogenation, thermal desorption, and photodesorption are implemented following Visser et al. (2011).



## Code Overview

### lukenet.process_data()
Processes input data and returns results.

Parameters:
- data (array): Input data array
- method (str): Processing method ['fast', 'accurate']

Returns:
- dict: Processed results

### lukenet.plot_data()
Creates visualization of processed data.

Parameters:
- result (dict): Output from process_data()
- style (str, optional): Plot style ['line', 'scatter']

Returns:
- Figure object

## Graphical User Interface (GUI)
Settings can be modified in `config.yaml`:
```yaml
processing:
  method: fast
  threads: 4
visualization:
  style: line
  dpi: 300
```

## Troubleshooting

### Common Issues
1. Import errors
   - Check Python version (3.8+ required)
   - Verify installation with `pip list`

2. Processing errors
   - Ensure data format matches requirements
   - Check available memory

## Support
Report issues on GitHub or contact support@lukenet.com