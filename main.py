import requests
import tkinter as tk
import os
import datetime


def blokowanie():
    url = "https://hole.cert.pl/domains/domains.txt"
    odpowiedz = requests.get(url)
    if odpowiedz.status_code == 200:
        zle_strony = odpowiedz.text.split("\n")
    else:
        zle_strony = []

    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "a") as f:
        for strona in zle_strony:
            f.write("195.187.6.33 " + strona + "\n")

    print("Zablokowano niebezpieczne strony.")


def dodawanie():
    skrypt = r"C:\Users\szymu\PycharmProjects\pythonProject\main.py"
    # ^tutaj trzeba zmienic tylko lokalizacje zeby na pewno dzialalo

    nazwa = "Aktualizacja zlych stron"
    czas = datetime.time(hour=12)

    command = f'schtasks /create /tn "{nazwa}" /tr "{skrypt}" /sc daily /st {czas.strftime("%H:%M:%S")}'
    os.system(command)


def interfejs():
    okno = tk.Tk()
    okno.title("Blokowanie stron")

    label = tk.Label(okno,
                     text="Kliknij przycisk \"Blokuj\" aby zaktualizować niebezpieczne strony lub przycisk \"Dodaj\" "
                          "by dodac aktualizowanie do harmonogramu zadan.")
    label.pack()

    przycisk = tk.Button(okno, text="Blokuj", command=blokowanie)
    przycisk.pack()

    przycisk2 = tk.Button(okno, text="Dodaj", command=dodawanie)
    przycisk2.pack()

    okno.mainloop()


def main():
    harmonogram = os.environ.get("SCHED_JOB_ID")
    if harmonogram:
        blokowanie()
    else:
        interfejs()


if __name__ == "__main__":
    main()
