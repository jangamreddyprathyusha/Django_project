from django.shortcuts import render,redirect

# Create your views here.
from hr_department.form import employee_form

def new_employee(request):
    form=employee_form()
    if request.method=='POST':
        form=employee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'hr_tem/emp_form.html',{'form':form})