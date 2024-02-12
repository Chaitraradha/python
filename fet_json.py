import json
with open("json.json",'r') as fh:
    data = json.load(fh)
    for package_name, version in data.items():
        for ver, attributes in version.items():
            if ver == "5.3.13":
                print(ver)
                print(attributes["SourceUrl"])
                print(attributes["License"])

