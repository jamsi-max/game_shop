from django import forms

from mainapp.models import News


class AdminNewsAddForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('news_tite', 'news_content')

    def __init__(self, *args, **kwars):
        super(AdminNewsAddForm, self).__init__(*args, **kwars)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-item-news-add'


    
  

