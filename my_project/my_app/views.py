from django.shortcuts import render
from my_app.forms import userForm,userProfileInfoForm
# Create your views here.
def index(request):
    return render (request,'index.html')

def login(request):
    return render (request,'login.html')

def register(request):
    form_1=userForm()
    form_2=userProfileInfoForm()
    
    registered=False
    if request.method=='POST':
        form_1_resp=userForm(request.POST)
        form_2_resp=userProfileInfoForm(request.POST)

        if form_1_resp.is_valid() and form_2_resp.is_valid():
            f=form_1_resp.save()
            f.set_password(f.password)
            f.save()

            p=form_2_resp.save(commit=False)
            p.user=f
            if 'profile_pic' in request.FILES:
                p.profile_pic=request.FILES['profile_pic']
            else:
                print('pic nnnnaaaaiiiii   !!!!')
            p.save()

            registered=True
        else:
            print(form_1.errors, form_2.errors)
    else:
        pass
        
    
    context_dict={'f1':form_1,'f2':form_2,'registered':registered}
    return render (request,'register.html',context_dict)
    