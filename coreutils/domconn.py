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
from connector.roconn import ROConnection
from connector.rwconn import RWConnection


class DomainStatus:

    def __init__(self, connection_type):
        self.connection_type = connection_type

    def connection(self):
        con_type = str(str(self.connection_type).lower()).strip()
        if con_type == 'ro':
            print("Establishing read only connection")
            c = ROConnection()
            conn = c.connect()
            # print("Connected")
            return c, conn

        elif con_type == 'rw':
            print("Establishing Read Write Connection")
            c = RWConnection()
            conn = c.connect()
            # print("Connected")
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
                # print("Disconnected")
        except Exception as e:
            print(e)
