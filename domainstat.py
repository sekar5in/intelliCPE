
'''
This is Class for ycn agent libvirt Guest Monitoring

Author : Dhanasekara Pandian
Email  : sekar5in@gmail.com
CopyRights : All Rights are Reserved
'''

import os
from connector import roConn
from coreutils.watcher import domConn
from coreutils.watcher import domAction

# Boiler Plate
if __name__ == '__main__':
    print("Current Working Directory :", os.getcwd())

    # Ensure read write call is running with administrator privileges
    conn = domConn.DomainStatus('ro')

    # Connection
    conn_obj, conn_return = conn.connection()

    # list all registered domains
    action_obj = domAction.DomainAction(conn_return)
    action_obj.list_all_domains()

    # disconnection
    conn.disconnection(conn_obj)







 