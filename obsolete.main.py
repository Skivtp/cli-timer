import time
import platform
import os
from datetime import datetime
print("Current working directory:", os.getcwd())
def write_log(mode, duration, status):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    mode_text = "study" if mode == "1" else "rest"
    log_line = f"{now} | mode: {mode_text} | duration: {duration} min | status: {status}\n"
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)
    
    log_path = os.path.join(log_dir, "session_log.txt")
    with open(log_path, "a") as file:
        file.write(log_line)
        
mode_names = {
        '1': 'study',
        '2': 'rest'
    }

print("hello")

def mode_selection():
    mode = input('choose mode (1 - study, 2 - rest): ')
    modelist = ['1', '2']
    while mode not in modelist:
        print("no such mode")
        mode = input('choose mode (1 - study, 2 - rest): ')
    return mode
mode = mode_selection()  

print(f'mode {mode_names[mode]} selected')

while True:
    duration = input("Enter duration in minutes: ")
    try:
        duration = int(duration)
        if duration <= 0:
            print("not a positive number")
        else:
            break
    except ValueError:
        print("not a number")

write_log(mode, duration, "started") 
study_end_en = 'Study session complete! Take a break.'
rest_end_en = 'Break time over! Get back to work.'

time_left = duration * 60

def countdown(t):
    
    while t > 0:
        if t >= 600 and t % 300 == 0:
            print(t // 60)
        elif 60 <= t < 600 and t % 60 == 0:
            print(t // 60)
        elif 10 <= t < 60 and t % 5 == 0:
            print(t)
        elif t < 10:
            print(t)
        time.sleep(1)  
        t -= 1
    if mode == '1':
        print(study_end_en)
    else:
        print(rest_end_en)
write_log(mode, duration, "finished")   
def play_sound():
    system = platform.system()

    if system == "Windows":
        try:
            import winsound
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        except ImportError:
            print("winsound not available")
    elif system == "Linux" or system == "Darwin":  # Darwin = macOS
            # Requires 'sox' installed (for 'play' command)
        os.system('play -nq -t alsa synth 1 sine 440')
    else:
        print('\a')  # fallback: ASCII bell
countdown(time_left)
play_sound()

    




