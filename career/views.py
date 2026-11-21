
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from .models import Student


def home(request):
    return render(request, 'home.html')


def register(request):

    error = ""

    if request.method == "POST":

        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        education = request.POST.get('education')
        skills = request.POST.get('skills')

        if password != confirm_password:
            error = "Passwords do not match!"

        elif Student.objects.filter(email=email).exists():
            error = "Email already registered!"

        else:
            Student.objects.create(
                full_name=full_name,
                email=email,
                password=make_password(password),
                education=education,
                skills=skills
            )

            return render(request, 'register.html', {
                'success': 'Registration Successful!'
            })

    return render(request, 'register.html', {
        'error': error
    })
def login_user(request):
    error = ""

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        try:
            student = Student.objects.get(email=email)

            if check_password(password, student.password):
                request.session['student_id'] = student.id
                return redirect('dashboard')
            else:
                error = "Incorrect Password!"

        except Student.DoesNotExist:
            error = "Email not registered!"

    return render(request, 'login.html', {
        'error': error
    })
def dashboard(request):
    student_id = request.session.get('student_id')

    if not student_id:
        return redirect('login')

    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return redirect('login')

    return render(request, 'dashboard.html', {
        'student': student
    })


def logout_user(request):
    request.session.flush()
    return redirect('login')

def skill_analysis(request):

    if 'student_id' not in request.session:
        return redirect('login')

    student = Student.objects.get(
        id=request.session['student_id']
    )

    user_skills = [
        skill.strip().lower()
        for skill in student.skills.split(',')
        if skill.strip()
    ]

    required_skills = [
        'python',
        'django',
        'html',
        'css',
        'javascript',
        'sql',
        'git'
    ]

    matched_skills = [
        skill for skill in required_skills
        if skill in user_skills
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in user_skills
    ]

    percentage = int(
        len(matched_skills) / len(required_skills) * 100
    )

    return render(request, 'skill_analysis.html', {
        'student': student,
        'matched_skills': matched_skills,
        'missing_skills': missing_skills,
        'percentage': percentage
    })

def career_roadmap(request):
    student_id = request.session.get('student_id')

    if not student_id:
        return redirect('login')

    student = Student.objects.filter(id=student_id).first()

    if not student:
        return redirect('login')

    return render(request, 'roadmap.html', {
        'student': student
    })




