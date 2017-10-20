import sys
import time
import Ice
Ice.loadSlice('Armory.ice')
import Armory


class Client(Ice.Application):
    def run(self, argv):
        proxy = self.communicator().stringToProxy(argv[1])
        turret = Armory.PanTiltPrx.checkedCast(proxy)

        if not turret:
            raise RuntimeError('Invalid proxy')

        turret.down()
        time.sleep(1)

        turret.up()
        time.sleep(1)

        turret.left()
        time.sleep(1)

        turret.right()
        time.sleep(1)

        turret.stop()
        time.sleep(1)

        turret.fire()

        return 0


sys.exit(Client().main(sys.argv))
