from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def hello(request):
    return HttpResponse('Hello!')

def dish(request, dish):
    context = {}
    servings = int(request.GET.get("servings", 1))
    print(f'Переданный в запросе {servings=}')
    if servings > 1:
        for k, v in DATA[dish].items():
            DATA[dish][k] = v * servings
    context = {'recipe': DATA[dish], 'dish': dish}
    return render(request, 'calculator/index.html', context)
    # return HttpResponse(f'{DATA[dish]}')

