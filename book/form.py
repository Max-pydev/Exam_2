from django import forms



class EventForm(forms.Form):

    full_name = Forms.CharField(max_length(50))
    email = Forms.EmailField(max_length(30))
    user_name = Forms.CharField(max_length(20))
    comment = Forms.CharField(max_length(100))
    phone_number = Forms.CharField(max_length(15))
    created_at = Forms.DateTimeField(auto_now_add=True)
    update_at=Forms.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.full_name
    
