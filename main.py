import yaml
from yaml.loader import SafeLoader

with open('verify_apache.yaml')as f:
    data =list(yaml.safe_load_all(f))

#print(data[1][0]["hosts"])
members = [{'name': 'Zoey', 'occupation': 'Doctor'},
           {'name': 'Zaara', 'occupation': 'Dentist'}]
with open('members.yaml','w')as f:
    data1=yaml.dump_all(members,f,sort_keys=False,default_flow_style=False)

print(data1)
