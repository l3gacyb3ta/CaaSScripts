import hashlib
passws = []

with open('top10k.txt') as pasw:
  for i in pasw.readlines():
    passws.append(i.strip().encode('utf-8'))


def sha256(pasw) -> str:
  return str(hashlib.sha256(pasw).hexdigest())

def sha1(pasw) -> str:
  return str(hashlib.sha1(pasw).hexdigest())

with open('top10k256.txt', 'w') as pasw:
  pass256 = []
  for i in passws:
    hash = sha256(i)
    pass256.append(hash)
    print("{} => {}".format(i, hash))
  
  pasw.write('\n'.join(pass256))

with open('top10k1.txt', 'w') as pasw:
  pass1 = []
  for i in passws:
    hash = sha1(i)
    pass1.append(hash)
    print("{} => {}".format(i, hash))
  
  pasw.write('\n'.join(pass1))
