#!/usr/bin/env python
# coding: utf-8

"""
Author: Khoi Van 2020

This script takes a CAS number and look up its pKa (dissociation constant) 
from Pubchem and return it if found; return None, otherwise

Change notes:
- 2020-02-14:
  - Instead of just returning the result, return the result combo as json dict

"""

import sys
import traceback
import xml.etree.ElementTree as ET
from typing import Optional
import re

import pubchempy as pcp  # https://pubchempy.readthedocs.io/en/latest/guide/gettingstarted.html
import requests

from classify import classify


debug = False


def pka_lookup_pubchem(identifier, namespace=None, domain='compound') -> Optional[str]:
    global debug

    if len(sys.argv) == 2 and sys.argv[1] in ['--debug=True', '--debug=true', '--debug', '-d']:
        debug = True

    if debug:
        print(f'In DEBUG mode: {debug}')

    # Identify lookup source (Pubchem in this case)
    lookup_source = 'Pubchem'

    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; CentOS; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

        # print('Searching Pubchem...')

        # Using pubchem api for python
        # Getting CID number, the result of this, by default is exact match. The result is returned as a list.
        cids = []
        identifier_type = ''

        if not namespace:
            identifier_type = classify(identifier)
            # print(f'identifier_type determined by classify() is: {identifier_type}')

            # If the input is inchi, inchikey or smiles (this could be a false smiles):
            if identifier_type in ['smiles', 'inchi', 'inchikey']:
                lookup = pcp.get_cids(identifier, namespace=identifier_type)
                if lookup:
                    cids.append(lookup[0])
            else:
                lookup = pcp.get_cids(identifier, namespace='name')
                if lookup:
                    cids.append(lookup[0])
                    # print(f'namespace from pubchem lookup is: {namespace}')
        elif namespace == 'cas':
            cids = pcp.get_cids(identifier, namespace='name')
        else:
            cids = pcp.get_cids(identifier, namespace=namespace)

        if not cids:
            lookup = pcp.get_cids(identifier, namespace='name')
            if lookup:
                cids.append(lookup[0])

            # cids = pcp.get_cids(identifier, namespace=namespace)
            identifier_type = namespace

        # print(cids)

        #  this api return an empty list if it cannot find cas_nr. This is to check if pubchem has this chemical.
        if len(cids) > 0:
            # if Pubchem found the result, get the first result of the list
            cid = cids[0]
            # print('Compound ID (CID) from PubChem is: {} and type is: {}'.format(cid, type(cid)))

            exact_match = True

            synonyms = []
            if identifier_type == 'cas':
                # To double check if the CAS number is correct:
                # using pubchem api, get a list of synonym. The result is a list of dict.
                # choose the first result and check all values for 'Synonym' key:
                synonyms = pcp.get_synonyms(cid)[0]['Synonym']
                # print('List of synonyms is: {}'.format(synonyms))
                exact_match = identifier in synonyms

            elif identifier_type in ['inchi', 'inchikey']:
                # Lookup inchi and inchikey returned by Pubchem:
                lookup_result = pcp.get_properties(['inchi', 'inchikey'], identifier, identifier_type)
                # print('lookup_result is: {}'.format(lookup_result))

                if identifier_type == 'inchi':
                    # print(lookup_result[0].get('InChI', False))
                    # print(f'input:\n{identifier}')
                    exact_match = (identifier == lookup_result[0].get('InChI', False))
                    # print(exact_match)
                
                elif identifier_type == 'inchikey':
                    exact_match = (identifier == lookup_result[0].get('InChIKey', False))


            if not exact_match:
                if debug:
                    print(f'Exact match between input and Pubchem return value? {identifier in synonyms}')
                raise ValueError('This is not an exact match on Pubchem!')

            '''
            get url from Pubchem to get pka lookup result
            'XML' can be replaced with 'JSON' but it is harder to parse later on
            for more info about Pubchem output types: https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest$_Toc494865558
            '''
            pka_lookup_result_xml = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{}/XML?heading=Dissociation+Constants'.format(cid)

            # Get the html request info using CID number from pubchem
            r = requests.get(pka_lookup_result_xml, headers=headers, timeout=15)
            # Check to see if give OK status (200) and not redirect
            if r.status_code == 200 and len(r.history) == 0:
                # print(r.text)
                # Use python XML to parse the return result
                tree = ET.fromstring(r.text)
            
                # Get the XML tree of <Information> only
                info_node = tree.find('.//*{http://pubchem.ncbi.nlm.nih.gov/pug_view}Information')
        #         print(info_node)
        #         print(list(child for child in info_node.iter()))

                # Get the pKa reference:
                original_source = info_node.find('{http://pubchem.ncbi.nlm.nih.gov/pug_view}Reference').text
                # Get the pKa result:
                pka_result = info_node.find('.//*{http://pubchem.ncbi.nlm.nih.gov/pug_view}String').text
                pka_result = re.sub(r'^pKa = ', '', pka_result)    # remove 'pka = ' part out of the string answer
                # print(pka_result)
                # print(original_source)
                
                return {
                    'input': identifier,
                    'source': lookup_source,
                    'Pubchem CID': cid,
                    'pka': pka_result,
                    'reference': original_source
                }
            else:
                raise RuntimeError('pKa not found in Pubchem.')
        
        else: 
            raise RuntimeError('Compound not found in Pubchem.')

    # except ValueError as error:
    #     if debug:
    #         traceback_str = ''.join(traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__))
    #         print(traceback_str)
    #     # return {
    #     #     'input': identifier,
    #     #     'source': lookup_source,
    #     #     'Pubchem CID': None,
    #     #     'pka': None,
    #     #     'reference': None
    #     # }
    #     return None

    except Exception as error:
        if debug:
            traceback_str = ''.join(traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__))
            print(traceback_str)

        # # Advice user about turning on debug mode for more error printing
        # print('\n\n(Optional): you can turn on debug mode (more error printing during structure search) using the following command:')
        # print('python src/pka_lookup_pubchem.py  --debug\n')

        # cid = cid or None
        # return {
        #     'input': identifier,
        #     'source': lookup_source,
        #     'Pubchem CID': cid,
        #     'pka': None,
        #     'reference': None
        # }

        return None


