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
import coreutils.confnode as nod
import coreutils.libdomain as ldom


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
        return domainsstatus

    def resource_status(self):
        node_info = nod.get_info(self.conn_return)

        nodestatus = {"vcpus": nod.get_getmaxvcpus(self.conn_return),
                          "nodename": nod.get_hostname(self.conn_return),
                          "freememory": nod.get_freememory(self.conn_return),
                          #"get_cpustats": nod.get_cpustats(self.conn_return),
                          #"get_capabilities": nod.get_capabilities(self.conn_return),
                          "model": node_info[0],
                          "memory": str(node_info[1]),
                          "no_of_cpus": node_info[2],
                          "mhz_of_cpus": node_info[3],
                          "no_of_numa_nodes": node_info[4],
                          "no_of_cpu_sockets": node_info[5],
                          "no_of_cpu_core_per_socket": node_info[6],
                          "no_of_cpu_threads_per_core": node_info[7],
                          "get_libversion": nod.get_libversion(self.conn_return),
                          "OS": nod.get_os(),
                          "kernel_ver": nod.get_kernel_version(),
                          "uptime": nod.get_uptime(),
                          "ipaddress": nod.get_ipaddress(),
                          "node_id": "",
                          "python_version":nod.get_python_version(),
                          "all_interfaces": nod.get_listInterfaces(self.conn_return),
                          "active_interfaces": nod.get_active_interfaces(self.conn_return)
                          #"get_sysinfo": nod.get_sysinfo(self.conn_return),
                          }
        json_data = dict_to_json(nodestatus)
        #print(resourcestatus)
        return nodestatus

    def stats(self):
        t_domain = dom.configured_domain(self.conn_return)
        vmstatus =  ldom.list_domain(self.conn_return)
        #print(statistics)
        return vmstatus


