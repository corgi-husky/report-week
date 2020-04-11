import sys
#from mn_wifi.link import wmediumd, WifiDirectLink
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

def topology(args):

    "Create a network."
    net=Mininet_wifi()
    info( "*** Creating nodes\n")
    h0 = net.addHost('h0',ip='10.0.0.1/8')

    sta0 = net.addStation('sta0',ip='10.0.0.2/8',position='20,40,0')
    ap1 = net.addAccessPoint( 'ap1', ssid= 'ssid_1', mode= 'g', channel= '1',position='30,50,0')
    ap2 = net.addAccessPoint( 'ap2', ssid= 'ssid_2', mode= 'g', channel= '1',position='10,20,0')

    s0 = net.addController('s0')

    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4.5)

    info ( "*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    

    print "*** Associating and Creating links"


    net.addLink(s0, ap1)
    net.addLink(s0, ap2)
    

    net.addLink(s0, h0)

    #net.addLink(sta0,intf='sta0-wlan0',ssid='ssid_0')
    #net.addLink(sta0,intf='sta0-wlan1',ssid='ssid_1')
    
    #net.addLink(ap1, sta0)
    #net.addLink(ap2, sta0)
    net.addLink(ap1, h0)
    net.addLink(ap2, h0)

    if '-p' not in args:
        net.plotGraph(max_x=100, max_y=100)

    net.setMobilityModel(time=0, model='RandomWayPoint', max_x=120, max_y=120,
                         min_v=0.3, max_v=0.5, seed=1, ac_method='ssf')
    

    info( "*** Starting network\n")
    net.build()
    #h0.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')

    #h0.setIP('192.168.0.1/24',intf='h0-wlan0')
    #c0.setIP('10.0.0.3/8', intf='c0-eth2')
    s0.start()
    ap1.start([s0])
    ap2.start([s0])
    

    info( "*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology(sys.argv)
