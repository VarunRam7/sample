import yaml
from yaml.loader import SafeLoader

with open('verify_apache.yaml')as f:
    data =yaml.load(f,Loader=SafeLoader)
    print(data)
