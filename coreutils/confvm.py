"""
Class for intelli Agent libvirt operations

Author : Dhanasekara Pandian
Email  : sekar5in@gmail.com
CopyRights : All Rights are Reserved

"""

import os
import sys
import platform
import distro
from datetime import timedelta
import uptime
import socket


def get_maxvcpu(dom):
    cpus = dom.maxVcpus()
    if cpus != -1:
        return cpus

