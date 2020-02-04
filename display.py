from machine import Pin
import neopixel
import time


class Colors:
    OFF = (0, 0, 0)
    WHITE = (128, 128, 128)


COLOR_POOL = [ # '#ffffff', '#ff0000', '#ffa500', '#008000', '#0000ff', '#000000'
    (255, 255, 255),
    (255, 0, 0),
    (255, 165, 0),
    (0, 255, 0),
    (0, 0, 255),
    (0, 0, 0)

]


def fade(color, factor):
    return int(round(color[0] * factor)), int(round(color[1] * factor)), int(round(color[2] * factor))


class Strip:
    """Represents an unit of display. Input values are the number of leds and the pin."""

    def __init__(self, pin, number_of_leds):
        print("Creating strip on pin " + str(pin) + " with " + str(number_of_leds) + " leds.")
        self.__pin__ = pin
        self.leds_count = number_of_leds
        self.strip = neopixel.NeoPixel(Pin(pin, Pin.OUT), number_of_leds)
        self.off()

    def set_pixel(self, index, color):
        self.strip[index] = color

    def write(self):
        self.strip.write()

    def number_of_leds(self):
        return self.leds_count

    def off(self):
        for i in range(self.strip.n):
            self.strip[i] = Colors.OFF
        self.strip.write()

    def on(self):
        for i in range(self.strip.n):
            self.strip[i] = fade(Colors.WHITE, 0.2)
        self.strip.write()

    def demo(self):
        print("INFO -- Strip " + str(self.__pin__) + " demo starting.")
        np = self.strip
        n = np.n

        # cycle
        for i in range(4 * n):
            for j in range(n):
                np[j] = Colors.OFF
            np[i % n] = Colors.WHITE

            np.write()

        # clear
        for i in range(n):
            np[i] = Colors.OFF
        np.write()
        print("INFO -- Strip " + str(self.__pin__) + " demo complete.")


class Plate:
    def __init__(self, strip, start_index, end_index):
        self.__strip__ = strip
        self.__start_index__ = start_index
        self.__end_index__ = end_index

    def on(self, color=Colors.WHITE):
        for factor in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
            for i in range(self.__start_index__, self.__end_index__):
                self.__strip__.set_pixel(i, fade(color, factor))
            self.__strip__.write()
            time.sleep_ms(5)

    def off(self):
        for factor in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
            for i in range(self.__start_index__, self.__end_index__):
                self.__strip__.set_pixel(i, fade(Colors.OFF, factor))
            self.__strip__.write()
            time.sleep_ms(5)


class Display:
    def __init__(self, plates):
        self.__plates__ = plates
        self.__model__ = [False for i in range(len(plates))]

    def on(self, index, color):
        self.__plates__[index].on(color)
        self.__model__[index] = True

    def off(self, index):
        self.__plates__[index].off()
        self.__model__[index] = False

    def demo(self, color=Colors.WHITE):
        for i in self.__plates__:
            i.on(fade(color, 0.2))
            time.sleep_ms(100)
            i.off()

    def on_all(self, color):
        self.__model__ = [False for i in range(len(self.__plates__))]
        for n in self.__plates__:
            n.on(color)

    def off_all(self):
        self.__model__ = [False for i in range(len(self.__plates__))]
        for n in self.__plates__:
            n.off()
