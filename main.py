from gui import *

def main():
    window = Tk()
    window.title('REMOTE')
    window.geometry('240x500')
    window.resizable(False,False)
    Gui(window)
    window.mainloop()


if __name__ == "__main__":
    main()