import sys, os
sys.path.append(os.path.realpath('src'))

import pytest
from src.pka_lookup_pubchem import pka_lookup_pubchem


@pytest.mark.parametrize(
    'input, expect', [
        ('64-19-7', {
            'source': 'Pubchem',
            'Pubchem CID': '176',
            'pka': '4.76 at 25 °C',
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989',
            'CanonicalSMILES': 'CC(=O)O', 
            'IsomericSMILES': 'CC(=O)O', 
            'InChI': 'InChI=1S/C2H4O2/c1-2(3)4/h1H3,(H,3,4)', 
            'InChIKey': 'QTBSBXVTEAMEQO-UHFFFAOYSA-N', 
            'IUPACName': 'acetic acid'
            }
        ),
        ('75-75-2', {
            'source': 'Pubchem',
            'Pubchem CID': '6395',
            'pka': '-1.86',
            'reference': 'Serjeant ED, Dempsey B; IUPAC Chemical Data Series No. 23. NY,NY: Pergamon Press p. 12 (1979)',
            'CanonicalSMILES': 'CS(=O)(=O)O', 
            'IsomericSMILES': 'CS(=O)(=O)O', 
            'InChI': 'InChI=1S/CH4O3S/c1-5(2,3)4/h1H3,(H,2,3,4)', 
            'InChIKey': 'AFVFQIVMOAPDHO-UHFFFAOYSA-N', 
            'IUPACName': 'methanesulfonic acid'
            }
        ),
        ('OC1=CC=CC=C1', {
            'source': 'Pubchem',
            'Pubchem CID': '996',
            'pka': '9.99 @ 25 °C',
            'reference': 'Lide, D.R. (ed.). CRC Handbook of Chemistry and Physics. 83rd ed. Boca Raton, Fl: CRC Press Inc., 2002-2003., p. 8-49',
            'CanonicalSMILES': 'C1=CC=C(C=C1)O', 
            'IsomericSMILES': 'C1=CC=C(C=C1)O', 
            'InChI': 'InChI=1S/C6H6O/c7-6-4-2-1-3-5-6/h1-5,7H', 
            'InChIKey': 'ISWSIDIOOBJBQZ-UHFFFAOYSA-N', 
            'IUPACName': 'phenol'
            }
        ),
        ('C1=CC=C(C=C1)O', {
            'source': 'Pubchem',
            'Pubchem CID': '996',
            'pka': '9.99 @ 25 °C',
            'reference': 'Lide, D.R. (ed.). CRC Handbook of Chemistry and Physics. 83rd ed. Boca Raton, Fl: CRC Press Inc., 2002-2003., p. 8-49',
            'CanonicalSMILES': 'C1=CC=C(C=C1)O', 
            'IsomericSMILES': 'C1=CC=C(C=C1)O', 
            'InChI': 'InChI=1S/C6H6O/c7-6-4-2-1-3-5-6/h1-5,7H', 
            'InChIKey': 'ISWSIDIOOBJBQZ-UHFFFAOYSA-N', 
            'IUPACName': 'phenol'
            }
        ),
        ('InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H', {
            'source': 'Pubchem', 
            'Pubchem CID': '7969', 
            'pka': '6.62', 
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 165',
            'CanonicalSMILES': 'C1=CC=C(C=C1)S',
            'IUPACName': 'benzenethiol',
            'InChI': 'InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H',
            'InChIKey': 'RMVRSNDYEFQCLF-UHFFFAOYSA-N',
            'IsomericSMILES': 'C1=CC=C(C=C1)S',            
            }
        ),
        ('OKKJLVBELUTLKV-UHFFFAOYSA-N', {
            'source': 'Pubchem', 
            'Pubchem CID': '887', 
            'pka': '15.3', 
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989',
            'CanonicalSMILES': 'CO', 
            'IsomericSMILES': 'CO', 
            'InChI': 'InChI=1S/CH4O/c1-2/h2H,1H3', 
            'InChIKey': 'OKKJLVBELUTLKV-UHFFFAOYSA-N', 
            'IUPACName': 'methanol'
            }
        ),
    ]
)
def test_pka_lookup_pubchem_nonamespace(input, expect):
    result = pka_lookup_pubchem(input)
    assert result == expect

