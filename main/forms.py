from django import forms
from .models import Option

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop('quiz', None)
        super().__init__(*args, **kwargs)
        if quiz:
            for question in quiz.questions.all():
                options = [(option.id, option.name) for option in question.options.all()]
                self.fields[f'question_{question.id}'] = forms.ChoiceField(
                    choices=options,
                    widget=forms.RadioSelect,
                    label=question.name
                )
