import csv
import random
#

def randomMAC():
	mac = [ 0x00, 0x16, 0x3e,
		random.randint(0x00, 0x7f),
		random.randint(0x00, 0xff),
		random.randint(0x00, 0xff) ]
	return ':'.join(map(lambda x: "%02x" % x, mac))
#
with open('hostnames.csv', 'w') as host_csvfile:
    fieldnames = ['ip', 'host']
    host_writer = csv.DictWriter(host_csvfile, fieldnames=fieldnames)

    host_writer.writeheader()
    for i in range(0,254):
        for j in range(1,254):
            host_writer.writerow({'ip': '10.10.'+str(i)+'.'+str(j), 'host': 'Workstation'+str(i+j)})


with open("mac_address_table.csv",'w') as mac_csvfile:

    fieldnames = ['ip','mac']
    writer = csv.DictWriter(mac_csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(0,254):
        for j in range(1,254):
            writer.writerow({'ip': '10.10.'+str(i)+'.'+str(j), 'mac' : randomMAC()})

with open("switchport.csv",'w') as csvfile:
    fieldnames = ['mac address', 'switchport']
    sw_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    sw_writer.writeheader()
    for i in range(1,48):
        sw_writer.writerow({'mac address': randomMAC(), 'switchport':i})
