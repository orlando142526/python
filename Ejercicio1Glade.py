import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
class Ejercicio1Glade():
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("caca.glade")
        sinais={"on_txtSaudo_activate":self.on_txtSaudo_activate,
                "on_btnSaudo_clicked":self.on_btnSaudo_clicked,
                "on_winSaudo_delete_event":Gtk.main_quit}
        builder.connect_signals(sinais)
        self.txtSaudo=builder.get_object("txtSaudo")
        self.lblSaudo=builder.get_object("lblSaudo")

    def on_txtSaudo_activate(self,boton):
        nome=self.txtSaudo.get_text()
        self.lblSaudo.set_text("ola"+nome+"Benvido!!")

    def on_btnSaudo_clicked(self,boton):
        nome = self.txtSaudo.get_text()
        self.lblSaudo.set_text("ola" + nome + "Benvido!!")


if __name__ == '__main__':
    Ejercicio1Glade()
    Gtk.main()
