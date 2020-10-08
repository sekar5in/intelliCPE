
'''
This is Class for ycn agent libvirt Guest Monitoring

Author : Dhanasekara Pandian
Email  : sekar5in@gmail.com
CopyRights : All Rights are Reserved
'''

import os
from coreutils import domconn, domaction

# Boiler Plate
if __name__ == '__main__':
    print("Current Working Directory :", os.getcwd())

    # Ensure read write call is running with administrator privileges
    conn = domconn.DomainStatus('ro')

    # Connection
    conn_obj, conn_return = conn.connection()

    # list all registered domains
    action_obj = domaction.DomainAction(conn_return)
    print("domainstatus:", action_obj.domain_status())

    # disconnection
    conn.disconnection(conn_obj)







 