from django.shortcuts import render, get_object_or_404
from .models import Program

def landing(request):
    # Get featured programs for the landing page
    featured_programs = Program.objects.all()[:6]  # Show 6 featured programs
    return render(request, 'programs/landing.html', {'featured_programs': featured_programs})

def program_list(request):
    programs = Program.objects.all()
    return render(request, 'programs/program_list.html', {'programs': programs})

def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'programs/program_detail.html', {'program': program})