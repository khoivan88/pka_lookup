## Version 0.2 (2020-02-20):

- Add pKa data from [JCheminform Mansouri et. al.](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0384-1) (~7000 pKa values)
- Create a local database using [tinyDB](https://github.com/msiemens/tinydb) to save data above and new data
- If record cannot be found in local database, the script will seach Pubchem and then add that info (if found) into local database to speed up search later
- Return value from local database as a list of dictionary
- Expand search text to include: CAS, SMILES, InChI, InChIKey, IUPAC name
- Ensure exact match from Pubchem when search text is: CAS, InChI, or InChIKey
- Return look up value from Pubchem as a Python dictionary


## Version 0.1 (2020-02-13):

- Look up pKa on Pubchem using CAS number