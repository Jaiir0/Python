import subprocess 

result = subprocess.run('ipconfig',capture_output=True )
result = str(result)
print(result)
'''
pos = result.find('IPv4')
pos2 = result.find(':',pos)         #exemplo 1 
pos3 = result.find('\\r\\n',pos2)

print(pos3,'bbb')
print(pos2,'aaaa')
print (result[pos2+2:pos3])'''

pos = 0
pos1 = result.find('\\r\\n',pos)
while pos1 != -1:
    print(result[pos:pos1])           #exemplo2

    pos = pos1+4
    pos1 = result.find('\\r\\n',pos)
