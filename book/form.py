from django import forms, TodoModel


class TodoModel(mode.Model):


    coment =models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = model.DateTimeField(auto_now=True)

    def __str__(self):
        retun f"{self.coment} {self.last_name}"

    class Meta:
        


