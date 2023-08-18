import ctypes
import multiprocessing
from img2ascii import IMG2ASCII
import pystray
from PIL import Image
import time
import random as rand
import os
import shutil
from multiprocessing import Process, Value

user = os.getenv("HOME")


def sleep_cachorro(icon, item):
    with is_visible.get_lock():
        is_visible.value = 0
    icon.stop()


def fala_dog(icon, item):
    cachorro_path = rf"{user}\Desktop\espaço 1\cachorro{str(rand.randint(-1000, 1000))}.txt"

    with open(cachorro_path, 'a+') as file:
        n = rand.randint(0, 1)
        match n:
            case 0:
                file.write(f"cachorro")
            case 1:
                file.write('latido')

        file.close()


def auto_cachorro(is_visible):
    cachorro_path = rf"{user}\Desktop\autodog.txt"
    watch_folder = rf'{user}\Desktop\espaço 1'
    destiny_folder = rf'{user}\Desktop\espaço 2'

    try:
        os.mkdir(watch_folder)
    except Exception:
        pass

    try:
        os.mkdir(destiny_folder)
    except Exception:
        pass

    time.sleep(5)
    while True:
        with is_visible.get_lock():
            if is_visible.value == 0:
                with open(cachorro_path, 'a+') as file:
                    file.write("\n vo é dormir zzzzz\n\n")
                file.close()

                IMG2ASCII(cachorro_path, 'cachorro.jpg')
                break

        for file in os.listdir(watch_folder):
            shutil.move(os.path.join(watch_folder, file), destiny_folder)

            with open(cachorro_path, 'a+') as log:
                log.write(f"au au {file} movido \n")

                log.close()

        time.sleep(5)


if __name__ == '__main__':
    multiprocessing.freeze_support()

    image = Image.open("cachorro.jpg")

    print(user)

    icon = pystray.Icon("cachorrometro", image, menu=pystray.Menu(
        pystray.MenuItem("cachorro", fala_dog),
        pystray.MenuItem("vai dormir cachorro", sleep_cachorro)
    ))

    is_visible = Value(ctypes.c_int, 0)

    icon.run_detached()

    time.sleep(2)

    with is_visible.get_lock():
        is_visible.value = icon.visible.real
    process = Process(target=auto_cachorro, args=(is_visible,))
    process.start()

    process.join()



