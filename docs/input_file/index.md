# Input File

``LukeNet`` reads its configuration from a simple text-based input file (`.dat`) that defines the physical conditions, environmental parameters, and runtime settings for the simulation.

## Example Input
Here's a representative input file with typical values:

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

## Parameter Definitions

| Parameter | Description | Units |
|:----------|:------------|:------|
| `n_gas` | Number density of gas | cm³ |
| `n_dust` | Number density of dust grains | cm³ |
| `t_gas` | Gas temperature | K |
| `t_dust` | Dust grain temperature | K |
| `gtd` | Gas-to-dust number density ratio | dimensionless |
| `Av` | Visual extinction | mag |
| `G_0` | Local FUV field strength in Draine units | ~2.7 x 10⁻³ erg s⁻¹ cm⁻² |
| `Zeta_X` | X-ray ionization rate | s⁻¹ |
| `h2_col` | H₂ column density | cm⁻² |
| `self_shielding` | Enable self-shielding calculations for H₂, N₂, CO, and C | boolean |
| `column` | Use user-specified H₂ column density (`True`) or calculate from Av (`False`) | boolean |
| `Zeta_CR` | Cosmic ray ionization rate | s⁻¹ |
| `pah_ism` | PAH abundance relative to ISM value | dimensionless |
| `t_chem` | Chemical evolution time | years |
| `network` | Path to chemical network definition file | string |


## Creating an Input File
You can generate a template input file using the built-in helper function:
```python
import lukenet

# Generate default input file
lukenet.create_input("path/to/save/input_file.dat")

# Modify the generated file with your specific parameters
```
