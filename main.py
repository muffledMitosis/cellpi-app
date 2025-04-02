from pySIM7020.src.Device import Device
from pySIM7020.src.TCP import TCP
from pySIM7020.src.Socket import Socket

device = Device()
tcp = TCP(device)
print(tcp.getDevice())
print(device.getFirmwareVersion())

sock = Socket()
print(sock.getConnCommand())
