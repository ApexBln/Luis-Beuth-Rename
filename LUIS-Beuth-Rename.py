from tkinter import Tk,Button,Frame,Label,filedialog, ttk
import os as os
import tkinter as tkinter

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)        
        #root.geometry("500x350")
        root.title("Rename it!")
        root.attributes('-zoomed', True)
        self.lst_abschluss = ['Bachelor','Master','Unbekannt']
        self.var_abschluss = tkinter.StringVar()
        self.var_abschluss.set("unbekannt")    
        self.lst_studiengang = ['BA_Bauingenieurwesen','BA_Umweltingenieurwesen-  Bau','BA_Wirtschaftsingenieurwesen- Bau','BA_Geoinformation', 'MA_Wirtschaftsingenieurwesen- Bau', 'MA_Bauingenieurwesen', 'MA_Geoinformation', 'MA_Umweltinformation- GIS', 'Unbekannt']
        self.var_studiengang = tkinter.StringVar()
        self.var_studiengang.set("unbekannt")        
        self.lst_modul = ['modul','Option2','Option3', 'Unbekannt']
        self.var_modul = tkinter.StringVar()
        self.var_modul.set("unbekannt")        
        self.lst_semester = ['vor2009','SS_09','WS_0910','SS_10','WS_1011','SS_11','WS_1112','SS_12','WS_1213','SS_13','WS_1314','SS_14','WS_1415','SS_15','WS_1516','SS_16','WS_1617','SS_17','WS_1718','SS_18','WS_1819','SS_19','WS_1920','SS_20','WS_2021','SS_21','WS_2122', 'Unbekannt']
        self.var_semester = tkinter.StringVar()
        self.var_semester.set("unbekannt")        
        self.lst_dozent = ['Axmann','Beck','Berger','Bergmann','Breuer','Dick','Domnick','Fehlau','Fischer','Füsser','Gierloff','Hanschke','Hehl','Heider','Heimann','Himburg','Keck','Kickler','Korth','Kramp','Lutz','Meyn','Möller','Nielsen','Pohlmann','Prietz','Resnik','Ripke','Rösler','Schneider','Schomacker','Schweikart','Selle','Stempfhuber','Wagner','Weiß', 'Unbekannt']
        self.var_dozent = tkinter.StringVar()
        self.var_dozent.set("unbekannt")        
        self.lst_przr = ['PRZ_1','PRZ_2', 'Unbekannt']
        self.var_przr = tkinter.StringVar()
        self.var_przr.set("unbekannt")        
        self.lst_version = ['version','Option2','Option3', 'Unbekannt']
        self.var_version = tkinter.StringVar()
        self.var_version.set("unbekannt")        
        self.lst_note = ['1,0','1,3','1,7','2,0','2,3','2,7','3,0','3,3','3,7','4,0','oE', 'Unbekannt']
        self.var_note = tkinter.StringVar()
        self.var_note.set("unbekannt")        
        self.create_widgets()
        self.drop_refresh()
    
    
    
    def create_widgets(self):
        self.abschluss_l = Label(root,text="Abschluss:  ")
        self.abschluss_l.grid(row=0,column=0,sticky='w')
        self.studiengang_l = Label(root,text="Studiengang:  ")
        self.studiengang_l.grid(row=1,column=0,sticky='w')
        self.modul_l = Label(root,text="Modulname:  ")
        self.modul_l.grid(row=2,column=0,sticky='w')
        self.semester_l = Label(root,text="Semester:  ")
        self.semester_l.grid(row=3,column=0,sticky='w')
        self.dozent_l = Label(root,text="Dozent:  ")
        self.dozent_l.grid(row=4,column=0,sticky='w')        
        self.przr_l = Label(root,text="Prüfungszeitraum:  ")
        self.przr_l.grid(row=5,column=0,sticky='w')        
        self.version_l = Label(root,text="Version:  ")
        self.version_l.grid(row=6,column=0,sticky='w')        
        self.note_l = Label(root,text="Note:  ")
        self.note_l.grid(row=7,column=0,sticky='w')

        self.select_button = Button(root,text="Datei",command=self.datei_umbennen)
        self.select_button.grid(row=8,column=0)
        self.save_button = Button(root,text="Save",command=self.save_file)
        self.save_button.grid(row=8,column=1)

        self.ausgabe_label = Label(root,text='')
        self.ausgabe_label.grid(row=9,columnspan=1000)
        
        self.vorschau_button = Button(root,text="Dateiname Vorschau",command=self.dateiname_vorschau)
        self.vorschau_button.grid(row=10,column=0)
        
        self.add_modul_b = Button(root, text="Modul hinzufügen",command=self.add_modul)
        self.add_modul_b.grid(row=2,column=2)
        self.add_dozent_b = Button(root, text="Dozent hinzufügen",command=self.add_dozent)
        self.add_dozent_b.grid(row=4,column=2)
        
        
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
        
    
    def datei_umbennen(self):
        self.filepath=filedialog.askopenfilename()
        self.filename=os.path.basename(self.filepath)
        
    def dateiname_vorschau(self):
        self.newName = self.var_abschluss.get()+"_"+self.var_studiengang.get()+"_"+self.var_modul.get()+"_"+self.var_semester.get()+"_"+self.var_dozent.get()+"_"+self.var_przr.get()+"_"+self.var_version.get()+"_"+self.var_note.get()+".pdf"
        self.ausgabe_label['text']=self.newName
        
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

root = Tk()
app = Application(master=root)
app.mainloop()