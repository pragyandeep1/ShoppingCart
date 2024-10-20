from django.shortcuts import render
from testapp.forms import AddItemForm

# Create your views here.
def index_view(request):
    return render(request,'testapp/home.html')

def add_item_view(request):
    form = AddItemForm() # empty form
    response = render(request,'testapp/addItem.html',{'form':form})
    if request.method == 'POST':
        form = AddItemForm(request.POST) # end-user provided data
        if form.is_valid():
            name = form.cleaned_data['itemName']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name,quantity)
    return response

def display_items_view(request):
    return render(request,'testapp/displayItems.html')