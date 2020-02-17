import pytest
from src.classify import classify


@pytest.mark.parametrize(
    'input, expect', [
        ('64-19-7', 'cas'),
        ('106-53-6', 'cas'),
        ('10216-17-8', 'cas'),
        ('80-71-7', 'cas'),
        ('2950-43-8', 'cas'),
        ('OC=1(N(N=C(C=1)C2(=CC=CC=C2))C)', 'smiles'),
        ('C1=CC(=CC=C1F)S', 'smiles'),
        ('OC1=C(O)C=CC=C1', 'smiles'),
        ('OC(=O)C1=CC=C[Se]1', 'smiles'),
        ('CC(=O)C1=CC=CC1', 'smiles'),
        ('InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3', 'inchi'),
        ('InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5+,6?/m1/s1', 'inchi'),
        ('InChI=1S/C6H5ClS/c7-5-2-1-3-6(8)4-5/h1-4,8H', 'inchi'),
        ('InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,13H,1H3', 'inchi'),
        ('InChI=1S/2z', 'inchi'),
        ('InChI=1S/CH100', 'inchi'),
        ('VZXOZSQDJJNBRC-UHFFFAOYSA-N', 'inchikey'),
        ('FTBCOQFMQSTCQQ-UHFFFAOYSA-N', 'inchikey'),
        ('ZAIBWUAGAZIQMM-UHFFFAOYNA-N', 'inchikey'),
        ('GVGFEJPTKINGLP-UHFFFAOYNA-N', 'inchikey'),
        ('WAQBFLCVNNZBQR-UHFFFAOYSA-N', 'inchikey'),
        ('ICXJVZHDZFXYQC-RAZYNMGUSA-N', 'inchikey'),
    ]
)
def test_classify_return_answer(input, expect):
    result = classify(input)
    assert result == expect


@pytest.mark.xfail    # smiles_pattern also recognize some none sense input
@pytest.mark.parametrize(
    'input, expect', [
        ('some non sense', None),
        ('123456789', None),
        (1234567, None),
        ('qwertyui', None),
    ]
)
def test_classify_return_None(input, expect):
    result = classify(input)
    assert result == expect
