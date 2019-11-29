from tkinter import *
import datetime


def click():
    entered_pro_code = pro_code.get()

def get_doctype(click):
    """ Allows users to input project information. Such as project code, orginator, document type and discipline"""
    project_code = []
    originator = []
    document_type = []
    discipline_type = []
    user_cancel = True

    window = Tk()
    window.title("Project properties input")    
    photo1 = PhotoImage(file="Arup.gif")
    Label (window, image=photo1) .grid(row=0, column=3, sticky=E)
    Label (window, text="Please enter project code: ", font="none 12") .grid(row=2, column=0, sticky=E)    
    
    pro_code = Entry(window, width=20, bg="white")
    pro_code.grid(row=2, column=1, sticky=E)
    project_code.append(entered_pro_code)
    
    origin = input("Please set originator: \n")
    originator.append(origin)

    doc_type = input("Please set document types: \n")
    document_type.append(doc_type)
    while user_cancel is True:
        cancel_question = input("Would you like to add another item (Y/N): \n")
        if cancel_question is 'Y':
           cancel_answer = input("Please enter another document type: \n")
           document_type.append(cancel_answer)
        else:
            user_cancel = False
    
    user_cancel = True
    
    dis_type = input("Please set disciplines working on this project: \n")
    while user_cancel is True:
        cancel_question = input("Would you like to add another item (Y/N): \n")
        if cancel_question is 'Y':
           cancel_answer = input("Please enter another discipline code: \n")
           discipline_type.append(cancel_answer)
        else:
            user_cancel = False
            
    print (project_code)
    print (originator)
    print (document_type)
    print (discipline_type)

    window.get_doctypeloop()



#def tk_GUI():
    """ Define gui elements which have drop down menus with pre populated list items."""
#    document_type = []

if __name__=="__main__":
    get_doctype(click)