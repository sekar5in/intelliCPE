#!/usr/bin/python3

"""
This is Class for ycn agent libvirt Guest Monitoring

Author : Dhanasekara Pandian
Email  : sekar5in@gmail.com
CopyRights : All Rights are Reserved
"""

# Global Import
from coreutils.constants import *
from coreutils.dataformat import dict_to_json
import coreutils.confdomain as dom


class DomainAction:

    def __init__(self, conn_return):
        self.conn_return = conn_return

    def domain_status(self):
        domainsstatus = {"configured_domain": dom.configured_domain(self.conn_return),
                         "active_domain": dom.active_domain(self.conn_return),
                         "inactive_domain": dom.inactive_domain(self.conn_return),
                         "running_domain": dom.running_domain(self.conn_return),
                         "paused_domain": dom.paused_domain(self.conn_return),
                         "stopped_domain": dom.stopped_domain(self.conn_return)
                         }
        json_data = dict_to_json(domainsstatus)
        return json_data