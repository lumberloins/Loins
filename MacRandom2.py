
#!/usr/bin/python


import random

def randomMAC():
	mac = [
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
		random.randint(0x00, 0xff),
		random.randint(0x00, 0xff),
		random.randint(0x00, 0xff) ]
	return ':'.join(map(lambda x: "%02x" % x, mac))


newMacAddr = randomMAC()
COMMAND = str('ifconfig urtwn0 ether ')

f = open( '/etc/start_if.urtwn0', 'w')
f.write(COMMAND)
f.write(newMacAddr)
f.write('\n')
f.close()






