from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Meal Planner."""
    return render(request, 'ml_plan/index.html')
