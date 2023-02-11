from django.shortcuts import render,reverse
from django.views import generic
from .forms import *
from django.contrib.auth.models import User
from django.views.generic import FormView



class CreateEmployeeFormView(generic.CreateView):
    template_name = "company/employee_registration.html"
    form_class = EmployeeModelForm

    def get_success_url(self):
        return reverse("register:list-employee")
    


class  EmployeeListView(generic.ListView):
    template_name = "company/employee_list.html"
    queryset = Employee.objects.all()
    context_object_name = "employees"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_employees'] = self.queryset.count()
        return context


class EmployeeDetailView(generic.DetailView):
    template_name = "company/employee_detail.html"
    queryset = Employee.objects.all()
    context_object_name = "employee"


class EmployeeUpdateView(generic.UpdateView):
    template_name = "company/employee_update.html"
    form_class = EmployeeModelForm
    queryset = Employee.objects.all()

    def get_success_url(self):
        return reverse("register:list-employee")
    

class EmployeeDeleteView(generic.DeleteView):
    template_name = "company/employee_delete.html"
    queryset = Employee.objects.all()

    def get_success_url(self):
        return reverse("register:list-employee")
    

class RegistrationView(FormView):
    template_name = 'company/register.html'
    form_class = RegistrationForm
    
    def get_success_url(self):
        return reverse('register:list-employee')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        if User.objects.filter(username=username).exists():
            form.add_error('username', 'Username is already taken')
            return self.form_invalid(form)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return super().form_valid(form)





    







