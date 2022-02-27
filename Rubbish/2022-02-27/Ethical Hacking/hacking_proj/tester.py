import json

with open('port_scan_results.json', 'r') as f:
    json_file = f.read()

nm_scan = json.loads(json_file)
# v = nm_scan.get("scan").get("192.168.1.209").get("tcp")
# v_keys = list(v.keys())
# print(v_keys)

# for i in range(len(v_keys) - 1):
#     for x in range(len(v.get(v_keys[i]))-1):
#         if v.get(v_keys[i][x]) == '':
#             print(f'Empty Column : {v_keys[i]}')

port_number = "21"
print(nm_scan.get("scan").get("192.168.1.209").get("tcp").get(port_number))
