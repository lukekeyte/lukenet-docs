# Chemical Network

The chemical network file specifies the chemical species, reactions, and rate coefficients used in `LukeNet`. The file follows a structured format with several sections:

## File Structure

### Elements Section
```
! n_elements
10
! LIST OF ELEMENTS 
H
He
C
N 
O
Mg
Si
S
Fe
Pa
```

### Species Section
```
! n_species
109
! LIST OF SPECIES
!             < Initial     amu chr H  He C  N  O  Mg Si S  Fe Pa
H               1.000e+00     1  0  1  0  0  0  0  0  0  0  0  0
He              7.590e-02     4  0  0  1  0  0  0  0  0  0  0  0
...
```
Each species entry contains:
- Species name
- Initial abundance
- Molecular mass (amu)
- Charge (0, +1, -1)
- Element composition (counts of each element)

### Reactions Section
```
! n_reactions
1463
!
!e1           e2            e3            p1            p2            p3            p4            p5               nr  type  a            b            c            temp_min     temp_max   pd-data
H             H                           H2                                                                         1  10   3.000e-18    5.000e-01    0.000e+00    0.000e+00    4.100e+04  ---------
```

Each reaction entry contains:
| Field | Description |
|:------|:------------|
| e1-e3 | Reactant species (up to 3) |
| p1-p5 | Product species (up to 5) |
| nr | Reaction number |
| type | Reaction type code |
| a | Rate coefficient $\alpha$ |
| b | Rate coefficient $\beta$  |
| c | Rate coefficient $\gamma$  |
| temp_min | Minimum valid temperature (K) |
| temp_max | Maximum valid temperature (K) |
| pd-data | Photodissociation data **(not currently used)**|

## Reaction Types

The network includes several categories of reactions, indicated by the type code:

### Surface Chemistry (10-12)
- **10**: H2 formation on grains
- **11**: Ice hydrogenation
- **12**: Photodesorption

### Gas Phase (20-22)
- **20**: Standard gas-phase reactions
- **21**: Temperature-limited reactions (no extrapolation)
- **22**: Temperature-bounded reactions (switched off outside range)

### Photochemistry (30-33)
- **30**: Standard photodissociation
- **31**: H2 photodissociation with self-shielding
- **32**: CO photodissociation with self-shielding
- **33**: C photoionization with self-shielding

### Cosmic Ray Chemistry (40-43)
- **40**: Direct cosmic ray ionization
- **41**: Cosmic ray induced FUV reactions
- **42**: Cosmic ray induced CO dissociation
- **43**: Cosmic ray induced He decay

### PAH Chemistry (70-72)
- **70**: PAH photoelectron production
- **71**: PAH charge exchange/recombination
- **72**: Mass-scaled PAH reactions

### Grain Chemistry (80-81)
- **80**: Thermal desorption
- **81**: Freeze-out

### H2* Chemistry (90-92)
- **90**: H2 excitation
- **91**: H2* de-excitation
- **92**: H2* reactions