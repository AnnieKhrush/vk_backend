from django.shortcuts import render

# Create your views here.
def page(request):
    if request.method == 'GET':
        return render(request, 'start_page_users.html')
    else:
        return HttpResponse(status=405)