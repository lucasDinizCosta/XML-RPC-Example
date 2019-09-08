import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print("pow: " + str(s.pow(2,3)))  # Returns 2 **3 = 8
print("add: " + str(s.add(2,3)))  # Returns 2 + 3 = 5
print("mul: " + str(s.mul(5,2)))  # Returns 5 * 2 = 10
print("sub: " + str(s.sub(5,8)))  # Returns 5 - 8 = -3
print("div: " + str(s.div(16,2)))  # Returns 16 / 2 = 8.0

# Print list of available methods
print(s.system.listMethods())