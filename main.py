from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *

#Declaring a variable fro ChatBot object
chatbot = ChatBot("Pybot")


#Training the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')

# Now we can export the data to a file
trainer.export_for_training('./my_export.json')

#Calling the tkinter library
main = Tk()

main.geometry("500x510")

main.title("Chaty: Virtual Assitant")

#Adding the chatbot icon
icon = PhotoImage(file="chaty.jpg")
photol = Label(main,image=icon)
photol.pack(pady=5)

#Function to display conversation
def ask_chaty():
    query = textF.get()
    answer = chatbot.get_response(query)
    msgs.insert(END,"User: "+query)
    msgs.insert(END,"Chaty: "+str(answer))
    textF.delete(0,END)

frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=15, font=("Courier 11",12), fg="maroon")

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

textF = Entry(main,font=("Verdana",12), fg="blue")
textF.pack(fill=X, pady=5, padx=5)
 
btn = Button(main, text="Ask Chaty", font=("Verdana",12), command=ask_chaty, bg="maroon",fg="white",)
btn.pack()

main.mainloop()