import pyautogui as pg
import msvcrt
import time


image_names = ['insérer ici le nom du fichier de l image','ici un deuxieme', 'ainsi de suite']

def check_image(image_name):
    found = False
    try:
        (x, y) = pg.locateCenterOnScreen(image_name, confidence=0.7)
        if not found:
            pg.click(x, y)
            print(f"{image_name} a été trouvé")
            found = True
    except:
        print(f"{image_name} not found")
    
    return found

# Boucle infinie pour exécuter la fonction en continu
while True:
    for image_name in image_names:
        found = check_image(image_name)
        if found:
            time.sleep(3.5) # Pause de 4 secondes entre chaque exécution
            break # Passer à l'image suivante
    if msvcrt.kbhit():
        break # Sortir de la boucle si une touche est pressée
