from django.shortcuts import render

def report_view(request):
    return render(request, 'polls/report.html')

    