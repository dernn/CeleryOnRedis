# for django shell
from mc_donalds.models import User

User.objects.create(name='Dmitry', profile_data={
    'country': 'Russia',
    'children': [
        {
            'name': 'John',
        },
    ],
    'phone_operator': 'MTS'
})

# <User: Dmitry>
User.objects.create(name='Megan Fox', profile_data={
    'country': 'UK',
    'children': None
})
# <User: Megan Fox>
User.objects.filter(profile_data__country='UK')
# <QuerySet [<User: Megan Fox>]>

# __contains [@>] для точной проверки наличия пар «ключ-значение»
User.objects.filter(profile_data__contains={'country': 'UK'})  # найти всех пользователей из Великобритании

# __contained_by проверка полного вхождения profile_data в массив __contained_by
User.objects.filter(profile_data__contained_by={'country': 'UK', 'children': None})
