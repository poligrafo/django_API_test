from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tasks.models import New_task
from tasks.serializers import NewTaskSerializer


class TaskListCreateView(APIView):
    def get(self, request):
        status_param = request.query_params.get('status', None)

        if status_param:
            if status_param.lower() == 'completed':
                tasks = New_task.objects.filter(completed=True)
            elif status_param.lower() == 'notcompleted':
                tasks = New_task.objects.filter(completed=False)
            else:
                return Response({'error': 'Invalid status parameter'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            tasks = New_task.objects.all()

        serializer = NewTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        try:
            task = New_task.objects.get(pk=pk)
        except New_task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = NewTaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            task = New_task.objects.get(pk=pk)
        except New_task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = NewTaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            task = New_task.objects.get(pk=pk)
        except New_task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



