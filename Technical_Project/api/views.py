from rest_framework import status
from .models import Task

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer 
# Create your views here.

# GET all the tasks in the database
@api_view(['GET'])
def tasklist(request):
    # Query the database for all the tasks to show
    tasks = Task.objects.all()
    
    #Check if there are tasks in the database
    if len(tasks) == 0:
        return Response({'Message':'There are no tasks available'},status=status.HTTP_204_NO_CONTENT)
    
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data,status=status.HTTP_200_OK)

# GET a specific task by id
@api_view(['GET'])
def taskdetail(request,id):
        # Try to query the database for the task and raise error if it does not exist
        try: 
            task = Task.objects.get(id = id) 
        except Task.DoesNotExist: 
            return Response({'message': 'This task does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
        serializer = TaskSerializer(task, many = False)
        return Response(serializer.data,status=status.HTTP_200_OK)

        
# Create a new Task    
@api_view(['POST'])
def taskcreate(request):
    
    # Serialize the user inout
    serializer = TaskSerializer(data = request.data)
    # Check for validation, save if valid and return failuer message id not. 
    if serializer.is_valid():
        serializer.save()
    else:
         return Response({'Message':"Something went wrong"}, status=status.HTTP_406_NOT_ACCEPTABLE)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

# Edit a task    
@api_view(['PUT'])
def taskupdate(request, id):
    
    # Query the database for the task 
    task = Task.objects.filter(id = id).first()
    # Serialize The user input 
    serializer = TaskSerializer(instance= task,data = request.data)

    # Check for validation 
    if serializer.is_valid():

        updated_task = serializer.validated_data
        
        # Check the state of the task before saving to meet the task state machine
        if task.state == 'archived':
            return Response({'Message':"This task was archived and can't go backward in state."},
             status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        elif task.state == 'draft':
            
            if updated_task['state'] in ['active', 'archived']:
                serializer.save()
            else:
                return Response({'Message':"Task can't move from draft directly to done."},
                 status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        elif task.state == 'active':
            
            if updated_task['state'] in ['done','archived']:
                serializer.save()
            else:
                return Response({'Message':"Task can't move from active back to done."},
                 status=status.HTTP_405_METHOD_NOT_ALLOWED)                
        
        else:
            if updated_task['state'] != 'archived':
                return Response({'Message':"Task can't move from done backward."},
                 status=status.HTTP_405_METHOD_NOT_ALLOWED)
            else:
                serializer.save()
    
    else:
        return Response({'Message':"status is not recognized"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return Response(serializer.data,status=status.HTTP_200_OK)


# DELETE a task    
@api_view(['DELETE'])
def taskdelete(request, id):
   
   # Query the database for task to be deleted    
    task = Task.objects.filter(id = id)

    # Delete the task
    task.delete()

    return Response("'Message':Item successfully deleted", status=status.HTTP_200_OK)