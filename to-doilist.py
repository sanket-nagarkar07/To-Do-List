from tkinter import *
import random

root=Tk()
root.geometry("200x500")   

tasks=[]      # empty list

tasks=["call rohit", "buy car" , "eat vadapav"]   #sample list

def update_listbox():
#clear the current list
    clear_listbox()
     #populate the list box
    for task in tasks:
        lb_tasks.insert("end" , task)

def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
    #get task to add 
    task = txt_input.get()
    #make sure the task is not empty
    if task !="":
        #Append to the list
        tasks.append(task)
        #update the list
        update_listbox()
    else:
        lbl_display["text"] ="please enter a task"
    txt_input.delete(0,"end")
def del_all():
    #since we are changing the list , it needs to be a global
    global tasks
    #clear the taks list
    tasks =[]
    #update the listbox
    update_listbox()
    

def del_one():
    #get the text of the currently selected item
    task = lb_tasks.get("active")
    #conform it is in the list
    if task in tasks:
        tasks.remove(task)
    #update the listbox
    update_listbox() 

def choose_random():
    #choose a random task
    task = random.choice(tasks)
    #update the display label
    lbl_display["text"] = task

def exit_task():
    root.destroy()   # close the application


lbl_titile=Label(root,text="To-DO-List", bg="white")
lbl_titile.pack()

lbl_display=Label(root,text="" ,bg="white")
lbl_display.pack()
#take input value 
txt_input=Entry(root,width=15)
txt_input.pack()
#Add Button
btn_add_task=Button(root,text="Add Task" , fg="green", bg="white",command=add_task )
btn_add_task.pack(pady=5)
#delete all button
btn_del_all=Button(root,text="Delete all" , fg="green", bg="white",command=del_all)
btn_del_all.pack(pady=5)
#Delete button
btn_sort_asc=Button(root,text="Delete " , fg="green", bg="white",command=del_one)
btn_sort_asc.pack(pady=5)
#random Button
btn_quit=Button(root,text="Random" , fg="green", bg="white",command=choose_random)
btn_quit.pack(pady=5)
#exit button
btn_quit=Button(root,text="EXit" , fg="green", bg="white",command=exit_task)
btn_quit.pack(pady=5)
#create list box
lb_tasks=Listbox(root)
lb_tasks.pack()

root.mainloop()