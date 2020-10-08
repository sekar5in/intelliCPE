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


class DomainStatus:

    def __init__(self, connection_type):
        self.connection_type = connection_type

    def connection(self):
        con_type = str(str(self.connection_type).lower()).strip()
        if con_type == 'ro':
            print("Establishing read only connection")
            c = ROConnection()
            conn = c.connect()
            print("Connected")
            return c, conn

        elif con_type == 'rw':
            print("Establishing Read Write Connection")
            c = RWConnection()
            conn = c.connect()
            print("Connected")
            return c, conn

        else:
            print("Unknown connection request")
            c = None
            conn = None
            return c, conn

    @staticmethod
    def disconnection(c):
        try:
            if c is not None:
                print("Disconnecting from Established Connection...")
                c.disconnect()
                print("Disconnected")
        except Exception as e:
            print(e)
