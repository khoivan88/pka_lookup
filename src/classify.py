import re

def classify(identifier: str) -> str:
    """Determine the type of chemical indentifier (CAS, smiles, inchi, inchikey)
    
    Parameters
    ----------
    indentifier : str
        a string of chemical indentifier
    
    Returns
    -------
    str
        one of (CAS, smiles, inchi, inchikey)
    """

    # https://www.ebi.ac.uk/miriam/main/collections/MIR:00000237
    cas_pattern = re.compile(r'^\d{1,7}\-\d{2}\-\d$')

    '''
    The first is reference from: https://gist.github.com/lsauer/1312860/264ae813c2bd2c27a769d261c8c6b38da34e22fb#file-smiles_inchi_annotated-js
    However, this can be matched with CAS or InChIKey as well
    >>> smiles_pattern = re.compile(r'^(?!InChI=)[^J][a-zA-Z0-9@+\-\[\]\(\)\\\/%=#$]{1,}$')
    This will not match CAS or InChIKey.
    Even then, the solution below can match a lot more strings: 
        'some non sense'
        '123456789',
        1234567,
        'qwertyui'
    '''
    smiles_pattern = re.compile(r'^(?!InChI=)(?!\d{1,7}\-\d{2}\-\d)(?![A-Z]{14}\-[A-Z]{10}(\-[A-Z])?)[^J][a-zA-Z0-9@+\-\[\]\(\)\\\/%=#$]{1,}$')

    # https://www.ebi.ac.uk/miriam/main/collections/MIR:00000383
    inchi_pattern = re.compile(r'^InChI\=1S?\/[A-Za-z0-9\.]+(\+[0-9]+)?(\/[cnpqbtmsih][A-Za-z0-9\-\+\(\)\,\/\?\;\.]+)*$')

    # https://www.ebi.ac.uk/miriam/main/collections/MIR:00000387
    inchikey_pattern = re.compile(r'^[A-Z]{14}\-[A-Z]{10}(\-[A-Z])?')

    # IMPORTANT: careful with the order of the dict since one regex might match more than 1 type
    # See smiles_pattern above
    lookup = {
        'cas': lambda x: cas_pattern.search(x),
        'inchi': lambda x: inchi_pattern.search(x),
        'inchikey': lambda x: inchikey_pattern.search(x),
        'smiles': lambda x: smiles_pattern.search(x),
    }

    for key, value in lookup.items():
        if value(identifier):
            return key


if __name__ == "__main__":
    print(classify('106-54-7'))
    # print(classify('InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5+,6?/m1/s1'))
    # print(classify('VZXOZSQDJJNBRC-UHFFFAOYSA-N'))
    # print(classify('C1=CC(=CC=C1F)S'))