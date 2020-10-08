
'''
This is Class for ycn agent libvirt Guest Monitoring

Author : Dhanasekara Pandian
Email  : sekar5in@gmail.com
CopyRights : All Rights are Reserved
'''

import os
from connector import roConn
from coreutils.watcher import DomainStatus


# Boiler Plate
if __name__ == '__main__':
    print("Current Working Directory :", os.getcwd())
    
    # Ensure read write call is running with administrator privileges
    conn = DomainStatus.DomainStatus('ro')

    # Connection
    conn_obj, conn_return = conn.connection()

    # disconnection
    conn.disconnection(conn_obj)







 