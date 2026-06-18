import os
import sys
import urllib.request
from colorama import init, Fore

init(autoreset=True)

OUI_URL = "https://standards-oui.ieee.org/oui/oui.txt"
OUI_FILE = "oui.txt"


#Use a safe writable location (THIS is the real fix)
def get_storage_path():
    path = os.path.join(os.environ["USERPROFILE"], "MacLookup")
    os.makedirs(path, exist_ok=True)
    return path


OUI_PATH = os.path.join(get_storage_path(), OUI_FILE)

def download_oui():
    try:
        req = urllib.request.Request(
            OUI_URL,
            headers={'User-Agent': 'Mozilla/5.0'}
        )

        with urllib.request.urlopen(req) as response, open(OUI_PATH, 'wb') as out_file:
            out_file.write(response.read())

        print(Fore.GREEN + "Download complete.\n")

    except Exception as e:
        print(Fore.RED + f"\nDownload failed: {e}")
        input("Press Enter to exit...")
        sys.exit()

def ensure_oui_file():
    if not os.path.exists(OUI_PATH):
        print(Fore.YELLOW + "\nOUI database not found. Downloading...")
        download_oui()


def read_file(filename):
    macbook = {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if "(hex)" in line:
                    macaddr = line.split("(hex)")
                    prefix = macaddr[0].replace("-", "").strip()[:6]
                    suffix = macaddr[1].strip()
                    macbook[prefix] = suffix

    except Exception as e:
        print(Fore.RED + f"\nError reading OUI file: {e}")
        input(Fore.RED + "\nPress Enter to exit...")
        sys.exit()

    return macbook


def macaddr_lookup(macbook):
    while True:
        dirtymac = input(Fore.CYAN + "\nType or paste MAC address (or 'q' to quit): ").strip()

        if dirtymac.lower() == "q":
            print(Fore.MAGENTA + "\nExiting... Bye!\n")
            break

        cleanmac = dirtymac.upper().replace("-", "").replace(":", "")[:6]

        if len(cleanmac) < 6:
            print(Fore.RED + "\nEnter at least 6 hex characters.")
            continue

        vendor = macbook.get(cleanmac)

        if vendor:
            print(Fore.GREEN + f"\nVendor -> {vendor}")
        else:
            print(Fore.YELLOW + "\nVendor not found.")


# --- MAIN ---
ensure_oui_file()
macbook = read_file(OUI_PATH)
macaddr_lookup(macbook)