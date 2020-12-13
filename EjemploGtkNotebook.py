import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
class EjemploGtkNotebook(Gtk.Window):
     def __init__(self):
         Gtk.Window.__init__(self)
         self.set_title("Ejemplo con NOTEBOOK")
         self.set_default_size(300,100)

         self.Notebook= Gtk.Notebook()
         self.add(self.Notebook)


         paxina1= Gtk.Box()
         paxina1.set_border_width(10)
         paxina1.add(Gtk.Label(label="paxina principal"))
         self.Notebook.append_page(paxina1,Gtk.Label(label="Titulo de texto"))

         paxina2= Gtk.Box()
         paxina2.set_border_width(10)
         paxina2.add(Gtk.Label(label="paxina con unha imaxe e titulo"))
         self.Notebook.append_page(paxina2,Gtk.Image.new_from_icon_name("help-about",Gtk.IconSize.MENU))

         self.connect("delete-event", Gtk.main_quit)
         self.show_all()



if __name__=="__main__":
    EjemploGtkNotebook()
    Gtk.main()