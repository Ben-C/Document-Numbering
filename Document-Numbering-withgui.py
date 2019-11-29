from tkinter import *


class project_details:
    ## Capturing input information and inputing in to libraries.##
    def project_code(self, entered_pro_code):
        self.entered_pro_code = pro_code.get()
  
    def project_origins(self, entered_origin):
        self.entered_origin = origin.get()

    def document_code(self, entered_doc_code):
        self.enetered_doc_code = doc_code.get()

    def disciplin_code(self, entered_disciplin):
        self.entered_disciplin = disciplin.get()

def get_doctype():
    ## Defining project properties.##
    doc_type[DR, SP, PL, RP, SC, ]
   
    
    project = project_details()
    origin = project_details()
    document = project_details()
    project_disciplin = project_details()

       
    window = Tk()
    window.title("Project properties input")
#   photo1 = PhotoImage(file="image.gif")
    Label (window, image=photo1) .grid(row=0, column=1, sticky=E)
    Label (window, text="Please enter project code: ", font="none, 12") .grid(row=2, column=1, sticky=E)
    
    pro_code = Entry(window, width=25, bg="white")
    pro_code.grid(row=2,column=2,sticky=W)
#    Label (window, text=" ").grid(row=3, column=1)
#    Label (window, text=" ").grid(row=3, column=2)
    Label (window, text="Please enter originator: (i.e. Arup = ARP)", font="none, 12").grid(row=4, column=1, sticky=E)

    origin = Entry(window, width=25, bg="white")
    origin.grid(row=4, column=2, sticky=W)
#    Label (window, text=" ").grid(row=5, column=1)
#    Label (window, text=" ").grid(row=5, column=2)
    Label (window, text="Please enter document type: (i.e. Plan = PL, Drawing = DW)", font="none, 12").grid(row=6, column=1, sticky=E)

    doc_code = Entry(window, width=25, bg="white")
    doc_code.grid(row=6, column=2, sticky=W)
   
    Label (window, text="Please enter disciplin: (i.e. Structures = S)", font="none, 12").grid(row=8, column=1, sticky=E)

    disciplin = Entry(window, width=25, bg="white")
    disciplin.grid(row=8, column=2, sticky=W)

    window.mainloop()

if __name__=="__main__":
    get_doctype()
    
print (project_details)


