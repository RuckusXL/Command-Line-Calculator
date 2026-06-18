#This is a gaming toolkit that will help manage clips, and provide resources like aim trainers and reaction time trackers
#Author: RuckusXL
import psutil
import platform
import time
import os
import random
import msvcrt
from colorama import init, Fore, Style

init(autoreset=True)

def clear_input_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()

class SystemMonitor:
    def __init__(self):
        net = psutil.net_io_counters()
        self.last_sent = net.bytes_sent
        self.last_recv = net.bytes_recv

    def clear_screen(self):
        print("\033[H", end="")

    def sysdata(self):
        #CPU Usuage
        cpu_percent = psutil.cpu_percent(interval=0.1)
        cpu_cores = psutil.cpu_count()

        #RAM Usage
        ram = psutil.virtual_memory()
        ram_total_gb = ram.total / (1024 **3)
        ram_used_gb = ram.used / (1024 ** 3)
        ram_percent = ram.percent

        #DISK Usage
        disk_path = "C:\\" if platform.system() == "Windows" else "/"
        disk = psutil.disk_usage(disk_path)
        disk_total_gb = disk.total / (1024 ** 3)
        disk_used_gb = disk.used / (1024 ** 3)
        disk_percent = disk.percent

        #NETWORK I/O
        net = psutil.net_io_counters()
        
        sent_now = net.bytes_sent
        recv_now = net.bytes_recv

        upload_speed = (sent_now - self.last_sent) / 1024
        download_speed = (recv_now - self.last_recv) / 1024

        self.last_sent = sent_now
        self.last_recv = recv_now

        return {
        Fore.LIGHTBLUE_EX + "CPU": f"{cpu_percent:.2f}%",
        Fore.LIGHTBLUE_EX + "CPU Cores": cpu_cores,
        Fore.LIGHTGREEN_EX + "RAM Total": f"{ram_total_gb:.2f} GB",
        Fore.LIGHTGREEN_EX +  "RAM Used": f"{ram_used_gb:.2f} GB",
        Fore.LIGHTGREEN_EX + "RAM Percent": f"{ram_percent}%",
        Fore.LIGHTYELLOW_EX + "Disk Total": f"{disk_total_gb:.2f} GB",
        Fore.LIGHTYELLOW_EX + "Disk Used": f"{disk_used_gb:.2f} GB",
        Fore.LIGHTYELLOW_EX + "Disk Percent": f"{disk_percent}% USED",
        Fore.LIGHTMAGENTA_EX + "Upload Speed": f"{upload_speed:.2f} KB/s",
        Fore.LIGHTMAGENTA_EX + "Download Speed": f"{download_speed:.2f} KB/s"
    }
    
    def showdata(self,data):
        for k, v in data.items():
            print(f"{k}: {v}")

    def run_monitor(self):
        os.system("")
        
        print("\033[2J", end="")

        while msvcrt.kbhit():
            msvcrt.getch()

        while True:

            data = self.sysdata()
            
            print("\033[H", end="")
            
            self.showdata(data)

            print(Fore.LIGHTCYAN_EX + "\nPress 'Q' or ENTER to exit...")

            if msvcrt.kbhit():
                key = msvcrt.getch()

                if key in (b'\x00', b'\xe0'):
                    msvcrt.getch()
                    continue

                if key.lower() == b'q' or key == b'\r':
                    break
            time.sleep(0.7)

    def wait_for_exit(self):
        input("Press 'Q' or ENTER to quit\n")

class ReactionTester:
    def __init__(self):
        self.reaction_times = []

    def get_ready(self):
        print("Get Ready...\n")

        while msvcrt.kbhit():
            msvcrt.getch()

        start_time = time.perf_counter()
        delay = random.uniform(2, 5)

        while time.perf_counter() - start_time < delay:

            if msvcrt.kbhit():
                msvcrt.getch()
                print("Too Early!!\n")
                return False
        
        time.sleep(0.001)
       
        print(Fore.LIGHTGREEN_EX + "GO!\n")
        return True
    
    def measure_reaction(self):
        start = time.perf_counter()
        input("Press Enter!\n")
        end = time.perf_counter()
        reactionTime = end - start
        return reactionTime
    
    def run_test(self):
        self.reaction_times = []

        input("\nPress Enter to start...\n")

        for i in range(5):
            print(Fore.LIGHTRED_EX + f"-- Round{i+1} --\n")

            ready = self.get_ready()

            if not ready:
                print("CHEAT!\n")
                continue

            reaction = self.measure_reaction()
            self.reaction_times.append(reaction)

        if len(self.reaction_times) == 0:
            print("\nQuit Cheating!!\n")
            return
        
        avg = sum(self.reaction_times) / len(self.reaction_times)
        fastest = min(self.reaction_times)
        slowest = max(self.reaction_times)

        print("\n=== Results ===")
        print(f"Times: {[round(t, 3) for t in self.reaction_times]}")
        print(f"Average: {avg:.3f}s")
        print(f"Fastest: {fastest:.3f}s")
        print(f"Slowest: {slowest:.3f}s\n")
    
        if avg < 0.20:
            print(Fore.YELLOW + "⚡ELITE\n")
        elif avg < 0.25:
            print(Fore.LIGHTBLUE_EX + "🔥FAST\n")
        elif avg < 0.30:
            print(Fore.LIGHTCYAN_EX + "💨 GOOD JOB\n")
        elif avg < 0.4:
            print(Fore.LIGHTWHITE_EX + "🐌 SLOW\n")
        else:
            print(Fore.GREEN + "🐢 TOO SLOW\n")

        self.wait_for_exit()
    
        return self.reaction_times
    
    def wait_for_exit(self):
        input("Press ENTER to exit...\n")

