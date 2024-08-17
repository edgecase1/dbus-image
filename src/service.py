#from gi.repository import GObject
from gi.repository import GObject as gobject
import dbus
import dbus.service
import subprocess

from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)


OPATH = "/com/example/HelloWorld"
IFACE = "com.example.HelloWorld"
BUS_NAME = "com.example.HelloWorld"


class Example(dbus.service.Object):
    def __init__(self):
        bus = dbus.SessionBus()
        bus.request_name(BUS_NAME)
        bus_name = dbus.service.BusName(BUS_NAME, bus=bus)
        dbus.service.Object.__init__(self, bus_name, OPATH)

    @dbus.service.method(dbus_interface=IFACE + ".SayHello",
                         in_signature="", out_signature="")
    def SayHello(self):
        print("hello, world")

    @dbus.service.method(dbus_interface=IFACE + ".Execute",
                         in_signature="s", out_signature="s")
    def Execute(self, path):
        print(path)
        cmd = path.split(" ")
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        return result.stdout

    @dbus.service.method(dbus_interface=IFACE + ".SPIwrite",
                         in_signature="s", out_signature="s")
    def SPIwrite(self, path):
        print("writing to SPI")
        return "ok"
  

if __name__ == "__main__":
    a = Example()
    loop = gobject.MainLoop()
    loop.run()
