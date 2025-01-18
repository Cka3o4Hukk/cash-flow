from django.shortcuts import render, redirect, get_object_or_404

from .forms import (TransactionForm, StatusForm, TypeForm, SubcategoryForm,
                    CategoryForm)
from transaction.models import (Transaction, TransactionStatus,
                                TransactionType, Category, Subcategory)

# Главная страница


def index(request):
    transactions = Transaction.objects.all()
    return render(request, 'index.html', {'transactions': transactions})

# Создание транзации


def create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)  # Вывод ошибок формы для отладки
    else:
        form = TransactionForm()

    return render(request, 'create.html', {'form': form})

# Базовые функции


def handle_form(request, form_class, redirect_url):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
        else:
            return render(request, f'{redirect_url}.html', {
                'form': form,
                'error': 'Вы должны выбрать или ввести новый элемент.'
            }, status=400)

    form = form_class()
    items = form_class.Meta.model.objects.all()
    return render(
        request, f'{redirect_url}.html',
        {'form': form, 'items': items})


def update_object_name(request, model, object_id, redirect_url):
    obj = get_object_or_404(model, id=object_id)

    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            obj.name = new_name
            obj.save()
            return redirect(redirect_url)

    return render(request, f'{redirect_url}_edit.html', {'object': obj})


def handle_delete(request, model, object_id, redirect_url):
    obj = get_object_or_404(model, id=object_id)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_url)
    return render(request, f'{redirect_url}_delete.html', {'object': obj})


def mass_delete(request, model, redirect_url):
    if request.method == 'POST':
        ids = request.POST.getlist("ids")
        if ids:
            model.objects.filter(id__in=ids).delete()
    return redirect(redirect_url)


def delete_all(request, model, redirect_url):
    if request.method == 'POST':
        model.objects.all().delete()
        return redirect(redirect_url)

# Статус


def status(request):
    """Создание статуса."""
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status')
        else:
            print(form.errors)

    form = StatusForm()
    statuses = TransactionStatus.objects.all()
    return render(request, 'status.html', {'form': form, 'statuses': statuses})


def status_edit(request, status_id):
    """Редактирование статуса."""
    return update_object_name(request, TransactionStatus, status_id, 'status')


def status_delete(request, pk):
    """Удаление статуса."""
    return handle_delete(request, TransactionStatus, pk, 'status')


def mass_delete_statuses(request):
    """Удаление нескольких статусов."""
    return mass_delete(request, TransactionStatus, 'status')


def delete_all_statuses(request):
    """Удаление всех статусов."""
    return delete_all(request, TransactionStatus, 'status')

# Тип


def type(request):
    """Создание типа."""
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('type')
        else:
            print(form.errors)

    form = TypeForm()
    types = TransactionType.objects.all()
    return render(request, 'type.html', {'form': form, 'types': types})


def type_edit(request, type_id):
    """Редактирование типа."""
    return update_object_name(request, TransactionType, type_id, 'type')


def one_type_delete(request, pk):
    """Удаление типа."""
    return handle_delete(request, TransactionType, pk, 'type')


def mass_delete_types(request):
    """Удаление нескольких типов."""
    return mass_delete(request, TransactionType, 'type')


def delete_all_types(request):
    """Удаление всех статусов."""
    return delete_all(request, TransactionType, 'type')


# Категория


def category_list(request):
    """Список категорий."""
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def add_category(request):
    """Создание категории."""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            return render(request, 'add_category.html', {'form': form})
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


def category_edit(request, type_id):
    """Редактирование категории."""
    category = get_object_or_404(Category, id=type_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'category_edit.html',
                  {'form': form, 'category': category})


def category_delete(request, type_id):
    """Удаление категории."""
    return handle_delete(request, Category, type_id, 'category_list')


def delete_all_categories(request):
    """Удаление всех категорий."""
    return delete_all(request, Category, 'category_list')

# Подкатегория


def subcategory_list(request):
    """Список подкатегорий."""
    categories = Category.objects.prefetch_related('subcategories').all()
    return render(request, 'subcategory_list.html', {'categories': categories})


def add_subcategory(request):
    """Создание подкатегории."""
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
        else:
            return render(request, 'add_subcategory.html', {'form': form})
    else:
        form = SubcategoryForm()
    return render(request, 'add_subcategory.html', {'form': form})


def subcategory_edit(request, subcategory_id):
    """Редактирование подкатегории."""
    subcategory = get_object_or_404(Subcategory, id=subcategory_id)

    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubcategoryForm(instance=subcategory)

    return render(request, 'subcategory_edit.html', {
        'form': form,
        'subcategory': subcategory,
        'category': subcategory.category
    })


def subcategory_delete(request, subcategory_id):
    """Удаление подкатегории."""
    return handle_delete(request, Subcategory, subcategory_id,
                         'subcategory_list')
