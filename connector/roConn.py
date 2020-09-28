"""
Class for intelli Agent libvirt operations

Author : Dhanasekara Pandian
Email  : sekar5in@quehive.com
CopyRights : All Rights are Reserved

"""

#Global Import
import pprint
import sys
import libvirt


class ROConnection:
    """Read Only Connection will attempt to open a connection for read-only access. Such a
    connection has a restricted set of method calls that are allowed, and is typically useful for monitoring
    applications that should not be allowed to make changes.
    """
    def __init__(self):
        try:
            self.conn = libvirt.openReadOnly('qemu:///system')
            if self.conn == None:
                e = "Failed to open connection to qemu:///system"
                print(e, file=sys.stderr)
                return 2, e
        except Exception as e:
            return 1, e

    def is_alive(self):
            alive = self.conn.isAlive()
            return alive
    
    def get_issecure(self):
        isSecure = self.conn.isSecure()
        return isSecure

    def get_version(self):
        ver = self.conn.getVersion()
        return ver
    
    def get_isencrypted(self):
        encrypt_status = self.conn.isEncrypted()
        return encrypt_status

    def close(self):
        """A connection must be released by calling the close method of the virConnection class when no
        longer required. Connections are reference counted objects, so there should be a corresponding call
        to the close method for each open function call.

        The open function call should have a matching close, and all other references will be released after 
        the corresponding operation completes.
        """
        self.conn.close()
        exit(0)