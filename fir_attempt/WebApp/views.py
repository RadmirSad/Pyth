from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from WebApp.models import Teacher, Web, Course, Cost
from WebApp.serializers import TeacherSerializer, WebSerializer, CourseSerializer, CostSerializer

# Create your views here.


@csrf_exempt
def teach_api(request, my_id=0):                        # func for managing teacher information
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        teacher_serial = TeacherSerializer(teachers, many=True)
        return JsonResponse(teacher_serial.data, safe=False)
    elif request.method == 'POST':
        teacher_data = JSONParser().parse(request)
        teacher_serial = TeacherSerializer(data=teacher_data)
        if teacher_serial.is_valid():
            teacher_serial.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        teacher_data = JSONParser().parse(request)
        teacher = Teacher.objects.get(id=teacher_data['id'])
        teacher_serial = TeacherSerializer(teacher, data=teacher_data)
        if teacher_serial.is_valid():
            teacher_serial.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        teacher = Teacher.objects.get(id=my_id)
        teacher.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def web_api(request, my_id=0):                          # func for managing webinar information
    if request.method == 'GET':
        webs = Web.objects.all()
        web_serial = WebSerializer(webs, many=True)
        return JsonResponse(web_serial.data, safe=False)
    elif request.method == 'POST':
        web_data = JSONParser().parse(request)
        web_serial = WebSerializer(data=web_data)
        if web_serial.is_valid():
            web_serial.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        web_data = JSONParser().parse(request)
        web = Web.objects.get(id=web_data['id'])
        web_serial = WebSerializer(web, data=web_data)
        if web_serial.is_valid():
            web_serial.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        web = Web.objects.get(id=my_id)
        web.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def course_api(request, my_id=0):                       # func for managing course information
    if request.method == 'GET':
        courses = Course.objects.all()
        course_serial = CourseSerializer(courses, many=True)
        return JsonResponse(course_serial.data, safe=False)
    elif request.method == 'POST':
        course_data = JSONParser().parse(request)
        course_serial = CourseSerializer(data=course_data)
        if course_serial.is_valid():
            course_serial.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        course_data = JSONParser().parse(request)
        course = Course.objects.get(id=course_data['id'])
        course_serial = CourseSerializer(course, data=course_data)
        if course_serial.is_valid():
            course_serial.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        course = Course.objects.get(id=my_id)
        course.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def cost_api(request, my_id=0):                         # func for managing information about earnings per hour
    if request.method == 'GET':
        costs = Cost.objects.all()
        cost_serial = CostSerializer(costs, many=True)
        return JsonResponse(cost_serial.data, safe=False)
    elif request.method == 'POST':
        cost_data = JSONParser().parse(request)
        cost_serial = CostSerializer(data=cost_data)
        if cost_serial.is_valid():
            cost_serial.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        cost_data = JSONParser().parse(request)
        cost = Cost.objects.get(id=cost_data['id'])
        cost_serial = CostSerializer(cost, data=cost_data)
        if cost_serial.is_valid():
            cost_serial.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        cost = Cost.objects.get(id=my_id)
        cost.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def get_salary_api(request):                            # func for getting information on teachers' salaries
    if request.method == 'GET':
        teachers = Teacher.objects.all()                # get all objects
        courses = Course.objects.all()
        costs = Cost.objects.all()
        salaries = {}
        for teacher in teachers:                        # create dict with names of the teachers and their salaries
            salaries.update({teacher.FullName: 0})
        for course in courses:                          # check all courses and all relevant webinars
            webs = course.Webinars.all()
            for web in webs:
                this_teachers = web.Teachers.all()      # in webinars check teachers who lead this webinar
                for this in this_teachers:              # find their find their working rate per hour
                    cost = costs.get(Course_ID=course, Teach_ID=this)   # add to their wages
                    sal = salaries.pop(this.FullName)
                    sal += cost.CostInHour
                    salaries.update({this.FullName: sal})
        return JsonResponse(salaries, safe=False)
    return JsonResponse("This method is not supported", safe=False)

