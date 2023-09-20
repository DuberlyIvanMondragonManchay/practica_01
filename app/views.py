from django.shortcuts import render,redirect,get_object_or_404
from .models import Food
from .forms import FoodForm
# Create your views here.
def get_foods_view(request):
    foods = Food.objects.all()
    return render(request, 'index_food.html',{'foods':foods,'len':len(foods)})

def create_food_view(request):
    if request.method == 'GET':
        return render(request, 'create_food.html',{'food_form':FoodForm})
    else:
        print(request.POST)
        try:
            form = FoodForm(request.POST)
            form.save(commit=True)

            return redirect('foods')
        except ValueError:
            return render(request, 'create_food.html', {"food_form": FoodForm, "error": "Error creating Food."})
        

def delete_food_view(request,food_id):
    food = get_object_or_404(Food, pk=food_id)

    if request.method == 'GET':
        food.delete()
        return redirect('foods')
    return redirect('foods')


def update_food_view(request,food_id):
    if request.method == 'GET':
        food = get_object_or_404(Food, pk=food_id)
        food_form = FoodForm(instance=food)
        return render(request, 'update_food.html', {'food': food,'food_form':food_form})
    
    try:
        food = get_object_or_404(Food, pk=food_id)
        form = FoodForm(request.POST, instance=food)
        form.save()
        return redirect('foods')
    except ValueError:
        return render(request, 'update_food.html', {'food': food,'food_form':food_form})