@pytest.mark.parametrize(
    'input, namespace, expect', [
        ('64-19-7', 'cas', {
            'source': 'Pubchem',
            'Pubchem CID': '176',
            'pka': '4.76 at 25 °C',
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989',
            'CanonicalSMILES': 'CC(=O)O', 
            'IsomericSMILES': 'CC(=O)O', 
            'InChI': 'InChI=1S/C2H4O2/c1-2(3)4/h1H3,(H,3,4)', 
            'InChIKey': 'QTBSBXVTEAMEQO-UHFFFAOYSA-N', 
            'IUPACName': 'acetic acid'
            }
        ),
        ('75-75-2', 'cas', {
            'source': 'Pubchem',
            'Pubchem CID': '6395',
            'pka': '-1.86',
            'reference': 'Serjeant ED, Dempsey B; IUPAC Chemical Data Series No. 23. NY,NY: Pergamon Press p. 12 (1979)',
            'CanonicalSMILES': 'CS(=O)(=O)O', 
            'IsomericSMILES': 'CS(=O)(=O)O', 
            'InChI': 'InChI=1S/CH4O3S/c1-5(2,3)4/h1H3,(H,2,3,4)', 
            'InChIKey': 'AFVFQIVMOAPDHO-UHFFFAOYSA-N', 
            'IUPACName': 'methanesulfonic acid'
            }
        ),
        ('OC1=CC=CC=C1', 'smiles', {
            'source': 'Pubchem',
            'Pubchem CID': '996',
            'pka': '9.99 @ 25 °C',
            'reference': 'Lide, D.R. (ed.). CRC Handbook of Chemistry and Physics. 83rd ed. Boca Raton, Fl: CRC Press Inc., 2002-2003., p. 8-49',
            'CanonicalSMILES': 'C1=CC=C(C=C1)O', 
            'IsomericSMILES': 'C1=CC=C(C=C1)O', 
            'InChI': 'InChI=1S/C6H6O/c7-6-4-2-1-3-5-6/h1-5,7H', 
            'InChIKey': 'ISWSIDIOOBJBQZ-UHFFFAOYSA-N', 
            'IUPACName': 'phenol'
            }
        ),
        ('C1=CC=C(C=C1)O', 'smiles', {
            'source': 'Pubchem',
            'Pubchem CID': '996',
            'pka': '9.99 @ 25 °C',
            'reference': 'Lide, D.R. (ed.). CRC Handbook of Chemistry and Physics. 83rd ed. Boca Raton, Fl: CRC Press Inc., 2002-2003., p. 8-49',
            'CanonicalSMILES': 'C1=CC=C(C=C1)O', 
            'IsomericSMILES': 'C1=CC=C(C=C1)O', 
            'InChI': 'InChI=1S/C6H6O/c7-6-4-2-1-3-5-6/h1-5,7H', 
            'InChIKey': 'ISWSIDIOOBJBQZ-UHFFFAOYSA-N', 
            'IUPACName': 'phenol'
            }
        ),
        ('InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H', 'inchi', {
            'source': 'Pubchem', 
            'Pubchem CID': '7969', 
            'pka': '6.62', 
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 165',
            'CanonicalSMILES': 'C1=CC=C(C=C1)S',
            'IUPACName': 'benzenethiol',
            'InChI': 'InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H',
            'InChIKey': 'RMVRSNDYEFQCLF-UHFFFAOYSA-N',
            'IsomericSMILES': 'C1=CC=C(C=C1)S',            
            }
        ),
        ('OKKJLVBELUTLKV-UHFFFAOYSA-N', 'inchikey', {
            'source': 'Pubchem', 
            'Pubchem CID': '887', 
            'pka': '15.3', 
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989',
            'CanonicalSMILES': 'CO', 
            'IsomericSMILES': 'CO', 
            'InChI': 'InChI=1S/CH4O/c1-2/h2H,1H3', 
            'InChIKey': 'OKKJLVBELUTLKV-UHFFFAOYSA-N', 
            'IUPACName': 'methanol'
            }
        ),
    ]
)
def test_pka_lookup_pubchem_with_namespace(input, namespace, expect):
    result = pka_lookup_pubchem(input, namespace)
    assert result == expect


@pytest.fixture
def set_debug(monkeypatch):
    monkeypatch.setattr("src.pka_lookup_pubchem.debug", True)
    return True


