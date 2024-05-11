from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reg_Employee
from .serializers import EmployeeSerializer
from django.db.utils import OperationalError
from .forms import EmployeeForm
from rest_framework.views import APIView
@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




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
    

class UpdateAPIView(APIView):
    def get(self, request, id):
        try:
            # Retrieve the object from the database
            obj = Reg_Employee.objects.get(id=id)
            
            # Serialize the object
            serializer = EmployeeSerializer(obj)
            
            # Return the serialized data
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Reg_Employee.DoesNotExist:
            # Handle the case where the object does not exist
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            # Handle other exceptions
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
        
# Define your view function
def employee_data_page(request):
    return render(request, 'getdata.html')