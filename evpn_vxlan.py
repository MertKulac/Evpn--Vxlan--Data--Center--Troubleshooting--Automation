from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from ttp import ttp
import json

with open('show_vxlan_flood_vte.txt') as f:
    lines = f.readlines()
    lines = "".join(lines)
    data_to_parse = lines.strip()
    print(data_to_parse)

#data_to_parse = conn.send_command_timing('show vxlan flood vte')

ttp_template = """
{{VLAN}}                           {{VTEP1}}    {{VTEP2}}    {{VTEP3}}  
"""

# create parser object and parse data using template:
parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

results = parser.result(format='json')[0]
print(results)

result = json.loads(results)
print(result[0])
print(result[0]["VLAN"])

-----------------------------------------------------------------------------------------

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from ttp import ttp
import json

with open('show_vxlan_address-table.txt') as f:
    lines = f.readlines()
    lines = "".join(lines)
    data_to_parse = lines.strip()
    print(data_to_parse)

#data_to_parse = conn.send_command_timing('show vxlan address-table')

ttp_template = """
  {{vlan}}  {{Mac-Address}}  {{type}}     {{port}}  {{vtep}}     {{move}}       {{time}} {{ago}}
"""

# create parser object and parse data using template:
parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

results = parser.result(format='json')[0]
print(results)

result = json.loads(results)
print(result[0])