if __name__ == "__main__":
    # cas_nr = '64-19-7'    # acetic acid   >>> pKa = 4.76 at 25 °C
    # cas_nr = '75-75-2'    # methanesulfonic acid   >>> pKa = -1.86
    cas_nr = '2950-43-8'    # Hydroxylamine-O-sulfonic acid, no result
    # cas_nr = '2687-12-9'
    # print(pka_lookup_pubchem(cas_nr))
    print(pka_lookup_pubchem(cas_nr, 'cas'))



    # smiles_string = 'C1=CC(=CC=C1F)S'
    # smiles_string = 'OC=1(N(N=C(C=1)C2(=CC=CC=C2))C)'
    smiles_string = 'OC1=CC=CC=C1'

    # # Look up pKa using pka_lookup_pubchem():
    # print(f'pKa from Pubchem using smiles: {pka_lookup_pubchem(smiles_string)}')
    # print(f'pKa from Pubchem using smiles: {pka_lookup_pubchem(smiles_string, "smiles")}')


    inchi_string = 'InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,13H,1H3'    # this is NOT exact match from Pubchem return search
    # inchi_string = 'InChI=1S/C10H10N2O/c1-12-10(13)7-9(11-12)8-5-3-2-4-6-8/h2-7,11H,1H3'    # this is an exact match from Pubchem return search

    # print(f'pKa from Pubchem using smiles: {pka_lookup_pubchem(inchi_string)}')
    # print(f'pKa from Pubchem using smiles: {pka_lookup_pubchem(inchi_string, "smiles")}')    # this function call has wrong 'namespace' (should be 'inchi', not 'smiles'). Therefore, return Pubchem CID even though it is not an exact match.
    # print(f'pKa from Pubchem using smiles: {pka_lookup_pubchem(inchi_string, "inchi")}')

    inchikey_string = 'OKKJLVBELUTLKV-UHFFFAOYSA-N'    # methanol
    # print(f'pKa from Pubchem using InChIKey:\n{pka_lookup_pubchem(inchikey_string, "inchikey")}')