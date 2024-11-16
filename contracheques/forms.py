from django import forms
from .models import ContraCheque

class ContraChequeForm(forms.ModelForm):
    class Meta:
        model = ContraCheque
        fields = [
            # 'usuario',
            'nome_funcionario',
            'data_criacao',
            'conta',
            'agencia',
            'arquivo',
            'ano'
        ]
        widgets = {
            'nome_funcionario': forms.TextInput(attrs={'class': 'form-control'}),
            'data_criacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'conta': forms.TextInput(attrs={'class': 'form-control'}),
            'agencia': forms.TextInput(attrs={'class': 'form-control'}),
            'arquivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
        }