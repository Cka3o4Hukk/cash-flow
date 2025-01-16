from django import forms
from transaction.models import Transaction, TransactionType, Category, Subcategory, TransactionStatus

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'status', 'transaction_type', 'category', 'subcategory', 'comment']
    
    # Поле для выбора статуса
    status = forms.ModelChoiceField(
        queryset=TransactionStatus.objects.all(),
        empty_label="Выберите статус",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Поле для выбора типа операции
    transaction_type = forms.ModelChoiceField(
        queryset=TransactionType.objects.all(),
        empty_label="Выберите тип операции",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Поле для выбора категории
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Выберите категорию",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Поле для выбора подкатегории
    subcategory = forms.ModelChoiceField(
        queryset=Subcategory.objects.all(),
        empty_label="Выберите подкатегорию",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class StatusForm(forms.ModelForm):
    predefined_status = forms.ChoiceField(
        choices=[('', 'Выберите статус'), ('Бизнес', 'Бизнес'), ('Личное', 'Личное'), ('Налог', 'Налог')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Выберите из существующих" 
    )
    new_status = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Или введите новый статус'
            }
        ),
        label="Добавить новый статус"
    )

    class Meta:
        model = TransactionStatus
        fields = []

    def clean(self):
        cleaned_data = super().clean()
        predefined_status = cleaned_data.get('predefined_status')
        new_status = cleaned_data.get('new_status')

        if not predefined_status and not new_status:
            raise forms.ValidationError("Вы должны выбрать статус или ввести новый.")

        if predefined_status:
            cleaned_data['name'] = predefined_status
        else:
            cleaned_data['name'] = new_status

        return cleaned_data

    def save(self, commit=True):
        name = self.cleaned_data.get('name')
        if commit:
            return TransactionStatus.objects.create(name=name)


class TypeForm(forms.ModelForm):
    predefined_status = forms.ChoiceField(
        choices=[('', 'Выберите тип'), ('Пополнение', 'Пополнение'), ('Списание', 'Списание')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Выберите из существующих" 
    )
    new_status = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Или введите новый тип'
            }
        ),
        label="Добавить новый тип"
    )

    class Meta:
        model = TransactionType
        fields = []

    def clean(self):
        cleaned_data = super().clean()
        predefined_type = cleaned_data.get('predefined_status')  # исправлено на 'predefined_status'
        new_type = cleaned_data.get('new_status')  # исправлено на 'new_status'

        if not predefined_type and not new_type:  # проверка переменных
            raise forms.ValidationError("Вы должны выбрать тип или ввести новый.")

        if predefined_type:
            cleaned_data['name'] = predefined_type
        else:
            cleaned_data['name'] = new_type

        return cleaned_data

    def save(self, commit=True):
        name = self.cleaned_data.get('name')
        if commit:
            return TransactionType.objects.create(name=name)
    