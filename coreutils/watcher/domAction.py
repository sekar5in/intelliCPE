#!/usr/bin/python3

'''
This is Class for ycn agent libvirt Guest Monitoring

Author : Dhanasekara Pandian
Email  : sekar5in@gmail.com
CopyRights : All Rights are Reserved
'''

#Global Import
import pprint
import sys
import libvirt
from connector.roConn import ROConnection
from connector.rwConn import RWConnection

"""
Available Constants

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


class DomainAction:

    def __init__(self, conn_obj):
        self.conn_obj = conn_obj

    def list_all_domains(self):
        domainNames = self.conn_obj.listDefinedDomains()
        print(domainNames)

