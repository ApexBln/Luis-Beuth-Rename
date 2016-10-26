from tkinter import Tk,Button,Frame,Label,filedialog, ttk, Menu, Toplevel
import os as os
import tkinter as tkinter
import csv as csv
#To Do
"""
-Studium Generale rein (Liste + CSV), zweites Dropdown
-If-BA/MA Abfragen zu Studiengängen
-Main Menü (Datei,Optionen,Info/About) erstellen
-Öffnen der Ursprungsdatei (Vorschau)
"""
class Application(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)        
       
        self.lst_abschluss=[]        
        #print("Leer: ",self.lst_abschluss)        
        self.lst_studiengang=[]
        self.lst_modul=[]
        self.lst_semester=[]
        self.lst_dozent=[]
        self.lst_przr=[]
        self.lst_version=[]
        self.lst_note=[]
        self.total_content=[]
        with open('LOUIS-Beuth-Renamer.csv','r',newline='')as csvfile:
            for row in csv.reader(csvfile):
                    self.total_content.append(row)
        self.lst_abschluss=self.total_content[0]
        self.lst_studiengang=self.total_content[1]
        self.lst_modul=self.total_content[2]
        self.lst_semester=self.total_content[4]
        self.lst_dozent=self.total_content[3]
        self.lst_przr=self.total_content[5]
        self.lst_version=self.total_content[6]
        self.lst_note=self.total_content[7]
        #print(self.lst_abschluss)
        #print(self.lst_studiengang)
                             

        self.var_abschluss = tkinter.StringVar()
        self.var_abschluss.set("unbekannt")    

        self.var_studiengang = tkinter.StringVar()
        self.var_studiengang.set("unbekannt")        
        
        self.var_modul = tkinter.StringVar()
        self.var_modul.set("unbekannt")        

        self.var_semester = tkinter.StringVar()
        self.var_semester.set("unbekannt")        

        self.var_dozent = tkinter.StringVar()
        self.var_dozent.set("unbekannt")        

        self.var_przr = tkinter.StringVar()
        self.var_przr.set("unbekannt")        

        self.var_version = tkinter.StringVar()
        self.var_version.set("unbekannt")        

        self.var_note = tkinter.StringVar()
        self.var_note.set("unbekannt")        
        self.create_widgets()
        self.drop_refresh()
        self.mainmenu()
    
    
    def create_widgets(self):
        self.abschluss_l = Label(root,text="Abschluss:  ")
        self.abschluss_l.grid(row=0,column=0,sticky='w')
        self.studiengang_l = Label(root,text="Studiengang:  ")
        self.studiengang_l.grid(row=1,column=0,sticky='w')
        self.modul_l = Label(root,text="Modulname:  ")
        self.modul_l.grid(row=2,column=0,sticky='w')
        self.semester_l = Label(root,text="Semester:  ")
        self.semester_l.grid(row=4,column=0,sticky='w')
        self.dozent_l = Label(root,text="Dozent:  ")
        self.dozent_l.grid(row=3,column=0,sticky='w')        
        self.przr_l = Label(root,text="Prüfungszeitraum:  ")
        self.przr_l.grid(row=5,column=0,sticky='w')        
        self.version_l = Label(root,text="Version:  ")
        self.version_l.grid(row=6,column=0,sticky='w')        
        self.note_l = Label(root,text="Note:  ")
        self.note_l.grid(row=7,column=0,sticky='w')

        self.select_button = Button(root,text="Datei",command=self.datei_waehlen)
        self.select_button.grid(row=8,column=0,sticky='w')
        
        self.save_button = Button(root,text="Save",command=self.save_file)
        self.save_button.grid(row=8,column=0,sticky='e')

        self.vorschau_label = Label(root,text='')
        self.vorschau_label.grid(row=11,columnspan=1000)
        self.datei_label = Label(root,text='Datei:  ')
        self.datei_label.grid(row=9,column=0,sticky='w')
        self.datei_gewaehlt = Label(root,text='')
        self.datei_gewaehlt.grid(row=9,column=1)
        
        self.vorschau_button = Button(root,text="Dateiname Vorschau",command=self.dateiname_vorschau)
        self.vorschau_button.grid(row=10,column=0)
        
        self.add_modul_b = Button(root, text="Modul hinzufügen",command=self.add_modul)
        self.add_modul_b.grid(row=2,column=2)
        
        self.add_dozent_b = Button(root, text="Dozent hinzufügen",command=self.add_dozent)
        self.add_dozent_b.grid(row=3,column=2)
        
        
    def drop_refresh(self):                             
        self.drop_abschluss = ttk.Combobox(root,textvariable=self.var_abschluss,values=self.lst_abschluss)
        self.drop_abschluss.grid(row=0,column=1)
        self.drop_studiengang = ttk.Combobox(root,textvariable=self.var_studiengang,values=self.lst_studiengang)
        self.drop_studiengang.grid(row=1,column=1)
        self.drop_modul = ttk.Combobox(root,textvariable=self.var_modul,values=self.lst_modul)
        self.drop_modul.grid(row=2,column=1)
        self.drop_semester = ttk.Combobox(root,textvariable=self.var_semester,values=self.lst_semester)
        self.drop_semester.grid(row=3,column=1)
        self.drop_dozent = ttk.Combobox(root,textvariable=self.var_dozent,values=self.lst_dozent)
        self.drop_dozent.grid(row=4,column=1)
        self.drop_przr = ttk.Combobox(root,textvariable=self.var_przr,values=self.lst_przr)
        self.drop_przr.grid(row=5,column=1)
        self.drop_version = ttk.Combobox(root,textvariable=self.var_version,values=self.lst_version)
        self.drop_version.grid(row=6,column=1)
        self.drop_note = ttk.Combobox(root,textvariable=self.var_note,values=self.lst_note)
        self.drop_note.grid(row=7,column=1)
        
    
    def datei_waehlen(self):
        self.filepath=filedialog.askopenfilename()
        self.filename=os.path.basename(self.filepath)
        if self.filename != '':
            self.datei_gewaehlt['text']=self.filename
        
    def dateiname_vorschau(self):
        self.newName = self.var_abschluss.get()+"_"+self.var_studiengang.get()+"_"+self.var_modul.get()+"_"+self.var_semester.get()+"_"+self.var_dozent.get()+"_"+self.var_przr.get()+"_"+self.var_version.get()+"_"+self.var_note.get()+".pdf"
        self.vorschau_label['text']=self.newName
        
    def target_directory(self):
        self.EndPath = self.var_abschluss.get()+"/"+self.var_studiengang.get()+"/"+self.var_modul.get()+"/"+self.var_semester.get()+"/"+self.var_dozent.get()      
        
    def new_name(self):
        self.newName = self.var_abschluss.get()+"_"+self.var_studiengang.get()+"_"+self.var_modul.get()+"_"+self.var_semester.get()+"_"+self.var_dozent.get()+"_"+self.var_przr.get()+"_"+self.var_version.get()+"_"+self.var_note.get()+".pdf"
        
        
    def make_dir(self):
        if not os.path.exists(self.EndPath):
            os.makedirs(self.EndPath)
            
    def add_modul(self):
        eintrag = self.var_modul.get()
        if not eintrag in self.lst_modul:
            
            self.lst_modul.append(eintrag)
        print(eintrag,self.lst_modul)
        self.drop_refresh()
            
    def add_dozent(self):
        self.create_window()        
        eintrag = self.var_dozent.get()
        if not eintrag in self.lst_dozent:
            self.lst_dozent.append(eintrag)

    def save_file(self):
        self.drop_refresh()
        self.target_directory()
        self.new_name()
        self.make_dir()
        os.rename(self.filepath,self.EndPath+"/"+self.newName)
        print(self.EndPath+"/"+self.newName)
            
 
    def mainmenu(self):
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)      
        filemenu.add_separator()      
        filemenu.add_command(label="Exit", command=self.donothing)    
        menubar.add_cascade(label="Datei", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Dozent hinzufügen", command=self.add_dozent)
        editmenu.add_command(label="Modul hinzufügen", command=self.donothing)
        editmenu.add_command(label="Noch nicht genutzt", command=self.donothing)
       
        menubar.add_cascade(label="Bearbeiten", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="About", menu=helpmenu)

    def donothing(self):
        button = Button(root, text="Do nothing button")
        button.pack()
       
    def create_window(self):
        t = Toplevel(self)
        t.wm_attributes('-topmost',-1)
        t.wm_title("Window" )
        l = Label(t, text="This is window " )
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)      
      
root = Tk()
root.title("LUIS Beuth Renamer") 
menubar=Menu(root)
root.config(menu=menubar)
root.wm_attributes('-topmost',-1)
try:
     root.state('zoomed')
except tkinter.TclError:
     root.attributes('-zoomed', True) 
app = Application(parent=root)
app.mainloop()