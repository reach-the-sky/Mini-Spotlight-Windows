import webbrowser
import tkinter as tk
from tkinter import scrolledtext
import PyDictionary

root = tk.Tk()
root.title("Smart Search")
root.geometry("600x25")
root.overrideredirect(True)

# Position
windowWidth = root.winfo_reqwidth() + 400
windowHeight = root.winfo_reqheight() + 250
print("Width", windowWidth, "Height", windowHeight)

positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

root.geometry("+{}+{}".format(positionRight, positionDown))


inputText = tk.Entry(root,width=600,border=2,font=('Century 12'))
inputText.pack()
inputText.focus_set()

printText = scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 600, height = 300, font = ("Times New Roman", 12))

printText.pack()

printText.configure(state="disabled")


def close(events = ""):
    root.destroy()

def showWindow(events = ""):
    root.deiconify()

def functionality(event = ""):
    input = inputText.get()
    if "google" == input[:6].lower():
        webbrowser.open("https://google.com/search?q="+input[7:],autoraise=True)
        root.after(1000, lambda: root.quit())

    elif "dict" == input[:4].lower():
        temp = PyDictionary.PyDictionary()
        meaning = temp.meaning(input[5:])
        message = "Meaning: " + input[5:]
        try:
            count = 1
            for _ in meaning.keys():
                message += "\n"+_ + ": \n"
                count = 1
                for __ in meaning[_]:
                    message += "\t"+str(count)+". " + __ + "\n"
                    count += 1
        except:
            message = "No definition found"
        # printText["text"] = message
        printText.configure(state="normal")
        printText.delete("0.0",tk.END)
        printText.insert(tk.INSERT,message)
        printText.configure(state="disabled")
        root.geometry("600x300")
        inputText.delete(0, "end")

    elif "wiki" == input[:4].lower():
        webbrowser.open("https://en.wikipedia.org/w/index.php?search=" + input[5:])
        root.after(1000, lambda: root.quit())

    elif "help" == input[:4].lower():
        message = """
google [Search Text] : Searches for the [Search Text] on Google in default browser.

duck [Search Text] : Searches for the [Search Text] on DuckDuckGo in default browser.

wiki [Search Text] : Searches for the [Search Text] on Wikipedia in default browser.
        
dict [Search Text] : Shows the meaning of [Search Text].
        
help : Documentation and functionalities discription of the Application. 
        """
        printText.configure(state="normal")
        printText.delete("0.0", tk.END)
        printText.insert(tk.INSERT, message)
        printText.configure(state="disabled")
        root.geometry("600x300")
        inputText.delete(0, "end")

    elif "duck" == input[:4].lower():
        webbrowser.open("https://duckduckgo.com/?q=" + input[5:])
        root.after(1000, lambda: root.quit())

    elif input[0] == ">":
        message = " = "+str(eval(input[1:]))
        printText.configure(state="normal")
        printText.delete("0.0", tk.END)
        printText.insert(tk.INSERT, message)
        printText.configure(state="disabled")
        root.geometry("600x50")

# Binding Enter
root.bind('<Return>', functionality)
# Binding ESC
root.bind('<Escape>', close)


tk.mainloop()
