from django.shortcuts import render

# Create your views here.
class ViewByClass(TemplateView):
    template_name = 'second_task/class_template.html'

def func_view(request):
    return render(request, 'second_task/func_template.html')
