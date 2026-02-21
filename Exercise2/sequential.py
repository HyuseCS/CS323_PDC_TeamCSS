import time

def cook_rice():
    print("  [Sequential] Cooking rice... (2 seconds)")
    time.sleep(2.0)
    print("  [Sequential] Rice is done.")

def cook_egg():
    print("  [Sequential] Cooking egg... (1 second)")
    time.sleep(1.0)
    print("  [Sequential] Egg is done.")
