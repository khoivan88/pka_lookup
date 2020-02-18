import sys, os
sys.path.append(os.path.realpath('src'))

import pytest
from src.pka_lookup_pubchem import pka_lookup_pubchem

@pytest.mark.parametrize(
    'input, expect', [
        ('64-19-7', {
            'input': '64-19-7',
            'source': 'Pubchem',
            'Pubchem CID': 176,
            'pka': '4.76 at 25 °C',
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989'
            }
        ),
        ('75-75-2', {
            'input': '75-75-2',
            'source': 'Pubchem',
            'Pubchem CID': 6395,
            'pka': '-1.86',
            'reference': 'Serjeant ED, Dempsey B; IUPAC Chemical Data Series No. 23. NY,NY: Pergamon Press p. 12 (1979)'
            }
        ),
        ('2950-43-8', {
            'input': '2950-43-8',
            'source': 'Pubchem',
            'Pubchem CID': 76284,
            'pka': None,
            'reference': None
            }
        ),
        ('34347-81-4', {
            'input': '34347-81-4',
            'source': 'Pubchem',
            'Pubchem CID': 2763504,
            'pka': None,
            'reference': None
            }
        ),
        ('OC=1(N(N=C(C=1)C2(=CC=CC=C2))C)', {
            'input': 'OC=1(N(N=C(C=1)C2(=CC=CC=C2))C)',
            'source': 'Pubchem',
            'Pubchem CID': 2763504,
            'pka': None,
            'reference': None
            }
        ),
        ('C1=CC(=CC=C1F)S', {
            'input': 'C1=CC(=CC=C1F)S',
            'source': 'Pubchem',
            'Pubchem CID': 67789,
            'pka': None,
            'reference': None
            }
        ),
        ('OC1=CC=CC=C1', {
            'input': 'OC1=CC=CC=C1',
            'source': 'Pubchem',
            'Pubchem CID': 996,
            'pka': '9.99 @ 25 °C',
            'reference': 'Lide, D.R. (ed.). CRC Handbook of Chemistry and Physics. 83rd ed. Boca Raton, Fl: CRC Press Inc., 2002-2003., p. 8-49'
            }
        ),
        ('C1=CC=C(C=C1)O', {
            'input': 'C1=CC=C(C=C1)O',
            'source': 'Pubchem',
            'Pubchem CID': 996,
            'pka': '9.99 @ 25 °C',
            'reference': 'Lide, D.R. (ed.). CRC Handbook of Chemistry and Physics. 83rd ed. Boca Raton, Fl: CRC Press Inc., 2002-2003., p. 8-49'
            }
        ),
        ('InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H', {
            'input': 'InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H', 
            'source': 'Pubchem', 
            'Pubchem CID': 7969, 
            'pka': '6.62', 
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 165'
            }
        ),
        ('InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,11H,1H3', {
            'input': 'InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,11H,1H3', 
            'source': 'Pubchem', 
            'Pubchem CID': 2763504, 
            'pka': None, 
            'reference': None            
            }
        ),
        ('InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,13H,1H3', {
            'input': 'InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,13H,1H3', 
            'source': 'Pubchem', 
            'Pubchem CID': None, 
            'pka': None, 
            'reference': None            
            }
        ),
        ('OKKJLVBELUTLKV-UHFFFAOYSA-N', {
            'input': 'OKKJLVBELUTLKV-UHFFFAOYSA-N', 
            'source': 'Pubchem', 
            'Pubchem CID': 887, 
            'pka': '15.3', 
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989'
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
            'input': '64-19-7',
            'source': 'Pubchem',
            'Pubchem CID': 176,
            'pka': '4.76 at 25 °C',
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989'
            }
        ),
        ('75-75-2', 'cas', {
            'input': '75-75-2',
            'source': 'Pubchem',
            'Pubchem CID': 6395,
            'pka': '-1.86',
            'reference': 'Serjeant ED, Dempsey B; IUPAC Chemical Data Series No. 23. NY,NY: Pergamon Press p. 12 (1979)'
            }
        ),
        ('2950-43-8', 'cas', {
            'input': '2950-43-8',
            'source': 'Pubchem',
            'Pubchem CID': 76284,
            'pka': None,
            'reference': None
            }
        ),
        ('OC=1(N(N=C(C=1)C2(=CC=CC=C2))C)', 'smiles', {
            'input': 'OC=1(N(N=C(C=1)C2(=CC=CC=C2))C)',
            'source': 'Pubchem',
            'Pubchem CID': 2763504,
            'pka': None,
            'reference': None
                    }
        ),
        ('C1=CC(=CC=C1F)S', 'smiles', {
            'input': 'C1=CC(=CC=C1F)S',
            'source': 'Pubchem',
            'Pubchem CID': 67789,
            'pka': None,
            'reference': None
            }
        ),
        ('OC1=CC=CC=C1', 'smiles', {
            'input': 'OC1=CC=CC=C1',
            'source': 'Pubchem',
            'Pubchem CID': 996,
            'pka': '9.99 @ 25 °C',
            'reference': 'Lide, D.R. (ed.). CRC Handbook of Chemistry and Physics. 83rd ed. Boca Raton, Fl: CRC Press Inc., 2002-2003., p. 8-49'
            }
        ),
        ('C1=CC=C(C=C1)O', 'smiles', {
            'input': 'C1=CC=C(C=C1)O',
            'source': 'Pubchem',
            'Pubchem CID': 996,
            'pka': '9.99 @ 25 °C',
            'reference': 'Lide, D.R. (ed.). CRC Handbook of Chemistry and Physics. 83rd ed. Boca Raton, Fl: CRC Press Inc., 2002-2003., p. 8-49'
            }
        ),
        ('InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H', 'inchi', {
            'input': 'InChI=1S/C6H6S/c7-6-4-2-1-3-5-6/h1-5,7H', 
            'source': 'Pubchem', 
            'Pubchem CID': 7969, 
            'pka': '6.62', 
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 165'
            }
        ),
        ('InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,11H,1H3', 'inchi', {
            'input': 'InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,11H,1H3', 
            'source': 'Pubchem', 
            'Pubchem CID': 2763504, 
            'pka': None, 
            'reference': None            
            }
        ),
        ('InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,13H,1H3', 'inchi', {
            'input': 'InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,13H,1H3', 
            'source': 'Pubchem', 
            'Pubchem CID': None, 
            'pka': None, 
            'reference': None            
            }
        ),
        ('OKKJLVBELUTLKV-UHFFFAOYSA-N', 'inchikey', {
            'input': 'OKKJLVBELUTLKV-UHFFFAOYSA-N', 
            'source': 'Pubchem', 
            'Pubchem CID': 887, 
            'pka': '15.3', 
            'reference': 'Serjeant, E.P., Dempsey B.; Ionisation Constants of Organic  Acids in Aqueous Solution. International Union of Pure and  Applied Chemistry (IUPAC). IUPAC Chemical Data Series No.  23, 1979. New York, New York: Pergamon Press, Inc., p. 989'
            }
        ),
    ]
)
def test_pka_lookup_pubchem_with_namespace(input, namespace, expect):
    result = pka_lookup_pubchem(input)
    assert result == expect

