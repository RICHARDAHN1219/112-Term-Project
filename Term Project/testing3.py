import tkinter as tk


class PlayerInfo:
    player1 = ""
    player2 = ""
    root= tk.Tk()

    canvas1 = tk.Canvas(PlayerInfo.root, width = 400, height = 300)
    canvas1.pack()

    nameEntry = tk.Entry (PlayerInfo.root) 
    canvas1.create_window(200, 140, window=nameEntry)

    def getSquareRoot ():  
        name = PlayerInfo.nameEntry.get()
        name2 = PlayerInfo.nameEntry.get()
        
        label1 = tk.Label(root, text= f"Player 1 Name is {name}")
        PlayerInfo.canvas1.create_window(200, 230, window=label1)
        label2 = tk.Label(root, text =  f"Player 2 Name is {name2}")
        PlayerInfo.canvas1.create_window(200, 230, window=label2)
        PlayerInfo.player1 = name
        PlayerInfo.player2 = name2
        
    button1 = tk.Button(text='Enter Name', command=getSquareRoot)
    canvas1.create_window(200, 180, window=button1)

    root.mainloop()
