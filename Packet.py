import socket
#defines properties of a packet
class Packet:
	def __init__(self,fields):
		if fields == None:
			self.source = None
			self.dest = None
                        self.prot = 0
			self.timestamp = None
			self.size = 0
			self.key = None
		else:
			self.source = socket.inet_aton(fields[0])
			self.dest = socket.inet_aton(fields[1])
                        self.prot = int(fields[2]) 
                        self.timestamp = float(fields[3])
                        try:
                                self.size = int(fields[4])
                        except IndexError:
                                self.size = 0
                        else:
                                self.size = int(fields[4])
			if self.source < self.dest:
				self.key = self.source + self.dest
			else:
				self.key = self.dest + self.source
		
