# 1. Reconnaissance
# 2. Scanning
# 3. Gaining Acess(Exploitation)
# 4. Maintaning Access(Persistence)
# 5. Post Exploitation
# 6. Clearing tracks

import json
import os
import pprint
import sys

import nmap

from print_status import fail, info, successful


# NOTE Information Gathering
def info_get(target_ip):
    tool = 'whatweb'
    successful(f'Gathering Information With {tool}')
    info('This is just for your information... The Program doesnt not use any of this')
    os.system(f'whatweb {target_ip} -a 3 -v')
    return True

# NOTE Recconisance & Scanning


def reconAndscan(target_ip, nmap_port_range, nmap_scan_types, nmap_file_save):
    v = os.system(f'ping {target_ip} -c 3')

    if v != 0:  # Host Is Not Active
        fail('Host Is Not Active')
    else:
        successful('Host Is Active')

    nm = nmap.PortScanner()
    nm_scan = nm.scan(target_ip, f'1-{str(nmap_port_range)}', nmap_scan_types)
    print('NM: ', nm, '\n\n')

    results = json.dumps(nm_scan, sort_keys=False, indent=4)
    print(results)
    print(type(results))

    with open(nmap_file_save, 'w') as f:
        json.dump(nm_scan, f)
    return nm_scan


# NOTE  Vulnerability Analysis
def vulnerability(scan_results, port_number, method='searchsploit', scan_json_file=True):
    # TODO Add as many ways as you can...
    # 1) Nmap Scripts {Python Library Or OS}- https://nmap.org/book/man-nse.html
    # 2) Google {Web Scraping... CVE, Etc.}- https://www.google.com/
    # 3) Searchsploit {??} - https://www.exploit-db.com/searchsploit
    # 4) Nessus {Wen Scraping Or API??}- https://www.tenable.com/products/nessus
    scan_results = scan_results

    with open('port_scan_results.json', 'r') as f:
        json_file = f.read()

    nm_scan = json.loads(json_file)
    port_number = str(port_number)
    port_info = nm_scan.get("scan").get(
        "192.168.1.209").get("tcp").get(port_number)
    # {'state': 'open', 'reason': 'syn-ack', 'name': 'ftp', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}
    print('\n\n\n\n\n')
    print(port_info)
    print('\n\n\n\n\n')
    name = port_info.get("name")
    searchSploitResult = os.system(f'searchsploit {name}')
    print(searchSploitResult)
    return searchSploitResult


def main(target_ip, nmap_port_range=65534, nmap_scan_types='-sS', nmap_file_save='port_scan_results.json'):
    # TODO UI: Terminal Or Flask (Wesbite), But Make It Better
    # NOTE Requirments Verification
    required = {
        'Hacking Tools': [
            'Test', 'e3'
        ],
        'Python libraries': [
            'Test', 'e3'
        ]}
    for i in range(len(required)):
        print(f'{list(required.keys())[i]}: {list(required.values())[i]}')
    # TODO Add A System Where it downloads stuff that is not there automatically
    print('\n\n')

    sys.argv = sys.argv
    type_exploit = sys.argv[1]
    infoGather = info_get(target_ip)
    nm_scan = reconAndscan(target_ip, nmap_port_range,
                           nmap_scan_types, nmap_file_save)
    if type_exploit == 'advance':
        vun = vulnerability(nm_scan, 21)
    else:
        vun = False

    return infoGather, nm_scan, vun


if __name__ == '__main__':
    infoGather, nm_scan, vun = main('192.168.1.209')
    print(nm_scan)
    print(vun)
    # nm_scan = main()
    # print('\n\n')
    # print(nm_scan.get("nmap"))
    # print(nm_scan.get("nmap").get("command_line"))
    # print('\n\n')
    # print(nm_scan.get("scan").get("192.168.1.209").get("tcp"))
    # print('\n\n')
