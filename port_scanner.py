import socket
import re
import common_ports

def get_open_ports(target, port_range, verbose = False):
  l = []
  # Verify host
  if re.search('[a-zA-Z]',target):
    try:
      iname = socket.gethostbyname(target)
      sname = target      
    except:
      return 'Error: Invalid hostname'
  else:
    try:
      try:
        sname = socket.gethostbyaddr(target)[0]
      except:
        sname = socket.gethostbyname(target)
      iname = target
    except:
        return 'Error: Invalid IP address'      

  t = '\nPORT     SERVICE'

  # view ports open
  for port in range(port_range[0],port_range[1]+1,1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if (s.connect_ex((target, port)) == 0):
      l.append(port)
      t = t + '\n'+str(port)+(9-len(str(port)))*' '+common_ports.ports_and_services[port]
    s.close()

  # Output string
  if (verbose == True):
    if (sname != iname):
      resp = 'Open ports for ' + sname + ' ('+iname+')'
    else:
      resp = 'Open ports for ' + sname
    resp = resp + t  
    return resp
  

  return(l)


