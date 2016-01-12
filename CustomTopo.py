'''
Coursera:
- Software Defined Networking (SDN) course
-- Module 3 Programming Assignment

Professor: Nick Feamster
Teaching Assistant: Muhammad Shahbaz
'''

from mininet.topo import Topo
from mininet.util import irange, dumpNodeConnections
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.log import setLogLevel

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        setLogLevel('info')
        host_cycle = 0
        switch_cycle = 0
        
        # Add your logic here ...
        coreSwitch = self.addSwitch('s1')
        for i in irange(1, fanout):
            switch = self.addSwitch('s%s' % (i+1))
            self.addLink(switch, coreSwitch, **linkopts1)
            aggreSwitch = switch
            for j in irange(1, fanout):
                switch = self.addSwitch('s%s' % (fanout+1+fanout*switch_cycle+j))
                self.addLink(switch, aggreSwitch, **linkopts2)
                edgeSwitch = switch
                for k in irange(1, fanout):
                    host = self.addHost('h%s' % (fanout*host_cycle+k))
                    self.addLink(host, edgeSwitch, **linkopts3)
                host_cycle += 1
            switch_cycle += 1
        
                    
topos = { 'custom': ( lambda: CustomTopo() ) }
