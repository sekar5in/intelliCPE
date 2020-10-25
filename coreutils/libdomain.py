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
from xml.dom import minidom


def lookup_by_name(conn, domain_name):
    dom = conn.lookupByName(domain_name)
    if dom is None:
        print('Failed to find the domain id ' + domain_name, file=sys.stderr)

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
    print("type", dname.getType())
    print("name", dname.getName())
    print("id", dname.getID())
    print("getOSType", dname.getOSType())
    print("hostname", dname.getHostname())
    print("getHypervisorVersion", dname.getHypervisorVersion('null'))
    '''
    tree = ElementTree.fromstring(dom.XMLDesc())
    iface = tree.find('devices/interface/target').get('dev')
    io_stats = dom.interfaceStats(iface)
    disk_path = domian_disk(dom)
    rd_req, rd_bytes, wr_req, wr_bytes, err = dom.blockStats(disk_path)

    dict_value = {"domain_id": domain_id, "status": const.VMSTATUS[status],
                  "state": const.VMSTATE[state], "reason": reason,
                   "name": dname.name(), "os": os_type, "guest_os": "",
                  "max_mem": maxmem, "memory": mem, "mem_stats": mem_stats,
                  "max_cpu": max_cpu, "cpu": cpus, "cpu_time": cput, "cpu_stats": cpu_stats,
                  "io_stats": {"iface_name": iface,
                               "read_bytes":io_stats[0],
                               "read_packets":io_stats[1],
                               "read_errors":io_stats[2],
                               "read_drops":io_stats[3],
                               "wrtn_bytes":io_stats[4],
                               "wrtn_packets":io_stats[5],
                               "wrtn_errors":io_stats[6],
                               "wrtn_drops":io_stats[7]
                               },
                  "image_path": disk_path,
                  "disk_stats": {"read_req": rd_req, "bytes_read": rd_bytes,
                                 "write_req": wr_req, "bytes_wrote": wr_bytes,
                                 "no_of_errors": err
                                }
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
    disk_path = domian_disk(dom)
    #print(disk_path)
    
    if id == -1:
        # print("Not running domain ", domain_name)
        dict_value = {"id": None, "status": const.VMSTATUS[status],
                      "state": const.VMSTATE[state], "reason": reason,
                      "image_path": disk_path
                      }
    else:
        dict_value = {"id": None, "status": const.VMSTATUS[status],
                      "state": const.VMSTATE[state], "reason": reason,
                      "image_path": disk_path
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


def domian_disk(dom):

    raw_xml = dom.XMLDesc(0)
    xml = minidom.parseString(raw_xml)
    #print(xml)
    diskTypes = xml.getElementsByTagName('disk')
    #print(diskTypes)
    for diskType in diskTypes:
        #print('disk: type=' + diskType.getAttribute('type') + ' device = '+diskType.getAttribute('device'))
        if diskType.getAttribute('device') == 'disk':
            diskNodes = diskType.childNodes
            for diskNode in diskNodes:
                if diskNode.nodeName[0:1] != '#':
                    #print(' ' + diskNode.nodeName)
                    for attr in diskNode.attributes.keys():
                        if attr == 'file':
                            #print(''+diskNode.attributes[attr].name+' = '+ diskNode.attributes[attr].value)
                            disk_path = diskNode.attributes[attr].value
                            return disk_path