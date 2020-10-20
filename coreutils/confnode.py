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

def get_capabilities(conn_return):
    caps = conn_return.getCapabilities()
    return caps

# Get the Node max VCPU's
def get_getmaxvcpus(conn_return):
    vcpus = conn_return.getMaxVcpus(None)
    return vcpus


def get_info(conn_return):
    nodeinfo = conn_return.getInfo()
    # It returns the list of items.
    return nodeinfo


def get_libversion(conn_return):
    ver = conn_return.getLibVersion()

    return str(ver)

# Get the Node Hostname
def get_hostname(conn_return):
    hostName = conn_return.getHostname()
    return hostName

# Get the Free Memory Availabe on Node
def get_freememory(conn_return):
    mem = conn_return.getFreeMemory()
    return mem

def get_memoryparameters(conn_return):
    buf = conn_return.getMemoryParameters()
    return buf

def get_sysinfo(conn_return):
    xmlInfo = conn_return.getSysinfo()
    return xmlInfo

def get_cpumap(conn_return):
    map = conn_return.getCPUMap()
    cpu = str(map[0])
    available = str(map[1])
    return cpu, available

def get_cpustats(conn_return):
    stats = conn_return.getCPUStats(0)
    return stats

def get_cpumodel(conn_return):
    models = conn_return.getCPUModelNames('x86_64')
    return models

def get_os():
    system = platform.system()
    arch = platform.architecture()
    mach = platform.machine()
    nname = platform.node()
    rel = platform.release()
    python_verison = platform.python_version()
    dist = ''.join(distro.linux_distribution())
    ret_os = distro.distro_release_info()
    return ret_os

def get_kernel_version():
    kernel_ver = platform.release()
    return kernel_ver

def get_uptime():
    uptime_seconds = uptime.uptime()
    uptime_string = str(timedelta(seconds=uptime_seconds))
    return uptime_string

def get_ipaddress():
    ipaddr = socket.gethostbyname(socket.gethostname())
    return ipaddr

def get_python_version():
    py_ver = platform.python_version()
    return py_ver
