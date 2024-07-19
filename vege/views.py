from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def recipe(request):
    if request.method=="POST":
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_descrip=data.get('recipe_descrip')
        recipe_image=request.FILES.get('recipe_image')
        # print(recipe_name)
        # print(recipe_descrip)
        # print(recipe_image)
        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_descrip
        )
        return redirect("/recipe")
    queryset=Recipe.objects.all()

    if request.GET.get('search'):
        # yaha prr humne jo humare input field ka name tha waha se get krra
        queryset=queryset.filter(recipe_name__icontains=request.GET.get('search'))
        # __icontains m kya woh string aati h ya ni jitni bhij substring m woh search word hoga
    context={"recipes":queryset}
    return render(request,"recipe.html",context)

def delete_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect("/recipe")

def update_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_descrip=data.get('recipe_descrip')
        recipe_image=request.FILES.get('recipe_image')
        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_descrip
        if recipe_image:
            queryset.recipe_image=recipe_image
        queryset.save()
        return redirect("/recipe")
    context={'recipes':queryset}
    return render(request,"update_recipe.html",context)

