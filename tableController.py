from display import Strip, Plate, fade, Display, Colors, COLOR_POOL

STRIP_DEMO = False

# Important note: The order of the elements in the array counts!!
led_strips = [
    Strip(25, 23 * 2),  # Pin T Right Top
    Strip(26, 23 * 2),  # Pin P Left Top
    Strip(14, 23 * 3),  # Pin H Right Bottom
    Strip(27, 23 * 3),  # Pin L Left Bottom
]
if STRIP_DEMO:
    print("Starting strip demos...")
    for strip in led_strips:
        strip.demo()

d0 = Display([
    Plate(led_strips[3], 2, 10),
    Plate(led_strips[1], 2, 10),
    Plate(led_strips[3], 32, 45),
    Plate(led_strips[1], 32, 45),
    Plate(led_strips[3], 47, 60)
])

d1 = Display([
    Plate(led_strips[3], 12, 20),
    Plate(led_strips[1], 12, 20),
    Plate(led_strips[3], 22, 30),
    Plate(led_strips[1], 22, 30),
    Plate(led_strips[3], 60, 69)
])

d2 = Display([
    Plate(led_strips[2], 2, 10),
    Plate(led_strips[0], 2, 10),
    Plate(led_strips[2], 32, 45),
    Plate(led_strips[0], 32, 45),
    Plate(led_strips[2], 47, 60)
])

d3 = Display([
    Plate(led_strips[2], 12, 20),
    Plate(led_strips[0], 12, 20),
    Plate(led_strips[2], 22, 30),
    Plate(led_strips[0], 22, 30),
    Plate(led_strips[2], 60, 69)
])

displays = [d0, d1, d2, d3]

front = Display([
    Plate(led_strips[2], 0, 2),
    Plate(led_strips[3], 0, 1)
])

# front.on_all(fade(Colors.WHITE, 0.1))

for d in displays:
    d.demo(fade(Colors.WHITE, 0.1))

for d in displays:
    d.off_all()

print("End of init sequence.")


def set_table_state(display_index, plate_index, color):
    print("Setting plate " + str(plate_index) + " on display " + str(display_index) + " to the color " + str(color))
    selected_display = displays[display_index]
    print(selected_display)
    color = fade(COLOR_POOL[color], 0.2)
    print(color)
    selected_display.on(plate_index, color)


def get_table_state():
    return [d.__model__ for d in displays]
