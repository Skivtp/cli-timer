import time
import platform
import os
from datetime import datetime

# задаю словари 
# общий словарь режимов
modes = {
    "study intensive": {
        "duration": 25,
        "session_repeat": None,
        "end_message": "Study session complete! Take a break.",
        "sound": "ding"
    },
    "study light": {
        "duration": 45,
        "session_repeat": None,
        "end_message": "Study session complete! Take a break.",
        "sound": "ding"
    },
    "rest": {
        "duration": 5,
        "end_message": "Break time over! Get back to work.",
        "sound": "chime"
    },
    "long_rest": {
        "duration": 20,
        "end_message": "Break time over! Get back to work.",
        "sound": "chime"
    },
     "light_study_rest": {
        "duration": 15,
        "end_message": "Break time over! Get back to work.",
        "sound": "chime"
    },
    "other": {
        "duration": None,
        "end_message": "that's all folks!",
        "sound": "chime"
    }
}
# отдельный словарь для выбора режима пользователем
mode_options = {
    "1": "study intensive",
    "2": "study light",
    "3": "other"
}

print("hello")

def mode_selection():
    mode_key = input('choose mode (1 - study intensive, 2 - study light, 3 - other): ')
    while mode_key not in mode_options:
        print("no such mode")
        mode_key = input('choose mode (1 - study intensive, 2 - study light, 3 - other): ')
    return mode_key
mode_key = mode_selection()
mode = mode_options[mode_key]

print(f"mode {mode} selected")
if mode != "other":
    while True:
        session_repeat = input("Please select repeat sessions :")
        try:
            session_repeat = int(session_repeat)
            if session_repeat <= 0:
                print("not a positive number")
            else:
                break
        except ValueError:
            print("not a number")
else:
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
# выбор режима работает, теперь нужно проверить что работает длительность

if mode == "study intensive":   
    time_left = modes["study intensive"]["duration"] * 60
    rest_time = modes["rest"]["duration"] * 60
elif mode == "study light":
    time_left = modes["study light"]["duration"] * 60
    rest_time = modes["light_study_rest"]["duration"] * 60
else:
    time_left = duration  * 60
# функция обратного отсчета
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
    
# конец функции обратного отсчета


# функция звуковое оповещение
def play_sound(sound_name):
    system = platform.system()
    if system == "Windows":
        try:
            import winsound
            if sound_name == "chime":
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            elif sound_name == "ding":
                winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS)
            else:
                winsound.Beep(1200, 250)
        except Exception:
            pass
    elif system == "Linux" or system == "Darwin":  # Darwin = macOS
            # Requires 'sox' installed (for 'play' command)
        os.system('play -nq -t alsa synth 1 sine 440')
    else:
        print('\a')  # fallback: ASCII bell
# конец звукового оповещения



# функция для определения количества повторов учебных периодов
def study_time():
    for session in range(session_repeat):
        print(f"Session {session + 1}/{session_repeat} — Study")
        countdown(time_left)
        print(modes[mode]["end_message"])
        play_sound(modes[mode]["sound"])

        # отдых после каждой учебной сессии, кроме последней
        if session < session_repeat - 1:
            print(f"Session {session + 1}/{session_repeat} — Rest")
            countdown(rest_time)
            print(modes["rest"]["end_message"])
            play_sound(modes["rest"]["sound"])
        


if mode == "other":
    countdown(time_left) # вызов функции обратного отсчета
    play_sound(modes[mode]["sound"]) # вызов звукового оповещения
    print(modes["other"]["end_message"])
else:  # mode == "study light"
    study_time()


print("that`s all for today!") 




