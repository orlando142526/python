import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
class Formulario(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self)
            self.set_title("Información sobre el producto")
            self.set_default_size(300,200)
            caixaV=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
            self.add(caixaV)
            etiqueta=Gtk.Label(label="Información sobre el producto")
            cadro1=Gtk.Frame(label="Datos básicos")
            cadro2 = Gtk.Frame(label="Datos económicos")
            caixaV.pack_start(etiqueta,False,False,2)
            caixaV.pack_start(cadro1, True , True, 20)
            caixaV.pack_start(cadro2, True, True, 20)

            builder = Gtk.Builder()
            builder.add_from_file("formulario.glade")
            caixaV2 = builder.get_object("caixav2")
            btnElixir = builder.get_object("btnElixir")
            sinais = {"on_btnElixir_clicked":self.on_btnElixir_clicked}
            builder.connect_signals(sinais)
            cadro1.add(caixaV2)

            """caixaV2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
            cadro1.add(caixaV2)
            lblNome=Gtk.Label(label="Nome")
            txtNome=Gtk.Entry()
            lblDescripcion=Gtk.Label(label="Descripción")
            txtDescripcion=Gtk.TextView()
            caixaH=Gtk.Box(spacing=2)
            boton=Gtk.CheckButton(label="AÑadir contador de visitas")
            caixaV2.pack_start(lblNome,False,False,2)
            caixaV2.pack_start(txtNome,True,False,2)
            caixaV2.pack_start(lblDescripcion,False,False,2)
            caixaV2.pack_start(txtDescripcion,True, True, 2)
            caixaV2.pack_start(caixaH, True, True, 2)
            caixaV2.pack_start(boton, False, False, 2)
            lblfoto=Gtk.Label(label="FOTO")
            txtFoto=Gtk.Entry()
            boton2=Gtk.CheckButton(label="ELEGIR....")
            
            caixaH.pack_start(lblfoto,False,False,2)
            caixaH.pack_start(txtFoto,False,False,2)
            caixaH.pack_start(boton2,False,False,2)
"""



            caixav3=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
            cadro2.add(caixav3)
            caixaH3=Gtk.Box(spacing=6)
            lblPrecio=Gtk.Label(label="PRECIO")
            txtPrecio=Gtk.Entry()
            lblImpuestos=Gtk.Label(label="IMPOSTOS")
            cmbImpostos=Gtk.ComboBoxText()
            caixaH3.pack_start(lblPrecio,False,False,2)
            caixaH3.pack_start(txtPrecio, False, False, 2)
            caixaH3.pack_start(lblImpuestos, False, False, 2)
            caixaH3.pack_start(cmbImpostos, False, False, 2)
            lblPromocion=Gtk.Label(label="PROMOCION")
            btnNingun=Gtk.RadioButton(label="Ningun")
            btnTransporte=Gtk.RadioButton(label="Desconto 5%")
            caixav3.pack_start(lblPromocion,False,False,2)
            caixav3.pack_start(btnNingun, False, False, 2)
            caixav3.pack_start(btnTransporte, False, False, 2)


            self.connect("delete-event",Gtk.main_quit)
            self.show_all()

        def on_btnElixir_clicked(self,boton):
                print("Boton elixir pulsado")

if __name__=="__main__":
    Formulario()
    Gtk.main()