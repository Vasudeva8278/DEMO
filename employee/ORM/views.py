from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reg_Employee,Photo
from .serializers import EmployeeSerializer,EmployeeUpdateSerializer,PhotoSerializer
from django.db.utils import OperationalError
from .forms import EmployeeForm
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action

# create employee api view function
@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# create employee from html page basic level 

def homepage(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except OperationalError as e:
                # Handle the exception, perhaps by redirecting to an error page
                return render(request, 'error.html', {'error_message': str(e)})
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})




 
# total employee data get function

@api_view(['GET'])
def get_data(request):
    try:
        queryset = Reg_Employee.objects.all()  # Replace YourModel with your actual model name
        serializer = EmployeeSerializer(queryset, many=True)  # Replace YourModelSerializer with your actual serializer
        return Response(serializer.data)
    except Exception as e:
        # Handle the exception, e.g., log it or return an error response
        error_message = str(e)  # Convert the exception to a string for display
        return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        
        
 

# delete employee data class
class DeleteAPIView(APIView):
    def delete(self, request, id):
        try:
            # Retrieve the object from the database
            obj = Reg_Employee.objects.get(id=id)
            
            # Delete the object
            obj.delete()
            
            # Return success response
            return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        except Reg_Employee.DoesNotExist:
            # Handle the case where the object does not exist
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            # Handle other exceptions
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
 
# update class methods 
class UpdateAPIView(APIView):
    def put(self, request, id):
        try:
            # Retrieve the object from the database
            employee = Reg_Employee.objects.get(id=id)
            
            # Serialize the object with the updated data
            serializer = EmployeeUpdateSerializer(employee, data=request.data, partial=True)  # Use partial=True to allow partial updates
            
            # Validate and save the updated data
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Reg_Employee.DoesNotExist:
            # Handle the case where the object does not exist
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            # Handle other exceptions
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class UploadPhotoView(APIView):
    def post(self, request, format=None):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)