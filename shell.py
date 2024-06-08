from barbearias.models import Cliente
from django.contrib.auth.models import User

users = User.objects.all()
for user in users:
    cliente = Cliente.objects.create(
        cliente=user,
    )
    print('usuario criado')