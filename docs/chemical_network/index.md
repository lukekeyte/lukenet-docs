# Chemical Network

The chemical network file specifies the complete set of chemical species, reactions, and rate coefficients that drive the chemical evolution in `LukeNet`. By design, `LukeNet` is configured to read chemical networks with identical format to that of the widely-used `DALI` astrochemistry code, enabling direct comparison with published results and facilitating network sharing within the community.

The file follows a structured format with three main sections:
1. A list of elements that form the basic building blocks
2. A comprehensive list of atomic and molecular species, including their properties
3. A detailed list of chemical reactions and their rate coefficients

It is crucial that the correct formatting is maintained, as even minor deviations can cause parsing errors. The structure of a typical network file is shown below.

##  Chemical Network File Format

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

<br>

### Species Section
```
! n_species
135
! LIST OF SPECIES
!             < Initial     amu chr H  He C  N  O  Mg Si S  Fe Pa
H               1.000e+00     1  0  1  0  0  0  0  0  0  0  0  0
He              7.590e-02     4  0  0  1  0  0  0  0  0  0  0  0
C               1.000e-05    12  0  0  0  1  0  0  0  0  0  0  0
N               2.140e-05    14  0  0  0  0  1  0  0  0  0  0  0
O               2.000e-05    16  0  0  0  0  0  1  0  0  0  0  0
...
```


Each species entry contains:
- Species name
- Initial abundance
- Molecular mass (amu)
- Charge (0, +1, -1 etc)
- Element composition (counts of each element)

<br>

> **⚠️ Important Notes:**  
> • PAHs are treated as a separate element in the species list ('Pa')  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• The PAH abundance should be set to the ISM value ~ 6.000e-7  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• The desired PAH abundance is then set using the ``pah_ism`` parameter in the Input File  
> • Ice-phase species are preceded with 'J' (eg. ice phase 'CO' is denoted 'JCO')  
> • Vibrationally excited H₂ is denoted H2*

<br>

### Reactions Section
```
! n_reactions
1463
!
!e1           e2            e3            p1            p2            p3            p4            p5               nr  type  a            b            c            temp_min     temp_max   pd-data
H             CH                          C             H2                                                          16  20   1.310e-10    0.000e+00    8.000e+01    0.000e+00    2.000e+03  ---------
H             CH2                         CH            H2                                                          17  20   6.640e-11    0.000e+00    0.000e+00    0.000e+00    2.500e+03  ---------
H             NH                          N             H2                                                          18  20   1.730e-11    5.000e-01    2.400e+03    0.000e+00    3.000e+02  ---------
H             CH3                         CH2           H2                                                          19  20   1.000e-10    0.000e+00    7.600e+03    0.000e+00    2.500e+03  ---------
H             NH2                         NH            H2                                                          20  20   5.250e-12    7.900e-01    2.200e+03    0.000e+00   -1.100e+03  ---------
H             NH2                         NH            H2                                                          21  20   1.050e-10    0.000e+00    4.450e+03    1.100e+03    3.000e+03  ---------
...
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
| pd-data | Photodissociation data **<span style="color:darkred">(not currently used)</span>**|

<br>

## Reaction Types

The network includes several categories of reactions, indicated by the type code:

### Surface Chemistry (10-12)
- **10**: H₂ formation on grains
- **11**: Hydrogenation
- **12**: Photodesorption

### Gas Phase (20-22)
- **20**: Standard gas-phase reactions
- **21**: Temperature-limited reactions (no extrapolation)
- **22**: Temperature-bounded reactions (switched off outside range)

### Photochemistry (30-33)
- **30**: Standard photodissociation
- **31**: H₂ photodissociation with self-shielding
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
- **90**: H₂ excitation
- **91**: H₂* de-excitation
- **92**: H₂* reactions
<br><br>
> **⚠️ Important Notes:**  
> • Self-shielding of CO isotopologues is not currently implemented  

<br>

## Alternative Network Formats

`LukeNet` is currently configured to only read `DALI`-format network files. However, support for alternative formats can be added by modifying the code:

### Steps to Add Custom Format Support

1. Create a Python function that reads your network file and returns the following arrays:

    ```python
    def read_custom_network(filename):
        # Your parsing code here
        return (n_elements, elements_name,
                n_species, species_name, species_abu, 
                species_mass, species_charge,
                n_reactions, reactions_educts, reactions_products,
                reactions_reaction_id, reactions_itype,
                reactions_a, reactions_b, reactions_c,
                reactions_temp_min, reactions_temp_max, 
                reactions_pd_data)
    ```

2. Replace the `read_chemnet` function in the `lukenet_helpers` module with your custom function

3. Ensure your network follows these requirements:
    - Uses the same reaction type IDs as described in this documentation
    - Maintains consistent array shapes and data types
    - Includes all required fields for species and reactions
