"""
Class for intelli Agent libvirt Domain operations

Author : Dhanasekara Pandian
Email  : sekar5in@gmail.com
CopyRights : All Rights are Reserved
"""


# Global Import
import sys


def domain_by_id(conn,domain_id):
    dom = conn.lookupByID(domain_id)
    return dom


def domain_by_name(conn, domain_name):
    dom = conn.lookupByName(domain_name)
    if dom is None:
        print('Failed to find the domain ' + domain_name, file=sys.stderr)

    id = dom.ID()
    if id == -1:
        print("Not running domain ", domain_name)
    else:
        print(f"Domain {domain_name} Running and id is {str(id)}")
    return dom


def domain_by_uuid(conn, domain_uuid):
    dom = conn.lookupByUUID(domain_uuid)
    return dom