@pytest.mark.parametrize(
    'input, expect, error', [
        ('2950-43-8', None, 'RuntimeError: pKa not found in Pubchem.'
        ),
        ('34347-81-4', None, 'RuntimeError: pKa not found in Pubchem.'
        ),
        ('OC=1(N(N=C(C=1)C2(=CC=CC=C2))C)', None, 'RuntimeError: pKa not found in Pubchem.'
        ),
        ('C1=CC(=CC=C1F)S', None, 'RuntimeError: pKa not found in Pubchem.'
        ),
        ('OC1=CC=CC=C1', {
            'source': 'Pubchem',
            'Pubchem CID': '996',
            'pka': '9.99 @ 25 °C',
            'reference': 'Lide, D.R. (ed.). CRC Handbook of Chemistry and Physics. 83rd ed. Boca Raton, Fl: CRC Press Inc., 2002-2003., p. 8-49',
            'CanonicalSMILES': 'C1=CC=C(C=C1)O', 
            'IsomericSMILES': 'C1=CC=C(C=C1)O', 
            'InChI': 'InChI=1S/C6H6O/c7-6-4-2-1-3-5-6/h1-5,7H', 
            'InChIKey': 'ISWSIDIOOBJBQZ-UHFFFAOYSA-N', 
            'IUPACName': 'phenol'
            }, 
            ''
        ),
        ('InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H', {
            'source': 'Pubchem', 
            'Pubchem CID': '7969', 
            'pka': '6.62', 
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 165',
            'CanonicalSMILES': 'C1=CC=C(C=C1)S',
            'IUPACName': 'benzenethiol',
            'InChI': 'InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H',
            'InChIKey': 'RMVRSNDYEFQCLF-UHFFFAOYSA-N',
            'IsomericSMILES': 'C1=CC=C(C=C1)S',            
            },
            ''
        ),
        ('InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,11H,1H3', 
            None,
            'RuntimeError: pKa not found in Pubchem.'
        ),
        ('InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,13H,1H3', 
            None, 
            'ValueError: This is not an exact match on Pubchem'
        ),
        ('00000-00-0', None, 'RuntimeError: Compound not found in Pubchem.'
        ),
        ('OKKJLVBELUTLKV-UHFFFAOYSA-N', 
            {
            'source': 'Pubchem', 
            'Pubchem CID': '887', 
            'pka': '15.3', 
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989',
            'CanonicalSMILES': 'CO', 
            'IsomericSMILES': 'CO', 
            'InChI': 'InChI=1S/CH4O/c1-2/h2H,1H3', 
            'InChIKey': 'OKKJLVBELUTLKV-UHFFFAOYSA-N', 
            'IUPACName': 'methanol'
            },
            ''
        ),
        ('SNAOXHWORPTDTJ-UHFFFAOYNA-N', 
            None,
            ''
        ),
    ]
)
def test_pka_lookup_pubchem_nonamespace_debugmode(set_debug, capsys, input, expect, error):
    # Ref for capture output: https://docs.pytest.org/en/latest/capture.html#accessing-captured-output-from-a-test-function
    
    result = pka_lookup_pubchem(input)
    captured = capsys.readouterr()
    assert result == expect
    assert error in captured.out


@pytest.mark.parametrize(
    'input, namespace, expect, error', [
        ('2950-43-8', 'cas', None, 'RuntimeError: pKa not found in Pubchem.'
        ),
        ('34347-81-4', 'cas', None, 'RuntimeError: pKa not found in Pubchem.'
        ),
        ('OC=1(N(N=C(C=1)C2(=CC=CC=C2))C)', 'smiles', None, 'RuntimeError: pKa not found in Pubchem.'
        ),
        ('C1=CC(=CC=C1F)S', 'smiles', None, 'RuntimeError: pKa not found in Pubchem.'
        ),
        ('OC1=CC=CC=C1', 'smiles', {
            'source': 'Pubchem',
            'Pubchem CID': '996',
            'pka': '9.99 @ 25 °C',
            'reference': 'Lide, D.R. (ed.). CRC Handbook of Chemistry and Physics. 83rd ed. Boca Raton, Fl: CRC Press Inc., 2002-2003., p. 8-49',
            'CanonicalSMILES': 'C1=CC=C(C=C1)O', 
            'IsomericSMILES': 'C1=CC=C(C=C1)O', 
            'InChI': 'InChI=1S/C6H6O/c7-6-4-2-1-3-5-6/h1-5,7H', 
            'InChIKey': 'ISWSIDIOOBJBQZ-UHFFFAOYSA-N', 
            'IUPACName': 'phenol'
            }, 
            ''
        ),
        ('InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H', 'inchi',
            {
                'source': 'Pubchem', 
                'Pubchem CID': '7969', 
                'pka': '6.62', 
                'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 165',
                'CanonicalSMILES': 'C1=CC=C(C=C1)S',
                'IUPACName': 'benzenethiol',
                'InChI': 'InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H',
                'InChIKey': 'RMVRSNDYEFQCLF-UHFFFAOYSA-N',
                'IsomericSMILES': 'C1=CC=C(C=C1)S',            
            },
            ''
        ),
        ('InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,11H,1H3', 
            'inchi',
            None,
            'RuntimeError: pKa not found in Pubchem.'
        ),
        ('InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,13H,1H3', 
            'inchi',
            None, 
            'ValueError: This is not an exact match on Pubchem'
        ),
        ('00000-00-0', 'cas', None, 'RuntimeError: Compound not found in Pubchem.'
        ),
        ('OKKJLVBELUTLKV-UHFFFAOYSA-N', 'inchikey', {
            'source': 'Pubchem', 
            'Pubchem CID': '887', 
            'pka': '15.3', 
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989',
            'CanonicalSMILES': 'CO', 
            'IsomericSMILES': 'CO', 
            'InChI': 'InChI=1S/CH4O/c1-2/h2H,1H3', 
            'InChIKey': 'OKKJLVBELUTLKV-UHFFFAOYSA-N', 
            'IUPACName': 'methanol'
            },
            ''
        ),
        ('SNAOXHWORPTDTJ-UHFFFAOYNA-N', 
            'inchikey', 
            None,
            ''
        ),
    ]
)
def test_pka_lookup_pubchem_with_namespace_debugmode(set_debug, capsys, input, namespace, expect, error):
    # Ref for capture output: https://docs.pytest.org/en/latest/capture.html#accessing-captured-output-from-a-test-function
    result = pka_lookup_pubchem(input)
    captured = capsys.readouterr()
    assert result == expect
    assert error in captured.out
