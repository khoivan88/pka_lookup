## Overview:
Python script to lookup pKa value from Pubchem using:
- CAS number
- SMILES
- InChI
- InChIKey

## Example usage:
- Using CAS number:
```python
>>> cas_nr = '64-19-7'    # acetic acid   >>> pKa = 4.76 at 25 °C
>>> print(pka_lookup_pubchem(cas_nr))    
>>> # print(pka_lookup_pubchem(cas_nr, 'cas'))    # give same result
{'input': '64-19-7', 'source': 'Pubchem', 'Pubchem CID': 176, 'pka': '4.76 at 25 °C', 'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989'}
```

- Using SMILES string:
```python
>>> smiles_string = 'OC1=CC=CC=C1'    # phenol
>>> print(pka_lookup_pubchem(smiles_string))
>>> # print(pka_lookup_pubchem(smiles_string, 'smiles'))    # give same result
{'input': 'OC1=CC=CC=C1', 'source': 'Pubchem', 'Pubchem CID': 996, 'pka': '9.99 @ 25 °C', 'reference': 'Lide, D.R. (ed.). CRC Handbook of Chemistry and Physics. 83rd ed. Boca Raton, Fl: CRC Press Inc., 2002-2003., p. 8-49'}
```

- Using InChI string:
```python
>>> inchi_string = 'InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H'    # thiophenol
>>> print(pka_lookup_pubchem(inchi_string))
>>> # print(pka_lookup_pubchem(inchi_string, 'inchi'))    # give same result
{'input': 'InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H', 'source': 'Pubchem', 'Pubchem CID': 7969, 'pka': '6.62', 'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 165'}
```

- Using InChIKey string:
```python
>>> inchikey_string = 'OKKJLVBELUTLKV-UHFFFAOYSA-N'    # methanol
>>> print(pka_lookup_pubchem(inchikey_string))
>>> # print(pka_lookup_pubchem(inchikey_string, "inchikey"))    # give same result
{'input': 'OKKJLVBELUTLKV-UHFFFAOYSA-N', 'source': 'Pubchem', 'Pubchem CID': 887, 'pka': '15.3', 'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989'}
```

- [More examples for pka_lookup_pubchem.py](examples/using_pka_lookup_pubchem.ipynb).

## Changelog:
See [here](VERSION.md) for details.
