from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import Teacher, University, Department
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def Signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')  
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('Signin')

    return render(request, 'signin.html')



def Home(request):
    return render(request, 'home.html')





from django.shortcuts import render
from .models import Teacher, University, Department
from django.shortcuts import render
from django.db.models import Avg
from .models import Teacher, University, Department, Rating

def filter_teachers(request):
    university_name = request.GET.get('university')  
    department_name = request.GET.get('department')  


    teachers = Teacher.objects.all()

    if university_name:  
        try:
            university = University.objects.get(name=university_name)
            teachers = teachers.filter(university=university)
        except University.DoesNotExist:
            teachers = Teacher.objects.none()  

    if department_name: 
        try:
            department = Department.objects.get(name=department_name)
            teachers = teachers.filter(department=department)
        except Department.DoesNotExist:
            teachers = Teacher.objects.none()  

      
    teachers = teachers.annotate(average_rating=Avg('ratings__rating'))

    
    teachers = teachers.order_by('-average_rating')

    
    universities = University.objects.all()
    departments = Department.objects.all()
    


    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filter_teachers')  

    else:
        form = RatingForm()

    return render(request, 'filter_teachers.html', {
        'teachers': teachers,
        'universities': universities,
        'departments': departments,
        'form': form,  
        'request': request,  
    })


from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Teacher, Rating
from .forms import RatingForm

def teacher_list(request):
    teachers = Teacher.objects.all()  
    teachers = sorted(teachers, key=lambda t: t.get_average_rating(), reverse=True)  
    return render(request, 'teacher_list.html', {'teachers': teachers})


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Teacher, Rating

def rate_teacher(request, teacher_id):
    if request.method == "POST":
        rating_value = int(request.POST.get('rating'))  
        teacher = get_object_or_404(Teacher, id=teacher_id)

        
        Rating.objects.create(teacher=teacher, rating=rating_value)

    
        ratings = teacher.ratings.all()
        avg_rating = sum(r.rating for r in ratings) / ratings.count()

        return JsonResponse({'success': True, 'average_rating': round(avg_rating, 2)})
    return JsonResponse({'success': False, 'error': 'Invalid request'})








from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('Signup')


        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_staff = True  
        user.save()
        
        messages.success(request, 'Admin account created successfully. Please sign in.')
        return redirect('Signin')

    return render(request, 'index.html')
