import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
class CrearVentana (Gtk.Window):

        def __init__(self):
            Gtk.Window.__init__(self)
            self.set_title("Mi primera ventanita")
            self.set_default_size ( 300 , 200)

            self.connect('delete-event',Gtk.main_quit)
            self.show_all()

if __name__=="__main__":

 CrearVentana()
 Gtk.main()