from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse

from .forms import TransactionForm, StatusForm, TypeForm
from transaction.models import Transaction, TransactionStatus, TransactionType


def index(request):
    transactions = Transaction.objects.all()
    return render(request, 'index.html', {'transactions': transactions})


def create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Перенаправление на список транзакций
    else:
        form = TransactionForm()

    return render(request, 'create.html', {'form': form})


def status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статус успешно добавлен.')
            return redirect('status')
        else:
            return render(request, 'status.html', {
                'form': form,
                'statuses': TransactionStatus.objects.all(),
                'error': 'Вы должны выбрать статус или ввести новый.'
            }, status=400)

    form = StatusForm()
    statuses = TransactionStatus.objects.all()
    return render(request, 'status.html', {'form': form, 'statuses': statuses})


def status_edit(request, status_id):
    status = get_object_or_404(TransactionStatus, id=status_id)

    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            status.name = new_name
            status.save()
        return redirect('status')

    return render(request, 'status-edit.html', {'status': status})


def status_delete(request, pk):
    if request.method == 'POST':
        status = get_object_or_404(TransactionStatus, pk=pk)
        status.delete()
    return redirect('status')


def mass_delete_statuses(request):
    if request.method == 'POST':
        status_ids = request.POST.getlist("status_ids")
        if status_ids:
            TransactionStatus.objects.filter(id__in=status_ids).delete()
            messages.success(request, "Выбранные статусы успешно удалены.")
        else:
            messages.warning(request, "Вы не выбрали ни одного статуса для удаления.")
        return redirect('status')

    return HttpResponse("Ошибка: неправильный запрос.")


def delete_all_statuses(request):
    if request.method == 'POST':
        TransactionStatus.objects.all().delete()
        return redirect('status')


def type(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'type.html', {
                'form': form,
                'types': TransactionType.objects.all(),
            })
        else:
            return render(request, 'type.html', {
                'form': form,
                'types': TransactionType.objects.all(),
                'error': 'Вы должны выбрать тип или ввести новый.'
            }, status=400)
    
    form = TypeForm()
    types = TransactionType.objects.all()
    return render(request, 'type.html', {'form': form, 'types': types})


def type_edit(request, type_id):
    type = get_object_or_404(TransactionType, id=type_id)

    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            type.name = new_name
            type.save()
        return redirect('type')

    return render(request, 'type-edit.html', {'type': type})


def one_type_delete(request, pk):
    if request.method == 'POST':
        type = get_object_or_404(TransactionType, pk=pk)
        type.delete()
    return redirect('type')


def mass_delete_types(request):
    if request.method == 'POST':
        type_ids = request.POST.getlist("type_ids")
        if type_ids:
            TransactionType.objects.filter(id__in=type_ids).delete()
            messages.success(request, "Выбранные типы успешно удалены.")
        else:
            messages.warning(request, "Вы не выбрали ни одного типа для удаления.")
    return redirect('type')


def delete_all_types(request):
    if request.method == 'POST':
        TransactionType.objects.all().delete()
        return redirect('type')
