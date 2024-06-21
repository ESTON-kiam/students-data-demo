import matplotlib.pyplot as plt
import io
import urllib
import base64
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student


def index(request):
    data = Student.objects.all()

    male_count = data.filter(gender='Male').count()
    female_count = data.filter(gender='Female').count()

    plt.figure(figsize=(10, 6))
    plt.bar(['Male', 'Female'], [male_count, female_count], color=['blue', 'pink'])
    plt.title('Number of Male and Female Students')
    plt.xlabel('Gender')
    plt.ylabel('Count')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode('utf-8')  # Ensure decoding to string
    uri = urllib.parse.quote(string)

    context = {"data": data, "chart": uri}
    return render(request, "index.html", context)


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()

        messages.info(request, "Data Inserted Successfully")
        return redirect("/")

    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        # Update operation: Update existing student data
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']

        edit = Student.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.gender = gender
        edit.age = age
        edit.save()

        messages.warning(request, "Data Updated Successfully")
        return redirect("/")

    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)


def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()

    messages.error(request, "Data deleted Successfully")
    return redirect("/")


def about(request):
    return render(request, "about.html")
