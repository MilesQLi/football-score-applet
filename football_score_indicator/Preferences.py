from gi.repository import Gtk
from configuration import Configurations

class PreferencesWindow(Gtk.Window):

    def __init__(self):
        self.config = Configurations().readConfigurations()
        Gtk.Window.__init__(self, title="Preferencees")
        self.set_border_width(10)
        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        self.button1 = Gtk.RadioButton.new_with_label_from_widget(None, "Show Only Live Matches")
        self.button1.set_active(self.config['live_matches'])
        self.button1.connect("toggled", self.on_button_toggled, "1")
        hbox.pack_start(self.button1, False, False, 0)

        self.button2 = Gtk.RadioButton.new_from_widget(self.button1)
        self.button2.set_label("Show all matches")
        self.button2.set_active(self.config['all_matches'])
        self.button2.connect("toggled", self.on_button_toggled, "2")
        hbox.pack_start(self.button2, False, False, 0)

        self.button3 = Gtk.CheckButton("Hide Leagues")
        self.button3.set_active(self.config['hide_leauges'])
        self.button3.connect("toggled", self.on_button_toggled, "3")
        hbox.pack_start(self.button3, False, False, 0)

        self.connect("destroy",self.exit)

    def exit(self,widget):
        self.close()
    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

        self.config['all_matches'] = self.button2.get_active()
        self.config['live_matches'] = self.button1.get_active()
        self.config['hide_leauges'] = self.button3.get_active()

        Configurations().writeConfigurations(self.config)

    def display(self):

        self.show_all()


