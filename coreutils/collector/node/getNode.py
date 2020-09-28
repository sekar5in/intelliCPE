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


class NodeAdmin:
    """The getCapabilities method call can be used to obtain information about the capabilities of the
    virtualization host. If successful, it returns a Python string containing the capabilities XML (described
    below). If an error occurred, None will be returned instead.
    """
    
    def __init__(self, connection):
        self.conn = connection

    def get_capabilities(self):
        caps = self.conn.getCapabilities()
        return caps
    
    def get_getmaxvcpus(self):
        vcpus = self.conn.getMaxVcpus(None)
        return str(vcpus)
    
    def get_info(self):
        nodeinfo = self.conn.getInfo()
        # It returns the list of items.
        return nodeinfo

    def get_libversion(self):
        ver = self.conn.getLibVersion()
        return str(ver)
    
    def get_hostname(self):
        hostName = self.conn.getHostname()
        return hostName

    def get_freememory(self):
        mem = self.conn.getFreeMemory()
        return mem
    
    def get_memoryparameters(self):
        buf = conn.getMemoryParameters()
        return buf
    
    def get_sysinfo(self):
        xmlInfo = conn.getSysinfo()
        return xmlInfo
    
    def get_cpumap(self):
        map = conn.getCPUMap()
        cpu = str(map[0])
        available = str(map[1])
        return cpu, available

    def get_cpustats(self):
        stats = conn.getCPUStats(0)
        return stats

    def get_cpumodel(self):
        models = conn.getCPUModelNames('x86_64')
        return models
    
    
