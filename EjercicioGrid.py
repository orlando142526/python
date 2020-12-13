import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
class EjercicioGrid(Gtk.Window):
     def __init__(self):
         Gtk.Window.__init__(self)
         self.set_title("Exemplo con Grid")
         self.set_default_size(300,100)

         grid=Gtk.Grid()
         self.add(grid)

         boton1=Gtk.Button(label="BOTON 1")
         boton2=Gtk.Button(label="BOTON 2")
         boton3 = Gtk.Button(label="BOTON 3")
         boton4 = Gtk.Button(label="BOTON 4")
         boton5 = Gtk.Button(label="BOTON 5")
         boton6 = Gtk.Button(label="BOTON 6")


         grid.add(boton1)
         grid.attach (boton2,1,0,2,1)
         grid.attach_next_to(boton3,boton1,Gtk.PositionType.BOTTOM,1,2)
         grid.attach_next_to(boton4,boton3,Gtk.PositionType.RIGHT,2,1)
         grid.attach (boton5,1,2,1,1)
         grid.attach_next_to(boton6,boton5,Gtk.PositionType.RIGHT,1,1)

         self.connect("delete-event", Gtk.main_quit)
         self.show_all()

if __name__=="__main__":
    EjercicioGrid()
    Gtk.main()