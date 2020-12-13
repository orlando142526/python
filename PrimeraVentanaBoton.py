import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
class PrimeraVentanaBoton (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Ventana con botón")
        self.set_default_size(300,300)

        btnBotonSaida = Gtk.Button()
        btnBotonSaida.set_label("sair")
        btnBotonSaida.connect("clicked",self.on_btnBotonSaida_clicked,"Que pacaha")

        self.add(btnBotonSaida)
        self.connect ('delete-event', Gtk.main_quit)
        self.show_all()

    def on_btnBotonSaida_clicked (self,control,datos):
        print ("datos")
        Gtk.main_quit()

if __name__ == "__main__":

    PrimeraVentanaBoton()
    Gtk.main()








