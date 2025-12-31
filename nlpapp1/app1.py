#for gui designing
from tkinter import *
from tkinter import messagebox
#for data storing
from mydb import Database
#for api class
from myapi import API

class NLPApp:

   
    def __init__(self):

        self.dbo = Database()
        self.apio = API()

        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap()
        self.root.geometry('350x600')
        self.root.configure(bg = "#34495E")
        self.login_gui()
        self.root.mainloop()

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

#login gui creation

    def login_gui(self):
        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=50)
        self.password_input.pack(pady=(5,10),ipady=4)

        login_button = Button(self.root,text = 'Login',width = 30,height=2,command=self.perform_login)
        login_button.pack(pady=(10,10))
        label3 = Label(self.root,text='Not a member?')
        label3.pack(pady=(20,10))

        redirect_button = Button(self.root,text='Register Now',command=self.register_gui)
        redirect_button.pack(pady=(10,10))

#Registration gui creation

    def register_gui(self):
        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label0 = Label(self.root,text='Enter Name')
        label0.pack(pady=(10,10))

        self.name_input = Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=4)

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=50)
        self.password_input.pack(pady=(5,10),ipady=4)

        registrer_button = Button(self.root,text = 'Register ',width = 30,height=2,command=self.perform_reg)
        registrer_button.pack(pady=(10,10))
        label3 = Label(self.root,text='Already a member?')
        label3.pack(pady=(20,10))

        redirect_button = Button(self.root,text='Login',command=self.login_gui)
        redirect_button.pack(pady=(10,10))

#method for registration

    def perform_reg(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response=self.dbo.add_data(name,email,password)
        if response:
            messagebox.showinfo('Success','Registration successful.you can login now')
        else:
            messagebox.showerror('Error','Email already exists')

#method for login

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response=self.dbo.search(email,password)

        if response:
            messagebox.showinfo('Success','Login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','incorrect email/password')

#Home page for menu

    def home_gui(self):
        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        sentiment_button = Button(self.root,text = 'Sentiment Analysis ',width = 30,height=2,command=self.sentiment_ana_gui)
        sentiment_button.pack(pady=(10,10))

        ner_button = Button(self.root,text = 'Named Entity Recognition ',width = 30,height=2,command=self.ner_ana_gui)
        ner_button.pack(pady=(10,10))

        language_detection= Button(self.root,text = 'Language Detection ',width = 30,height=2,command=self.language_detection_gui)
        language_detection.pack(pady=(10,10))

        logout_button = Button(self.root,text = 'logout ',width = 30,height=2,command=self.login_gui)
        logout_button.pack(pady=(10,10))

#Sentiment analysis gui

    def sentiment_ana_gui(self):
        self.clear()
        heading = Label(self.root,text='Sentiment Analysis',bg='#34495E',fg='white')
        heading.pack(pady=(10,20))
        heading.configure(font=('verdana',12))

        label1 = Label(self.root,text='Enter Text')
        label1.pack(pady=(10,10))

        self.sentiment_input = Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(5,10),ipady=4)

        sentiment_button = Button(self.root,text = 'Analyze Sentiment ',width = 30,height=2,command=self.perform_senti_ana)
        sentiment_button.pack(pady=(10,10))

        self.sentiment_res = Label(self.root,text='',bg='#34495E',fg='white')
        self.sentiment_res.pack(pady=(10,10))
        self.sentiment_res.configure(font=('verdana',20))
        

        goback_button = Button(self.root,text = 'Home ',width = 30,height=2,command=self.home_gui)
        goback_button.pack(pady=(10,10))

#sentiment analyzing method

    def perform_senti_ana(self):
        text = self.sentiment_input.get()
        try:
            result = self.apio.sentiment_analysis(text)
        except Exception:
            self.sentiment_res['text']='you reached maximum limit'            
        else:
            formated_output = ""

            for item in result["scored_labels"]:
             
             formated_output += f"Label:{item['label']}\n"
             formated_output += f"Score:{item['score']}\n\n"

            self.sentiment_res['text']=formated_output

#Name entity recognition gui   

    def ner_ana_gui(self):
        self.clear()
        heading = Label(self.root,text='Name Entity Recognition ',bg='#34495E',fg='white')
        heading.pack(pady=(10,20))
        heading.configure(font=('verdana',12))

        label1 = Label(self.root,text='Enter Text')
        label1.pack(pady=(10,10))

        self.ner_input = Entry(self.root,width=50)
        self.ner_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text='Enter Search Entity')
        label2.pack(pady=(10,10))

        self.search_input = Entry(self.root,width=50)
        self.search_input.pack(pady=(5,10),ipady=4)

        ner_button = Button(self.root,text = 'Analyze Entity ',width = 30,height=2,command=self.perform_ner_ana)
        ner_button.pack(pady=(20,20))

        self.ner_res = Label(self.root,text='',bg='#34495E',fg='white')
        self.ner_res.pack(pady=(10,10))
        self.ner_res.configure(font=('verdana',20))
        

        goback_button = Button(self.root,text = 'Home ',width = 30,height=2,command=self.home_gui)
        goback_button.pack(pady=(10,10))

#Name entity recognition method

    def perform_ner_ana(self):
        text = self.ner_input.get()
        search_entity = self.search_input.get().upper()
        try:
            result = self.apio.ner_analysis(text)
        except Exception:
            self.ner_res['text']='Error while analyzing entities'
        else:
            matches = []
            for ent in result['entities']:
                if ent['label']==search_entity:
                    matches.append(ent['text'])

            if matches:
             output = f'Entity type:{search_entity}\n\n'
            for i,m in enumerate(matches,1):
                    output+=f'{i}.{m}\n'
            else:
             output = f'No entities of type "{search_entity}"found'

            self.ner_res['text']=output

#Language detection gui

    def language_detection_gui(self):
        self.clear()
        heading = Label(self.root,text='Language Derection',bg='#34495E',fg='white')
        heading.pack(pady=(10,20))
        heading.configure(font=('verdana',12))

        label1 = Label(self.root,text='Enter Text')
        label1.pack(pady=(10,10))

        self.language_input = Entry(self.root,width=50)
        self.language_input.pack(pady=(5,10),ipady=4)

        language_button = Button(self.root,text = 'Detect Language ',width = 30,height=2,command=self.perform_language_detection)
        language_button.pack(pady=(10,10))

        self.language_res = Label(self.root,text='',bg='#34495E',fg='white')
        self.language_res.pack(pady=(10,10))
        self.language_res.configure(font=('verdana',20))
        

        goback_button = Button(self.root,text = 'Home ',width = 30,height=2,command=self.home_gui)
        goback_button.pack(pady=(10,10))

##Language detection method

    def perform_language_detection(self):
        text = self.language_input.get()

        try:
            result = self.api.language_detection(text)
        except Exception:
            self.language_res["text"] = "Error detecting language"
        else:

        
            language = result.get("language", "Unknown")
            code = result.get("code", "").upper()
            confidence = result.get("confidence", None)

            output = "Detected Language\n"
            output += "-----------------\n"
            output += f"Language : {language}\n"
            output += f"Code     : {code}\n"

            if confidence is not None:
                output += f"Confidence : {confidence * 100:.2f}%"

            self.language_res["text"] = output


nlp = NLPApp()

