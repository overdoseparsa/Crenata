from django import forms



class EmailForms(forms.Form):
    # this is the simple field for porgrammers 
    name = forms.CharField(
        max_length=320
    )
    Email = forms.EmailField()
    send_to  = forms.EmailField()
    comments = forms.CharField(
    required=False,
    widget=forms.Textarea
    )