[![Python 3](https://pyup.io/repos/github/khoivan88/pka_lookup/python-3-shield.svg)](https://pyup.io/repos/github/khoivan88/pka_lookup/)
[![Updates](https://pyup.io/repos/github/khoivan88/pka_lookup/shield.svg)](https://pyup.io/repos/github/khoivan88/pka_lookup/)


## Overview:

- Python script to lookup pKa value from local database (~7,300 records) and from Pubchem using: CAS number, SMILES, InChI, InChIKey, IUPAC name.
- Most of the records (~6,900) in the current database is from [JCheminform Mansouri et. al.](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0384-1)
- The data is provide in this repo [here](src/data).
- If record is found on Pubchem but not in local database, the record will be added into the local database for faster access in the future

## Technology:

- Python 3.5+
- Python libraries:
  - PubChemPy
  - requests
  - pandas
  - tinyDB

## Example usage:

### For searching pKa from local database and Pubchem:

The following is a snippet of [search_pka.py](src/search_pka.py)

```python
db = TinyDB('data/tinydb_db.json', sort_keys=True, indent=4, 
        storage=CachingMiddleware(JSONStorage))    # Using caching for faster performance 
try:
    identifiers = [
        '64-19-7',    # acetic acid   >>> pKa = 4.76 at 25 °C
        '2950-43-8',    # Hydroxylamine-O-sulfonic acid, no result     
        'InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H',    # thiophenol
        'C1=CC=C(C=C1)O',    # phenol   >>> pKa = 9.9
    ]
    for identifier in identifiers:
        print('Searching for pKa of structure with identifier: {}'.format(identifier))
        result = search_pka(identifier=identifier, database=db)
        pprint(result)
except Exception as error:
    print(error)
finally:
    # Close database to write to disk
    db.close()
```

Result:

```bash
Searching for pKa of structure with identifier: 64-19-7
[
    {
        "Canonical_SMILES": "CC(=O)O",
        "IUPAC_Name": "acetic acid",
        "InChI": "InChI=1S/C2H4O2/c1-2(3)4/h1H3,(H,3,4)",
        "InChIKey": "QTBSBXVTEAMEQO-UHFFFAOYSA-N",
        "Isomeric_SMILES": "CC(=O)O",
        "Pubchem_CID": "176",
        "Substance_CASRN": "64-19-7",
        "pKa": "4.76 at 25 °C",
        "reference": "Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989",
        "source": "Pubchem"
    }
]
Searching for pKa of structure with identifier: 2950-43-8
null
Searching for pKa of structure with identifier: InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H
[
    {
        "Canonical_SMILES": "SC1C=CC=CC=1",
        "DSSTox_Structure_Id": "DTXCID906811",
        "InChI": "InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H",   
        "InChIKey": "RMVRSNDYEFQCLF-UHFFFAOYSA-N",
        "Original_SMILES": "SC1(=CC=CC=C1)",
        "Original_Source_ID": "17763",
        "Salt_Solvent_(Concatenate)": "?",
        "Structure_Formula": "C6H6S",
        "Structure_SMILES": "SC1=CC=CC=C1",
        "Substance_CASRN": "108-98-5",
        "Substance_Name": "Benzenethiol",
        "Substance_Type": "Single Compound",
        "basicOrAcidic": "acidic",
        "group": "SH",
        "method": "mean from 6",
        "pKa": "6.37",
        "solvent": "H2O",
        "source": "https://doi.org/10.1186/s13321-019-0384-1",
        "temp": "23",
        "type": "a1/apparent"
    },
    {
        "Canonical_SMILES": "C1=CC=C(C=C1)S",
        "IUPAC_Name": "benzenethiol",
        "InChI": "InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H",
        "InChIKey": "RMVRSNDYEFQCLF-UHFFFAOYSA-N",
        "Isomeric_SMILES": "C1=CC=C(C=C1)S",
        "Pubchem_CID": "7969",
        "Substance_CASRN": "108-98-5",
        "pKa": "6.62",
        "reference": "Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 165",
        "source": "Pubchem"
    }
]
Searching for pKa of structure with identifier: C1=CC=C(C=C1)O
[
    {
        "Canonical_SMILES": "C1=CC=C(C=C1)O",
        "IUPAC_Name": "phenol",
        "InChI": "InChI=1S/C6H6O/c7-6-4-2-1-3-5-6/h1-5,7H",
        "InChIKey": "ISWSIDIOOBJBQZ-UHFFFAOYSA-N",
        "Isomeric_SMILES": "C1=CC=C(C=C1)O",
        "Pubchem_CID": "996",
        "Substance_CASRN": "108-95-2",
        "pKa": "9.99 @ 25 °C",
        "reference": "Lide, D.R. (ed.). CRC Handbook of Chemistry and Physics. 83rd ed. Boca Raton, Fl: CRC Press Inc., 
2002-2003., p. 8-49",
        "source": "Pubchem"
    }
]
```


### For looking up pKa from Pubchem

- Using CAS number:

```python
>>> cas_nr = '64-19-7'    # acetic acid   >>> pKa = 4.76 at 25 °C
>>> print(pka_lookup_pubchem(cas_nr))    
>>> # print(pka_lookup_pubchem(cas_nr, 'cas'))    # give same result
{
    "Canonical_SMILES": "CC(=O)O",
    "IUPAC_Name": "acetic acid",
    "InChI": "InChI=1S/C2H4O2/c1-2(3)4/h1H3,(H,3,4)",
    "InChIKey": "QTBSBXVTEAMEQO-UHFFFAOYSA-N",
    "Isomeric_SMILES": "CC(=O)O",
    "Pubchem_CID": "176",
    "Substance_CASRN": "64-19-7",
    "pKa": "4.76 at 25 °C",
    "reference": "Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989",
    "source": "Pubchem"
}
```

- Using SMILES string:

```python
>>> smiles_string = 'OC1=CC=CC=C1'    # phenol
>>> print(pka_lookup_pubchem(smiles_string))
>>> # print(pka_lookup_pubchem(smiles_string, 'smiles'))    # give same result
{
    "Canonical_SMILES": "C1=CC=C(C=C1)O",
    "IUPAC_Name": "phenol",
    "InChI": "InChI=1S/C6H6O/c7-6-4-2-1-3-5-6/h1-5,7H",
    "InChIKey": "ISWSIDIOOBJBQZ-UHFFFAOYSA-N",
    "Isomeric_SMILES": "C1=CC=C(C=C1)O",
    "Pubchem_CID": "996",
    "Substance_CASRN": "108-95-2",
    "pKa": "9.99 @ 25 °C",
    "reference": "Lide, D.R. (ed.). CRC Handbook of Chemistry and Physics. 83rd ed. Boca Raton, Fl: CRC Press Inc., 2002-2003., p. 8-49",
    "source": "Pubchem"
}
```

- Using InChI string:

```python
>>> inchi_string = 'InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H'    # thiophenol
>>> print(pka_lookup_pubchem(inchi_string))
>>> # print(pka_lookup_pubchem(inchi_string, 'inchi'))    # give same result
{
    "Canonical_SMILES": "C1=CC=C(C=C1)S",
    "IUPAC_Name": "benzenethiol",
    "InChI": "InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H",
    "InChIKey": "RMVRSNDYEFQCLF-UHFFFAOYSA-N",
    "Isomeric_SMILES": "C1=CC=C(C=C1)S",
    "Pubchem_CID": "7969",
    "Substance_CASRN": "108-98-5",
    "pKa": "6.62",
    "reference": "Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 165",
    "source": "Pubchem"
}
```

- Using InChIKey string:

```python
>>> inchikey_string = 'OKKJLVBELUTLKV-UHFFFAOYSA-N'    # methanol
>>> print(pka_lookup_pubchem(inchikey_string))
>>> # print(pka_lookup_pubchem(inchikey_string, "inchikey"))    # give same result
{
    "Canonical_SMILES": "CO",
    "IUPAC_Name": "methanol",
    "InChI": "InChI=1S/CH4O/c1-2/h2H,1H3",
    "InChIKey": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
    "Isomeric_SMILES": "CO",
    "Pubchem_CID": "887",
    "Substance_CASRN": "67-56-1",
    "pKa": "15.3",
    "reference": "Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989",
    "source": "Pubchem"
}
```

- [More examples for pka_lookup_pubchem.py](examples/using_pka_lookup_pubchem.ipynb).

## Changelog:

See [here](VERSION.md) for details.
