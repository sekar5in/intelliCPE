#!/usr/bin/python3

"""
This is Class for ycn agent libvirt Guest Monitoring

Author : Dhanasekara Pandian
Email  : sekar5in@gmail.com
CopyRights : All Rights are Reserved
"""

# Global Import
from coreutils.constants import *


def configured_domain(conn_return):
    config_domains = conn_return.listAllDomains(0)
    if len(config_domains) != 0:
        return len(config_domains)
    else:
        return None


def active_domain(conn_return):
    active = conn_return.listAllDomains(VIR_CONNECT_LIST_DOMAINS_ACTIVE)
    if len(active) != 0:
        return len(active)
    else:
        return None


def inactive_domain(conn_return):
    inactive = conn_return.listAllDomains(VIR_CONNECT_LIST_DOMAINS_INACTIVE)
    if len(inactive) != 0:
        return len(inactive)
    else:
        return None


def running_domain(conn_return):
    running = conn_return.listAllDomains(VIR_CONNECT_LIST_DOMAINS_RUNNING)
    if len(running) != 0:
        return len(running)
    else:
        return None


def paused_domain(conn_return):
    paused = conn_return.listAllDomains(VIR_CONNECT_LIST_DOMAINS_PAUSED)
    if len(paused) != 0:
        return len(paused)
    else:
        return None


def stopped_domain(conn_return):
    stopped = conn_return.listAllDomains(VIR_CONNECT_LIST_DOMAINS_SHUTOFF)
    if len(stopped) != 0:
        return len(stopped)
    else:
        return None
