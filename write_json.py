import json

with open("sample.json", 'r') as fa:
    data = json.load(fa)
    for package_name, version in data.items():
        for ver, attributes in version.items():
            if ver == "5.3.20":
                print(ver)
                print(attributes["SourceUrl"])
                with open("json1.json", 'w') as fh:
                 json.dump(attributes, fh, indent=4)
                 
