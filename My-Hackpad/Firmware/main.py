import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

# Initialize the keyboard
keyboard = KMKKeyboard()

# Initialize the Rotary Encoder (The Knob)
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# 1. PIN MAPPING (Matching your KiCad Schematic)
# Rows: Connected to D0 and D1
keyboard.row_pins = (board.D0, board.D1)

# Columns: Connected to D2, D3, and D4
keyboard.col_pins = (board.D2, board.D3, board.D4)

# Diode Direction: Standard for most DIY builds
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# 2. ENCODER PINS (The Knob)
# Pins: A=D7, B=D8, Click/Button=D9
# The "False" at the end means we aren't using a custom resolution
encoder_handler.pins = ((board.D7, board.D8, board.D9, False),)

# 3. KEYMAP (What the buttons do)
# Layer 0: Media Controls
keyboard.keymap = [
    [
        KC.MPLY, KC.MNXT, KC.MPRV,  # Top Row: Play/Pause, Next, Previous
        KC.MUTE, KC.VOLU, KC.VOLD,  # Bottom Row: Mute, Vol Up, Vol Down
    ]
]

# 4. ENCODER MAP (What the turning does)
# (Clockwise, Counter-Clockwise, Click)
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),)
]

if __name__ == '__main__':
    keyboard.go()