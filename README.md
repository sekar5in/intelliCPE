# intelliCPE
IntelliCPE Python Agent

 def is_alive(self):
            alive = self.conn.isAlive()
            return alive
    
    def get_issecure(self):
        isSecure = self.conn.isSecure()
        return isSecure

    def get_version(self):
        ver = self.conn.getVersion()
        return ver
    
    def get_isencrypted(self):
        encrypt_status = self.conn.isEncrypted()
        return encrypt_status
         
    def list_domain(self):
        host = self.conn.getHostname()
        print("Hostname :" + host)

    def listdomain(self):
        caps = self.conn.getCapabilities()
        print("capabilities:\n"+caps)
        
        host = self.conn.getHostname()
        print("Hostname :"+ host)

        vcpus = self.conn.getMaxVcpus(None)
        print('Maximum support virtual CPUs per Guest: '+str(vcpus))

        nodeinfo = self.conn.getInfo()
        print('Model: '+str(nodeinfo[0]))
        print('Memory size: '+str(nodeinfo[1])+'MB')
        print('Number of CPUs: '+str(nodeinfo[2]))
        print('MHz of CPUs: '+str(nodeinfo[3]))
        print('Number of NUMA nodes: '+str(nodeinfo[4]))
        print('Number of CPU sockets: '+str(nodeinfo[5]))
        print('Number of CPU cores per socket: '+str(nodeinfo[6]))
        print('Number of CPU threads per core: '+str(nodeinfo[7]))

        domainIDs = self.conn.listDomainsID()
        if domainIDs == None:
            print('Failed to get a list of domain IDs', file=sys.stderr)
        
        print("Active domain IDs:")
        if len(domainIDs) == 0:
            print('  None')
        else:
            for domainID in domainIDs:
                print('  '+str(domainID))
        
        

        domainIDs = self.conn.listDomainsID()
        print(domainIDs)

        domains = self.conn.listAllDomains(0)
        for d in domains:
            print("d", d.name())
            print("d", d.id())
            print("d", d.status())