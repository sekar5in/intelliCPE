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

class DomainAction:

    def __init__(self, conn_return):
        self.conn_return = conn_return

    def domain_status(self):
        domainsstatus = {"configured_domain": self.configured_domain(),
                         "active_domain": self.active_domain(),
                         "inactive_domain": self.inactive_domain(),
                         "running_domain": self.running_domain(),
                         "paused_domain": self.paused_domain(),
                         "stopped_domain": self.stopped_domain()
                         }
        json_data = dict_to_json(domainsstatus)
        return json_data

    def configured_domain(self):
        config_domains = self.conn_return.listAllDomains(0)
        if len(config_domains) != 0:
            return len(config_domains)
        else:
            return None

    def active_domain(self):
        active = self.conn_return.listAllDomains(VIR_CONNECT_LIST_DOMAINS_ACTIVE)
        if len(active) != 0:
            return len(active)
        else:
            return None

    def inactive_domain(self):
        inactive = self.conn_return.listAllDomains(VIR_CONNECT_LIST_DOMAINS_INACTIVE)
        if len(inactive) != 0:
            return len(inactive)
        else:
            return None

    def running_domain(self):
        running = self.conn_return.listAllDomains(VIR_CONNECT_LIST_DOMAINS_RUNNING)
        if len(running) != 0:
            return len(running)
        else:
            return None

    def paused_domain(self):
        paused = self.conn_return.listAllDomains(VIR_CONNECT_LIST_DOMAINS_PAUSED)
        if len(paused) != 0:
            return len(paused)
        else:
            return None

    def stopped_domain(self):
        stopped = self.conn_return.listAllDomains(VIR_CONNECT_LIST_DOMAINS_SHUTOFF)
        if len(stopped) != 0:
            return len(stopped)
        else:
            return None