class ReactionTrainer:
    def __init__(self):
        self.shots = 0
        self.hits = 0
        self.score = 0

    def get_ready(self, round_num):
        while msvcrt.kbhit():
            msvcrt.getch()

        wait_time = random.uniform(0.5, max(0.7, 2 - (round_num * 0.1)))
        start_wait = time.time()

        while time.time() - start_wait < wait_time:
            if msvcrt.kbhit():
                print("Too Early!!\n")
                clear_input_buffer()
                return False
            
        return True
        
    def run_trainer(self):
        input("\nPress ENTER when ready...\n")

        for i in range(10):
            
            threshold = max(0.15, 0.30 - (i * 0.01))
            
            ready = self.get_ready(i)
            if not ready:
                print("CHEAT! Round skipped\n")
                continue
            
            print(f"Round {i+1} | Reaction Window: {threshold:.3f}s")
            print("TARGET!🎯")

            start = time.time()
            input()
            reaction = time.time() - start

            self.shots += 1

            if reaction < threshold * 0.5:
                print(Fore.LIGHTWHITE_EX + "INSANE 🎯")
                self.hits += 1
                self.score += 150
            elif reaction < threshold:
                print(Fore.GREEN + "HIT 🔥\n")
                self.hits += 1
            else:
                print(Fore.RED + "MISS 🤡\n")

        self.show_results()
        self.wait_for_exit()

    def show_results(self):
        accuracy = (self.hits / self.shots) * 100

        if accuracy >= 80:
            rank = "S"
        elif accuracy >= 60:
            rank = "A"
        elif accuracy >= 40:
            rank = "B"
        elif accuracy >= 20:
            rank = "C"
        else:
            rank = "F"
    
        print(f"Accuracy: {accuracy:.2f}% | {rank}")
        print(f"Score: {self.score}\n")

    def wait_for_exit(self):
        input(Fore.LIGHTBLUE_EX + "Press ENTER to exit...\n")

class ToolkitApp:
    def __init__(self):
        self.run_test = ReactionTester()
        self.monitor_tool = SystemMonitor()
        self.reactiontrainer = ReactionTrainer()

    def dashboard(self):
        while True:
            os.system("cls")

            self.gamingtooldash()

            print(Fore.MAGENTA + "\n1. Reaction Tester")
            print(Fore.MAGENTA + "2. Reaction Trainer")
            print(Fore.MAGENTA + "3. System Monitor")
            print(Fore.MAGENTA + "4. Exit")

            try:
                choice = int(input(Fore.MAGENTA + "\nSelect number 1-5: "))
            except ValueError:
                print(Fore.MAGENTA + "Please select number 1 - 5: ")
                continue

            if choice == 1:
                self.reacttooldash()
                self.run_test.run_test()
            elif choice == 2:
                self.reacttrainerdash()
                self.reactiontrainer.run_trainer()
            elif choice == 3:
                self.resourcedash()
                self.monitor_tool.run_monitor()
            elif choice == 4:
                print(Fore.MAGENTA + "\nGoodbye!!\n")
                break
            else:
                print("Invalid option")
                time.sleep(1)

    def gamingtooldash(self):
        print(Fore.MAGENTA + "\n========================")
        print(Fore.MAGENTA + "Gaming Toolkit Prototype")
        print(Fore.MAGENTA + "========================\n")

    def reacttooldash(self):
        print(Fore.LIGHTBLUE_EX + "\n======================")
        print(Fore.LIGHTBLUE_EX + "Reaction Time Analyzer")
        print(Fore.LIGHTBLUE_EX + "======================\n")

    def reacttrainerdash(self):
        print(Fore.LIGHTMAGENTA_EX + "\n=================")
        print(Fore.LIGHTMAGENTA_EX + "REACTION TRAINER")
        print(Fore.LIGHTMAGENTA_EX + "=================\n")

    def resourcedash(self):
        print(Fore.RED + "\n===============")
        print(Fore.RED + " Resource Tool")
        print(Fore.RED + "===============\n")

#This is the function that calls the programs
if __name__ == "__main__":
    app = ToolkitApp()
    app.dashboard()
