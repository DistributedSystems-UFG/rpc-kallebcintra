import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

  def exposed_remove(self, data):
    if data in self.value:
        self.value.remove(data)
        return True
    return False

  def exposed_search(self, data):
    return data in self.value

  def exposed_insert(self, index, data):
    try:
        self.value.insert(index, data)
        return True
    except IndexError:
        return False 

  def exposed_sort(self):
    self.value.sort()
    return self.value

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()