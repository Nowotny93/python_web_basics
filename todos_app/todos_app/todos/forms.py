from django import forms
from django.core.exceptions import ValidationError

from todos_app.todos.models import Todo


def validate_dot(value):
    if '.' in value:
        raise forms.ValidationError('\'.\' is present in value')


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        #fields = ['title', 'description']
        #exclude = ['description']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                },
            ),
            'owner': forms.RadioSelect()
        }

    def clean(self):
        owner = self.cleaned_data['owner']
        if owner.todo_set.count() > 2:
            raise ValidationError(f'{owner.name} cannot have more than 2 todos')
    # def clean_title(self):
    #     validate_dot(self.cleaned_data['title'])


class CreateTodoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        validators=[
            #validate_dot,
        ],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter todo text',
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'my-text-area',
                'rows': 3,
            }
        )
    )

    bot_catcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
    )

    def clean_bot_catcher(self):
        if len(self.cleaned_data['bot_catcher']):
            raise forms.ValidationError('This is a bot')


class UpdateTodoForm(CreateTodoForm):
    state = forms.BooleanField()
