from django import forms
from valve_nodes.models import ValveNode, MeterDevice


class ValveNodeForm(forms.ModelForm):

    class Meta:
        model = ValveNode
        fields = ['title', 'locate', 'node_state', 'visit_date',
                  'visit_master', 'note', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'locate': forms.TextInput(attrs={'class': 'form-control'}),
            'node_state': forms.Select(attrs={'class': 'form-control'}),
            'visit_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'visit_master': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }



'''
class MeterDeviceForm(forms.Form):
    title = forms.CharField(max_length=80, db_index=True)
    device_type = forms.CharField(max_length=80, blank=True, help_text='Тип СИ')
    state = forms.CharField(max_length=50, blank=True, help_text='состояние, уст, хранение, ремонт, утиль')
    place = forms.CharField(max_length=50, blank=True, help_text='Место нахождения')
    # tags = forms.ManyToManyField('Tag', blank=True, related_name='meter_devices')
    tag_name = forms.CharField(max_length=100, blank=True, help_text='Содержимое бирки')
    tag_check = forms.BooleanField(help_text='Бирка установлена')
    number_factory = forms.CharField(max_length=20, blank=True, help_text='Заводской номер')
    model = forms.CharField(max_length=50, blank=True, help_text='Модель')
    meter_limit = forms.CharField(max_length=50, blank=True, help_text='Предел измерений')
    accuracy = forms.CharField(max_length=10, blank=True, help_text='Класс точности')
    date_make = forms.DateField(blank=True, null=True)
    date_verify_mark = forms.DateField(blank=True, null=True)
    date_install = forms.DateField(blank=True, null=True)
    date_uninstall = forms.DateField(blank=True, null=True)
'''