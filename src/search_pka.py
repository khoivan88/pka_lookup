# import csv
import json
import sys
import traceback
from functools import partial
from typing import Dict, List, Optional, Tuple

from pka_lookup_pubchem import pka_lookup_pubchem
from tinydb import Query, TinyDB
from tinydb.middlewares import CachingMiddleware
from tinydb.storages import JSONStorage


debug = False


# Create print alias to pretty print a dict (sorted keys, indent)
def pprint(nested_element):
    """Pretty printing a nested element such as dict"""

    style = partial(json.dumps, indent=4, sort_keys=True, ensure_ascii=False)
    print(style(nested_element))


def search_pka(identifier: str, database) -> Optional[List[Tuple[Dict]]]:
    """Search for pKa in current local database, if not found
     then search Pubchem. If result is found from Pubchem, then 
     add to the local database
    
    Parameters
    ----------
    identifier : str
        search string. Could be one of (ranked likely search)
        - CAS number ~ InChIKey ~ InChI > IUPAC name >> SMILES
    database : tinyDB tiny.database object
        the name of the database the search query need

    Returns
    -------
    Optional[List[Tuple[Dict]]]: either
        - The record(s) found in local database in the following format:
            [
                (record1_id, record1 [Dict]),
                (record2_id, record2 [Dict]),
                ...
            ]
        - The record found in Pubchem: i.e.
            {"Canonical_SMILES": "CO",
            "IUPAC_Name": "methanol",
            "InChI": "InChI=1S/CH4O/c1-2/h2H,1H3",
            "InChIKey": "OKKJLVBELUTLKV-UHFFFAOYSA-N",
            "Isomeric_SMILES": "CO",
            "Pubchem_CID": "887",
            "Substance_CASRN": "67-56-1",
            "pKa": "15.3",
            "reference": "Serjeant, E.P., Dempsey B.;...",
            "source": "Pubchem"}
        - None: if not found any

    """
    global debug

    if len(sys.argv) == 2 and sys.argv[1] in ['--debug=True', '--debug=true', '--debug', '-d']:
        debug = True

    try:
        # Search local DB first:
        db_result = search_db(identifier=identifier, database=db)

        if db_result:
            # return db_result
            return [record for _, record in db_result]

        # If record(s) NOT found, search in Pubchem
        elif not db_result:
            # Get pubchem result
            pubchem_result = pka_lookup_pubchem(identifier)

            # Get pubchem result InChIKey
            pubchem_result_inchikey = pubchem_result.get('InChIKey') if pubchem_result else None
            
            # Add pubchem result (if found) into local DB:
            if pubchem_result_inchikey:
                '''Use pubchem_result_inchikey to search in current db:
                A bit redundant to check if current DB has the entry again 
                but this is for EXACT match'''
                current_db_result = search_db(identifier=pubchem_result_inchikey, database=db)
                record_existed = False
                if current_db_result:
                    for db_id, result in current_db_result:
                        if pubchem_result == result:
                            # Do not add into current db
                            if debug:
                                print('Will not add into current DB')    # for trouble shooting
                            record_existed = True
                            break
                
                # Add record from pubchem
                if not record_existed:
                    if debug:
                        print('Will add into current DB')    # for trouble shooting
                        # print('Exiting record id with same InChIKey: {}'.format(db_id))    # for trouble shooting

                    # Add into current DB
                    db.insert(pubchem_result)
                    return pubchem_result
    
    except Exception as error:
        if debug:
            traceback_str = ''.join(traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__))
            print(traceback_str)

        return None

                   
def search_db(identifier: str, database) -> Optional[List[Tuple[Dict]]]:
    """Return a list of (result'ID, result) from pka search using local database 
    
    Parameters
    ----------
    identifier : str
        search keywords. Could be one of (ranked likely search)
        - CAS number ~ InChIKey ~ InChI > IUPAC name >> SMILES 
    database : tinyDB tiny.database object
        the name of the database the search query need
    
    Returns
    -------
    Optional[List[Tuple[Dict]]]
        The record(s) found in local database in the following format:
            [
                (record1_id, record1 [Dict]),
                (record2_id, record2 [Dict]),
                ...
            ]
        None: if not found any
    """

    if identifier and database:
        results = database.search(
                    (Query()['Substance_CASRN'] == identifier) | 
                    (Query()['IUPAC_Name'] == identifier) | 
                    (Query()['InChI'] == identifier) | 
                    (Query()['InChIKey'] == identifier) |
                    (Query()['Original_SMILES'] == identifier) | 
                    (Query()['Structure_SMILES'] == identifier) |
                    (Query()['Canonical_SMILES'] == identifier) | 
                    (Query()['Isomeric_SMILES'] == identifier)
                )
        return [(record.doc_id, record) for record in results]


if __name__ == "__main__":
    # Access local tinyDB
    db = TinyDB('data/tinydb_db.json', 
                sort_keys=True, 
                indent=4, 
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
        if debug:
            traceback_str = ''.join(traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__))
            print(traceback_str)

    finally:
        # Because CachingMIddleware is used, db.close() is required to save to disk after some operations!
        # db.storage.flush()
        db.close()
