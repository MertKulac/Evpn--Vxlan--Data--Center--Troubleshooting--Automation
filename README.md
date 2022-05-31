# Data Center Troubleshooting Automation
Network automation works with show commands  used to solve customer problems in a data center network.

# Show Outputs
show vxlan flood vte => Vlan list the customer is connected to and corresponding VTEPs

show vxlan address-table => Mac-addresses learned over VXLAN and which VTEPs they belong to

show bgp evpn route-type imet => VTEP IPs and Route Distinguisher values learned with Route type3

show bgp evpn route-type mac-ip => Mac-address list learned in EVPN
 
# Network Design
![image](https://user-images.githubusercontent.com/96883175/167458552-da8cbeae-f4e3-433a-a416-6419ff3e8deb.png)
