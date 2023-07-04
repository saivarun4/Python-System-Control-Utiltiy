import os
from tkinter import *

def shutdown(  ):
    return os.system( 'shutdown /s /t 1' )
def restart(  ):
    return os.system( 'shutdown /r /t 1' )
def logout(  ):
    return os.system( 'shutdown /l' )
root = Tk()
root.configure( bg = 'light grey' )
Button( root , text = 'Shutdown' , command = shutdown  ).pack()
Button( root , text = 'Restart' , command = restart  ).pack()
Button( root , text = 'Logout' , command = logout  ).pack()
root.mainloop()