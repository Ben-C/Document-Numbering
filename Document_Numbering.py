import tkinter
import datetime


def get_doctype():
    """ Allows users to input project information. Such as project code, orginator, document type and discipline"""
    project_code = []
    originator = []
    document_type = []
    discipline_type = []
    user_cancel = True
    
    pro_code = input("Please enter project code: \n")
    project_code.append(pro_code)
    
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





#def tk_GUI():
    """ Define gui elements which have drop down menus with pre populated list items."""
#    document_type = []

if __name__=="__main__":
    get_doctype()