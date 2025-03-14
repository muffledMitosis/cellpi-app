from pySIM7020.src.Device import Device
from pySIM7020.src.TCP import TCP

device = Device()
tcp = TCP(device)
print(tcp.getDevice())
