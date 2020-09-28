'''
Class for intelli Agent libvirt Domain operations

Author : Dhanasekara Pandian
Email  : sekar5in@quehive.com
CopyRights : All Rights are Reserved

'''

#Global Import
import pprint
import sys
import libvirt



def domain_by_id(domain_id):
    dom = conn.lookupByID(domain_id)
    return dom

def domain_by_name(domain_name):
    dom = conn.lookupByID(domain_name)
    return dom

def domain_by_uuid(domain_uuid):
    dom = conn.lookupByUUID(domainUUID)
    return dom

def domain_list_by_id():
    domainIDs = conn.listDomainsID()
    if domainIDs == None:
        print('Failed to get a list of domain IDs', file=sys.stderr)
    
    print("Active domain IDs:")
    if len(domainIDs) == 0:
        print(' None')
    else:
        for domainID in domainIDs:
        print(' '+str(domainID))
    
