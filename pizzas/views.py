from django.shortcuts import get_object_or_404, render, redirect
from .models import Pizza, Topping, Comment
from .forms import CommentForm



def home(request):
    return render(request, 'home.html')


def pizzas(request):
    pizzas = Pizza.objects.all()
    return render(request, "pizzas.html", {"pizzas": pizzas})

def pizza(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    toppings = Topping.objects.filter(pizza=pizza)
    comments = pizza.comment_set.all()
    context = {
        "pizza": pizza,
        "toppings": toppings,
        "comments": comments,
    }
    return render(request, "pizza.html", context)

def comment_form(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pizza = pizza
            comment.save()
            return redirect("pizza", pizza_id=pizza.id)
    else:
        form = CommentForm()
    return render(request, "comment_form.html", {"pizza": pizza, "form": form})