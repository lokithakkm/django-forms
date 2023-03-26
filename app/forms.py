
from django import forms
g=[['MALE','male'],('FEMALE','female')]
c=[['PYTHON','python'],['DJANGO','django']]
class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    


class TopicForm(forms.Form):
    topic=forms.CharField(max_length=100)
    date=forms.DateField()
