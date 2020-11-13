# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:18:32 2020

@author: Estudio
"""
import PyInstaller
import requests,re, bs4#
from tkinter import *
#definitions
''''''''''''''''''''''''''''''''''''''''''''''''''''''
def Sumbit():
    ########## Variables ############
       search=entry_conv.get()
       n=float(entry_n.get())
       
       def fahrenheit2celsius(temp):
            """
            Returns temperature in Celsius given Fahrenheit temperature.
            """
            result=(5. / 9.) * (temp - 32)
            return result
       def celsius2fahrenheit(temp):
           """
           Returns temperature in Fahrenheit given Celsius temperature.
           """
           result=(((9./5.) * (temp)) + 32)
           return result
        
        # request data from google.com#
       res = requests.get('https://google.com/search?q='+ search)
         
        #checking if connection was successful#       
       res.raise_for_status()
        #Parsing HTML
       soup= bs4.BeautifulSoup(res.text, 'html.parser')
        # dowloading web page content
      
        # to validate the user input by searching numbers
       searchbool=re.findall(r'-?\d+\.?\d*',search)
        #Find digits in the web content
       numbers=re.findall(r'-?\d+\.?\d*',soup.text)
        # if input is not correct
       if len(searchbool)>0:
           print('Please introduce the conversion in the correct format, for example: try squared meters instead of m2')
            #continue
       tem=(re.findall("temperature",soup.text))
       a=(re.findall("convert",soup.text))
        #webbrowser.open('https://google.com/search?q='+ search)
        # if conversion
       if len(a) != 0 and len(tem)==0:
           a=True
           conversion=float(numbers[2])
           result=conversion* n
      
        
       else:
           if search.upper()[0]=='F':
               result=fahrenheit2celsius(n)
               
           else:
               result=celsius2fahrenheit(n)
              
       label_res=Label(framed, text='                                                                               ')
       label_res.grid(row=3,column=0)
       label_res=Label(framed, text='The equivalent value is '+str(result))
       label_res.grid(row=3,column=0)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def Reset():
    entry_conv.delete(0,'end')
    entry_n.delete(0,'end')
   

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
root = Tk()
root.geometry('400x125')
framed=LabelFrame(root, text='Unit Converter, powered by Google.com')
label_conv=Label(framed,text='Conversion Type')
label_n=Label(framed,text='Quantity')
label_res=Label(framed,text='')
entry_conv=Entry(framed)
entry_n=Entry(framed)
sumbit_button= Button(framed, text='Sumbit',padx=10,command=Sumbit)
reset_button= Button(framed, text='Reset',padx=10,command=Reset)

#packing
framed.pack()
sumbit_button.grid(row=2,column=1)
entry_conv.grid(row=1,column=0)
entry_n.grid(row=1,column=1)
label_conv.grid(row=0,column=0)
label_n.grid(row=0,column=1)
reset_button.grid(row=2,column=0)
############
root.mainloop()
dir(Entry)


! pyinstaller GUIconv.py