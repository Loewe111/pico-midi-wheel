import storage
import board, digitalio

button = digitalio.DigitalInOut(board.GP9)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

if button.value:
    storage.disable_usb_drive()
