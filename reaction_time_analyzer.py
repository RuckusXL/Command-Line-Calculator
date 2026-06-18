#This script is a Reaction time analyzer
#Author: RuckusXL

import time
import random
import msvcrt

def get_ready():
    print("Get Ready...\n")

    while msvcrt.kbhit():
        msvcrt.getch()

    start_time = time.perf_counter()
    delay = random.uniform(2, 5)

    while time.perf_counter() - start_time < delay:

        if msvcrt.kbhit():
            msvcrt.getch()
            print("Too Early!!")
            return False
        
        time.sleep(0.001)
       
    print("GO!\n")
    return True

def measure_reaction():
    start = time.perf_counter()
    input("Press Enter!\n")
    end = time.perf_counter()
    reactionTime = end - start
    return reactionTime

def run_reaction_test():
    reaction_times = []
    print(input("\nPress Enter to start...\n"))

    for i in range(5):
        print(f"-- Round {i+1} -- \n")
        
        ready = get_ready()

        if ready is False:
            print("CHEAT!\n")
            continue

        reaction = measure_reaction()
        reaction_times.append(reaction)

    if len(reaction_times) == 0:
        print("Quit Cheating!!")
        return
    
    average = sum(reaction_times) / len(reaction_times)
    fastest = min(reaction_times)
    slowest = max(reaction_times)
    
    print("\nResults:")
    print("----------------")
    print(f"Times: {[round(t, 3) for t in reaction_times]}")
    print(f"Average: {average:.3f}s")
    print(f"Fastest: {fastest:.3f}s")
    print(f"Slowest: {slowest:.3f}s\n")
    
    if average < 0.20:
        print("⚡ELITE\n")
    elif average < 0.25:
        print("🔥FAST\n")
    elif average < 0.30:
        print("💨 GOOD JOB\n")
    elif average < 0.4:
        print("🐌 SLOW\n")
    else:
        print("🐢 TOO SLOW\n")
    
    return reaction_times

def wait_for_exit():
    print(input("Press ENTER to exit...\n"))

    while msvcrt.kbhit():
        msvcrt.getch()

def run_program():
    run_reaction_test()

if __name__ == "__main__":
    run_program()
    wait_for_exit()