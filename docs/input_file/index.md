# Input

The main parameters for `LukeNet` are read in from a simple input file which specifies the physical conditions, environmental parameters, and runtime settings.

The input file is a simple `.dat` file with the following form:

```
# LukeNet Input File

n_gas          = 1.190e+08
n_dust         = 2.498e+05
t_gas          = 1830.8
t_dust         = 148.0
gtd            = 4.763e+02
Av             = 3.136e-01
G_0            = 6.419e+04
Zeta_X         = 5.626e-14
h2_col         = 5.489e+18
self_shielding = True
column         = True
Zeta_CR        = 5e-17
pah_ism        = 0.1
t_chem         = 1e6
network        = 'network/data_chemnet4.dat'
```

where the individual parameters are defined as follows:


| Parameter| Description | 
|:-----|:------|
| `n_gas`          | Gas number density ($\small\text{cm}^3$)   | 
| `n_dust`         | Dust number density ($\small\text{cm}^3$)     | 
| `t_gas`          | Gas temperature (K)   | 
| `t_dust`         | Dust temperature (K)   | 
| `gtd`            | Gas-to-dust ratio   | 
| `Av`             | Visual extinction (mag) | 
| `G_0`            | Local FUV field strength in Draine units ($\small {\sim2.7 \times 10^{-3} \; \text{erg s}^{-1} \;\text{cm}^{-2}}$) | 
| `Zeta_X`         | X-ray ionization rate ($\text{s}^{-1}$) | 
| `h2_col`         | H2 column density ($\small\text{cm}^{-2}$)   | 
| `self_shielding` | Enable self-shielding of $\small \text{H}_2$, $\small \text{N}_2$, $\small \text{CO}$, $\small \text{C}$ (True/False) | 
| `column`         | User-specified $\small \text{H}_2$ column for self-shielding (True/False; calculated from Av if False)| 
| `Zeta_CR`        | Cosmic ray ionization rate ($\text{s}^{-1}$) | 
| `pah_ism`        | PAH abundance relative to ISM | 
| `t_chem`         | Chemical evolution time (years) | 
| `network`        | Full path to chemical network file | 






