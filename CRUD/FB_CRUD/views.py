from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import User
from django.http import HttpResponseRedirect
# Create your views here.

def add_show(request):
    #GET METHOD surumai localhost:8000 auni bela load huni part 
    form = UserRegistrationForm()

    #Submit button click garda matrai POST Method ko kam huncha
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) # Method POST aundaa Form Show hoss vanera ho and request.post leh data laucha .

        if form.is_valid():
            #Form bata clean data garnu ko meaning input field ma type gareko value haru dekhauna ho.
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            register = User(name=name, email=email, password=password) #3 wotai clean data ko field lai save garna ko lagi 
            register.save()
            form = UserRegistrationForm() # submit button click garisakey pachi teta lekheko kura hatos and feri new field haru dekhawos vanera rakheko ho
            # return render(request, 'FB_CRUD/add_show.html')

    studentshow = User.objects.all()       
    context = {'form':form, 'studentshow':studentshow} # yo form => Line 9 ko form ho
    return render(request,'FB_CRUD/add_show.html', context)



# fro delete

def delete(request,id):
    if request.method == 'POST':
        del_record = User.objects.get(pk=id) # Specific id ko record ayera baseko huncha.
        del_record.delete()
    return HttpResponseRedirect('/')    #page refresh after delete

def edit(request, id):
    if request.method == 'POST':
        edit_record = User.objects.get(pk=id) # yesma id aayerako huncha edit button click garda 
        form = UserRegistrationForm(request.POST, instance=edit_record) # tei id ma edit gareko kura update huna parni vayeko le yo instance =edit_record banayeko ho. 
        if form.is_valid:
            form.save()         # edited form lai save gareko.
        return HttpResponseRedirect('/')    #submit click garisakey pachi page reload gareko ho.

    else:
        edit_record = User.objects.get(pk=id) #edit_record ma particular edit button click garda id ayerako huncha
        form = UserRegistrationForm(instance=edit_record) # form ma edit garda form ko field ma edit garna ko lagi previsous value haru show garirakhna ko lagi ho
         
    return render (request, 'FB_CRUD/edit.html', {'form':form} )
        
