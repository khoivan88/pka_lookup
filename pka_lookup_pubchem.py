#!/usr/bin/env python
# coding: utf-8

"""
Author: Khoi Van

This script takes a CAS number and look up its pKa (dissociation constant) 
from Pubchem and return it if found; return None, otherwise


"""

import sys
import traceback
import xml.etree.ElementTree as ET
from typing import Optional

import pubchempy as pcp  # https://pubchempy.readthedocs.io/en/latest/guide/gettingstarted.html
import requests

debug = False


def pka_lookup_pubchem(cas_nr: str) -> Optional[str]:
    global debug

    if len(sys.argv) == 2 and sys.argv[1] in ['--debug=True', '--debug=true', '--debug', '-d']:
        debug = True

    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; CentOS; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

        # print('Searching Pubchem...')

        # Using pubchem api for python
        # Getting CID number, the result of this, by default is exact match. The result is returned as a list.
        # cid = pcp.get_cids(cas_nr, 'name', 'substance', list_return='flat')
        cid = pcp.get_cids(cas_nr, 'name')
        # print(cid)

        #  this api return an empty list if it cannot find cas_nr. This is to check if pubchem has this chemical.
        if len(cid) > 0:
            # if Pubchem found the result, get the first result of the list
            cid = cid[0]
            # print('Compound ID (CID) from PubChem is: {} and type is: {}'.format(cid, type(cid)))

            # To double check if the CAS number is correct:
            # using pubchem api, get a list of synonym. The result is a list of dict.
            # choose the first result and check all values for 'Synonym' key:
            synonyms = pcp.get_synonyms(cid)[0]['Synonym']
        #     print('List of synonyms is: {}'.format(synonyms))

        if cas_nr not in synonyms:
            raise ValueError('\tThis is not an exact match!')

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

        pka_result = ''
            
        for node in tree.iter('{http://pubchem.ncbi.nlm.nih.gov/pug_view}String'):
            # print(node.text)
            pka_result = node.text

        return pka_result
    
    except Exception as error:
        if debug:
            traceback_str = ''.join(traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__))
            print(traceback_str)

    finally:
        # Advice user about turning on debug mode for more error printing
        print('\n\n(Optional): you can turn on debug mode (more error printing during structure search) using the following command:')
        print('python oe_find_sds/find_sds.py  --debug\n')


if __name__ == "__main__":
    cas_nr = '64-19-7'    # acetic acid   >>> pKa = 4.76 at 25 °C
#     cas_nr = '75-75-2'    # methanesulfonic acid   >>> pKa = -1.86
    # cas_nr = '2950-43-8'    # Hydroxylamine-O-sulfonic acid, no result

    print(pka_lookup_pubchem(cas_nr))
