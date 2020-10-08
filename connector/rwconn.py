'''
Class for intelli Agent libvirt operations

Author : Dhanasekara Pandian
Email  : sekar5in@quehive.com
CopyRights : All Rights are Reserved

'''

#Global Import
import pprint
import sys
import libvirt


class RWConnection:
    """Read Write Connection will attempt to open a connection for full read-write access. It does not have any
    scope for authentication callbacks to be provided, so it will only succeed for connections where
    authentication can be done based on the credentials of the application.
    """

    def __init__(self):
        self.conn = libvirt.open('qemu:///system')

    def connect(self):
        if self.conn is None:
            e = "Failed to open readwrite connection to qemu:///system"
            print(e, file=sys.stderr)
            return e

    def disconnect(self):
        """A connection must be released by calling the close method of the virConnection class when no
        longer required. Connections are reference counted objects, so there should be a corresponding call
        to the close method for each open function call.

        The open function call should have a matching close, and all other references will be released after 
        the corresponding operation completes.
        """
        self.conn.close()
        return 255
