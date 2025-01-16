from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from rest_framework import serializers
#from djoser.serializers import (
#    UserCreateSerializer as DjoserUserCreateSerializer)
#from djoser.serializers import UserSerializer as DjoserUserSerializer

#from recipes.models import Follow, Ingredient, Recipe, RecipeIngredients, Tag
#from .validators import validate_ingredients, validate_tags
from transaction.models import Transaction

User = get_user_model()

class TransactionSerializer(serializers.ModelSerializer):
    """Создание пользователя."""



    class Meta:
        model = Transaction
        fields = '__all__'

