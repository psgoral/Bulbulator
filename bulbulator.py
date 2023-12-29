import rumps
from yeelight import discover_bulbs,Bulb


class GUI(rumps.App):
    def __init__(self):
        super(GUI, self).__init__("💡 Bulbulator 💡")

        
        bulbs = [Bulb(bulb["ip"],effect="sudden") for bulb in discover_bulbs()]


        if len(bulbs) == 1:

            bright_slider = rumps.SliderMenuItem(50,0,100,dimensions=(200,30))
            bright_slider.set_callback(callback=lambda _: bulbs[0].set_brightness(bright_slider.value))
            temp_slider = rumps.SliderMenuItem(5000,1700,6500,dimensions=(200,30))
            temp_slider.set_callback(callback=lambda _: bulbs[0].set_color_temp(temp_slider.value))


            self.menu = [
                'ON/OFF',
                rumps.MenuItem("ON",callback=lambda _: bulbs[0].turn_on()),
                rumps.MenuItem("OFF",callback=lambda _: bulbs[0].turn_off()),
                None,
                'Colors',
                rumps.MenuItem("⚪",callback=lambda _: bulbs[0].set_rgb(255,255,255)),
                rumps.MenuItem("🔴",callback=lambda _: bulbs[0].set_rgb(255,0,0)),
                rumps.MenuItem("🟢",callback=lambda _: bulbs[0].set_rgb(0,255,0)),
                rumps.MenuItem("🔵",callback=lambda _: bulbs[0].set_rgb(0,0,255)),
                rumps.MenuItem("🟠",callback=lambda _: bulbs[0].set_rgb(255,140,0)),
                rumps.MenuItem("🟣",callback=lambda _: bulbs[0].set_rgb(255,0,255)),
                None,
                'Brightness',
                bright_slider,
                None,
                "Temperatura",
                temp_slider
                ]
        
if __name__ == "__main__":
    GUI().run()
