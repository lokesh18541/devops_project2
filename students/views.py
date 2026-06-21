from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student

@csrf_exempt
def student_list_create(request):
    if request.method == 'GET':
        students = list(Student.objects.values('id', 'name'))
        return JsonResponse(students, safe=False)
        
    elif request.method == 'POST':
        data = json.loads(request.body)
        if 'name' in data:
            student = Student.objects.create(name=data['name'])
            return JsonResponse({'id': student.id, 'name': student.name}, status=201)
        return JsonResponse({'error': 'Name field is required'}, status=400)