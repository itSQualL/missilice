import sys
import time
import Ice
Ice.loadSlice('Armory.ice')
import Armory

class PanTiltI(Armory.PanTilt):
    def down(self, current=None):
        print("going down...")

    def up(self, current=None):
        print("going up...")

    def left(self, current=None):
        print("going left...")

    def right(self, current=None):
        print("going right...")

    def stop(self, current=None):
        print("stopped...")

    def fire(self, current=None):
        print("fire!!!")


class Server(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        servant = PanTiltI()

        adapter = broker.createObjectAdapter("PanTiltAdapter")
        proxy = adapter.add(servant, broker.stringToIdentity("turret"))

        print(proxy)
        sys.stdout.flush()

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0


server = Server()
sys.exit(server.main(sys.argv))
