from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def imageUpload(request):
    '''Docstring here.'''
    file = request.FILES['image']
    file_system = FileSystemStorage()
    file_name = str(file).split('.')[0]
    file_object = file_system.save(file_name, file)
    file_url = file_system.url(file_object)

    return JsonResponse(
      {
        'success': 1,
        'file': {
          'url': file_url
        }
      }
    )

@csrf_exempt
def fileUpload(request):
    file = request.FILES['file']
    file_system = FileSystemStorage()
    file_name, ext = str(file).split('.')[0]

    file_object = file_system.save(file_name, file)
    file_url = file_system.url(file_object)

    return JsonResponse(
      {
        'success': 1,
        'file': {
          'url': file_url,
          'size': file_system.size(file_name),
          'name': str(file),
          'extension': ext
        }
      }
    )