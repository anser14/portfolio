from django import forms

class Client_message(forms.Form):
    name= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Enter your name','class':'nme'}))
    email= forms.CharField(max_length=250,
                           widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your e-mail','class':'emi'}))
    message= forms.CharField(max_length=500,
                           widget=forms.Textarea
                           (attrs={'placeholder':'Enter your message '}))


    
