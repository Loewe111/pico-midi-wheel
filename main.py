import time
import board
import busio
import usb_midi
import rotaryio

import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

from digitalio import DigitalInOut, Direction, Pull

CONF_ENCODERS = [ # A and B pins
    (board.GP9, board.GP10),
    (board.GP11, board.GP12)
]

CONF_BUTTONS = [
    (board.GP13),
    (board.GP14)
]

BUTTON_OFFSET = 60

midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], in_channel=0, midi_out=usb_midi.ports[1], out_channel=0)

encoders = []
for enc in CONF_ENCODERS:
    encoders.append({
        "encoder": rotaryio.IncrementalEncoder(enc[0], enc[1]),
        "last_position": 0
    })

buttons = []
for btn in CONF_BUTTONS:
    button = DigitalInOut(btn)
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    buttons.append({
        "button": button,
        "last_state": True
    })

while True:
    for key, enc in enumerate(encoders): # Read encoders
        position = enc["encoder"].position
        diff = position - enc["last_position"]
        if diff > 0:
            midi.send(NoteOn(key, 127 - diff))
        elif diff < 0:
            midi.send(NoteOn(key, 1 - diff))
        enc["last_position"] = position
        
    for key, btn in enumerate(buttons): # Read buttons
        if btn["button"].value != btn["last_state"]:
            if btn["button"].value == False:
                midi.send(NoteOn(BUTTON_OFFSET + key, 127))
            else:
                midi.send(NoteOff(BUTTON_OFFSET + key, 127))
            btn["last_state"] = btn["button"].value