"""
Class for intelli Agent libvirt Domain operations

Author : Dhanasekara Pandian
Email  : sekar5in@gmail.com
CopyRights : All Rights are Reserved
"""


# Global Import
import sys
import coreutils.constants as const
import coreutils.confvm as conf
from xml.etree import ElementTree

def lookup_by_name(conn, domain_name):
    dom = conn.lookupByName(domain_name)
    if dom is None:
        print('Failed to find the domain id ' + id, file=sys.stderr)

    return dom


def domain_by_id(conn, domain_id):
    dom = conn.lookupByID(domain_id)
    if dom is None:
        print('Failed to find the domain id ' + domain_id, file=sys.stderr)

    domain_name = dom.name()
    status = dom.isActive()
    state, reason = dom.state()
    dname = lookup_by_name(conn, domain_name)
    max_cpu = conf.get_maxvcpu(dname)
    state, maxmem, mem, cpus, cput = dname.info()
    mem_stats = dom.memoryStats()
    cpu_stats = dom.getCPUStats(True)
    os_type = dname.OSType()
    
    '''
    tree = ElementTree.fromstring(dom.XMLDesc())
    iface = tree.find('devices/interface/target').get('dev')
    io_stats = dom.interfaceStats(iface)
    '''

    dict_value = {"domain_id": domain_id, "status": const.VMSTATUS[status],
                  "state": const.VMSTATE[state], "reason": reason,
                   "name": dname.name(), "os": os_type,
                  "max_mem": maxmem, "memory": mem, "mem_stats": mem_stats,
                  "max_cpu": max_cpu, "cpu": cpus, "cpu_time": cput, "cpu_stats": cpu_stats
                  #"hostname": dname.hostname()
                  }
    return domain_name, dict_value


def domain_by_name(conn, domain_name):
    dict_value = {}
    dom = conn.lookupByName(domain_name)
    if dom is None:
        print('Failed to find the domain ' + domain_name, file=sys.stderr)

    status = dom.isActive()
    state, reason = dom.state()
    id = dom.ID()

    if id == -1:
        # print("Not running domain ", domain_name)
        dict_value = {"id": None, "status": const.VMSTATUS[status],
                      "state": const.VMSTATE[state], "reason": reason
                      }
    else:
        dict_value = {"id": None, "status": const.VMSTATUS[status],
                      "state": const.VMSTATE[state], "reason": reason
                      }

    return domain_name, dict_value


def domain_by_uuid(conn, domain_uuid):
    dom = conn.lookupByUUID(domain_uuid)
    return dom


def list_domain(conn):
    vm_stat = {}
    # Inactive Domains
    domainNames = conn.listDefinedDomains()
    if len(domainNames) != 0:
        for domain_name in domainNames:
            dom_name, dict_value = domain_by_name(conn, domain_name)
            #max_cpu = conf.get_maxvcpu(conn, dom_name)
            #dict_value["max_cpu"] = max_cpu
            vm_stat[dom_name] = dict_value


    # Active Domains
    domainIDs = conn.listDomainsID()

    if len(domainIDs) != 0 and domainIDs is not None:
        for domainID in domainIDs:
            dom_name, dict_value = domain_by_id(conn, domainID)
            #max_cpu = conf.get_maxvcpu(conn, dom_name)
            #dict_value["max_cpu"] = max_cpu
            vm_stat[dom_name] = dict_value

    return vm_stat
