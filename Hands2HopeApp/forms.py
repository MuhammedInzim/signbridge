from django.forms import ModelForm

from .models import *

class ComplaintsForm(ModelForm):
    class Meta:
        model=ComplaintsTable
        fields=['Complaints']


class ReplyForm(ModelForm):
    class Meta:
        model =ComplaintsTable
        fields=['Reply']

class UserForm(ModelForm):
    class Meta:
        model=UserTable
        fields=['Name','Age','Gender','Email','Phone_no','Place']

class FeedbackForm(ModelForm):
    class Meta:
        model=FeedbackTable
        fields=['Rating','Feedback']
