import customtkinter
import vlc
import threading
import os

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

HEIGHT = 150
WIDTH = 250

def switch_page(page):
    pages = [Page_1, Page_2, Page_3]
    for i in pages:
        i.pack_forget()
    page.pack(expand=True, fill='both')

    fixed_widgets = []
    for widget in fixed_widgets:
        widget.lift()

root = customtkinter.CTk()
root.title("Mini App Store")
root.iconbitmap("appstore.ico")
root.geometry((f"{WIDTH}x{HEIGHT}"))
root.resizable(False, False)

Page_1 = customtkinter.CTkFrame(root, fg_color='transparent', corner_radius=0, border_width=0)
Page_1.pack(expand=True, fill='both')
Page_2 = customtkinter.CTkFrame(root, fg_color='transparent', corner_radius=0, border_width=0)
Page_3 = customtkinter.CTkFrame(root, fg_color='transparent', corner_radius=0, border_width=0)

player = vlc.MediaPlayer("shopchanneltitle.mp3")
player.play()

label1x = 45
started = False

def startProgram():
    global player, Page_2, started, WIDTH, HEIGHT
    HEIGHT = 150
    WIDTH = 400
    if not started:
        player.stop()
        player = vlc.MediaPlayer("shopchannel.mp3")
        player.play()
    root.geometry((f"{WIDTH}x{HEIGHT}"))
    switch_page(Page_2)

def uninstall():
    global Page_1, started
    started = True
    program = OptionMenu1.get()
    if program == "Firefox":
        os.system("winget uninstall Mozilla.Firefox")
    elif program == "Discord":
        os.system("winget uninstall Discord.Discord")
    elif program == "Opera Browser":
        os.system("winget uninstall Opera.Opera")
    elif program == "Messenger":
        os.system("winget uninstall 9WZDNCRF0083")
    elif program == "Roblox Player":
        os.system("winget uninstall Roblox.Roblox")
    elif program == "Steam":
        os.system("winget uninstall Valve.Steam")
    elif program == "VSCode":
        os.system("winget uninstall Microsoft.VisualStudioCode")
    elif program == "Chrome":
        os.system("winget uninstall Google.Chrome")
    elif program == "Microsoft 365 (Office)":
        os.system("winget uninstall 9WZDNCRD29V9")
    elif program == "Python 3.12":
        os.system("winget uninstall Python.Python.3.12")
    elif program == "Spotify":
        os.system("winget uninstall Spotify.Spotify")
    elif program == "Prism Launcher":
        os.system("winget uninstall PrismLauncher.PrismLauncher")
    Label1.configure(text="Uninstalled successfully!")
    Label1.place_configure(x=57.5)
    switch_page(Page_1)

def startuninstall():
    global Page_3, Label2, WIDTH, HEIGHT
    Label2.configure(text="Uninstalling...")
    HEIGHT = 150
    WIDTH = 250
    switch_page(Page_3)
    root.geometry((f"{WIDTH}x{HEIGHT}"))
    uninstalling = threading.Thread(target=uninstall)
    uninstalling.start()

def install():
    global Page_1, started
    started = True
    program = OptionMenu1.get()
    if program == "Firefox":
        os.system("winget install Mozilla.Firefox")
    elif program == "Discord":
        os.system("winget install Discord.Discord")
    elif program == "Opera Browser":
        os.system("winget install Opera.Opera")
    elif program == "Messenger":
        os.system("winget install 9WZDNCRF0083")
    elif program == "Roblox Player":
        os.system("winget install Roblox.Roblox")
    elif program == "Steam":
        os.system("winget install Valve.Steam")
    elif program == "VSCode":
        os.system("winget install Microsoft.VisualStudioCode")
    elif program == "Chrome":
        os.system("winget install Google.Chrome")
    elif program == "Microsoft 365 (Office)":
        os.system("winget install 9WZDNCRD29V9")
    elif program == "Python 3.12":
        os.system("winget install Python.Python.3.12")
    elif program == "Spotify":
        os.system("winget install Spotify.Spotify")
    elif program == "Prism Launcher":
        os.system("winget install PrismLauncher.PrismLauncher")
    Label1.configure(text="Installed successfully!")
    Label1.place_configure(x=57.5)
    switch_page(Page_1)

def startinstall():
    global Page_3, Label2, WIDTH, HEIGHT
    Label2.configure(text="Installing...")
    HEIGHT = 150
    WIDTH = 250
    switch_page(Page_3)
    root.geometry((f"{WIDTH}x{HEIGHT}"))
    installing = threading.Thread(target=install)
    installing.start()

OptionMenu1 = customtkinter.CTkOptionMenu(master=Page_2, values=["Firefox", "Discord", "Opera Browser", "Messenger", "Roblox Player", "Steam", "VSCode", "Chrome", "Microsoft 365 (Office)", "Python 3.12", "Spotify", "Prism Launcher"])
OptionMenu1.place(x=145, y=30)

Button1 = customtkinter.CTkButton(master=Page_2, text="Install", command=lambda: startinstall())
Button1.place(x=50, y=95)

Button3 = customtkinter.CTkButton(master=Page_2, text="Uninstall", command=lambda: startuninstall())
Button3.place(x=220, y=95)

Button2 = customtkinter.CTkButton(master=Page_1, text="Continue", command=lambda: startProgram())
Button2.place(x=55, y=95)

Label1 = customtkinter.CTkLabel(master=Page_1, text="Welcome to the Mini App Store")
Label1.place(x=45, y=30)

Label2 = customtkinter.CTkLabel(master=Page_3, text="Installing...")
Label2.place(x=45, y=30)

root.mainloop()