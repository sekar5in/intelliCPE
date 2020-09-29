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
        e = "Failed to get a list of domain IDs"
        print(e, file=sys.stderr)
        return e

    if len(domainIDs) == 0:
        return None
    else:
        return str(domainID)
    
def domain_list_all_status():
    """
    VIR_CONNECT_LIST_DOMAINS_ACTIVE
    VIR_CONNECT_LIST_DOMAINS_INACTIVE
    VIR_CONNECT_LIST_DOMAINS_PERSISTENT
    VIR_CONNECT_LIST_DOMAINS_TRANSIENT
    VIR_CONNECT_LIST_DOMAINS_RUNNING
    VIR_CONNECT_LIST_DOMAINS_PAUSED
    VIR_CONNECT_LIST_DOMAINS_SHUTOFF
    VIR_CONNECT_LIST_DOMAINS_OTHER
    VIR_CONNECT_LIST_DOMAINS_MANAGEDSAVE
    VIR_CONNECT_LIST_DOMAINS_NO_MANAGEDSAVE
    VIR_CONNECT_LIST_DOMAINS_AUTOSTART
    VIR_CONNECT_LIST_DOMAINS_NO_AUTOSTART
    VIR_CONNECT_LIST_DOMAINS_HAS_SNAPSHOT
    VIR_CONNECT_LIST_DOMAINS_NO_SNAPSHOT
    """
    domains = conn.listAllDomains(0)
    if domains:
        #if len(domains) != 0:
            #for domain in domains:
            #    print('  '+domain.name())
            return domains
    else:
        return None

