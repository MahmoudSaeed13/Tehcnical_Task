from django.urls import reverse, path, include
from rest_framework import response, status
from rest_framework.test import APITestCase
from .models import Task
from django.test import Client
from django.db.models import Max
# create your tests here.

class TaskTest(APITestCase):
    

    def setUp(self):
        # create tasks
        Task.objects.create(id = 1, title = 'Task1', state = 'draft')
        Task.objects.create(id = 2, title = 'Task2', state = 'active')
        Task.objects.create(id = 3, title = 'Task3', state = 'done')
        Task.objects.create(id = 4, title = 'Task4', state = 'archived')
    
    
    # Test the tasklist view which shows all tasks
    def test_valid_get_tasks(self):
        
        url = reverse('task-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 4)

    # Test the detail view which retrive a specific task bby id 
    def test_valid_detail_task(self):
        task = Task.objects.count()
        for id in range(1,task+1):
            url = reverse('task_detail', kwargs={'id' : id})
            response = self.client.get(url, format='json')

            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_detail_task(self):
        
        max_id = Task.objects.all().aggregate(Max("id"))["id__max"]
        
        url = reverse('task_detail', kwargs={'id' : max_id+1})
        
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Test the create task view 
    def test_valid_create_view(self):
        
        url = reverse('task_create')
        data = {
            'id' : 5,
            'title' : 'Task5',
            'state' : 'draft'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 5)

    
    def test_invalid_create_view(self):
        
        tests_data =[
            {'id' : 5, 'title' : '', 'state' : 'done'},
            {'id' : 5, 'title' : 'task5', 'state' : ''},
            {'id' : 5, 'title' : 'Task5','state' : 'finished'}
        ] 

        for data in tests_data:
            
            url = reverse('task_create')
            response = self.client.post(url, data, format='json') 
             
            self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
            self.assertNotEqual(Task.objects.count(), 5)

    # Test the update view 
    def test_valid_update_view(self):
    
        tasks = Task.objects.all()
        for task in tasks:
            url = reverse('task_update', kwargs={'id':task.id})
            if task.state == 'draft':
                
                tests_data = [
                    {'id' : 1,'title' : 'Task1','state' : 'active'},
                    {'id' : 1,'title' : 'Task1','state' : 'archived'}
                    ]
               
                for data in tests_data:
                        response = self.client.put(url,data, format='json')
                    
                        self.assertEqual(response.status_code,status.HTTP_200_OK)

                            
            elif task.state == 'active':
               
                tests_data = [
                    {'id' : 2,'title' : 'Task2','state' : 'done'},
                    {'id' : 2,'title' : 'Task2','state' : 'archived'}
                    ]
               
                for data in tests_data: 
                    response = self.client.put(url,data, format='json')
                
                    self.assertEqual(response.status_code,status.HTTP_200_OK)
                
            
            elif task.state == 'done':
             
                tests_data = {'id' : 3,'title' : 'Task3','state' : 'archived'}
                response = self.client.put(url, tests_data, format='json')
                self.assertEqual(response.status_code,status.HTTP_200_OK)
        
            else:
                tests_data = [
                    {'id' : 4,'title' : 'Task4','state' : 'draft'},
                {'id' : 4,'title' : 'Task4','state' : 'active'},
                {'id' : 4,'title' : 'Task4','state' : 'done'}
                ]

                for data in tests_data:
                
                    response = self.client.put(url,data, format='json')
                    self.assertNotEqual(response.status_code,status.HTTP_200_OK)

        self.assertEqual(Task.objects.count(), 4)    

    def test_invalid_update_view(self):
    
        tasks = Task.objects.all()
        for task in tasks:
            url = reverse('task_update', kwargs={'id':task.id})
            if task.state == 'draft':
                
                data =  {'id' : 1,'title' : 'Task1','state' : 'done'} 
                response = self.client.put(url,data, format='json')         
                self.assertNotEqual(response.status_code,status.HTTP_200_OK)

                            
            elif task.state == 'active':
               
                data = {'id' : 2,'title' : 'Task2','state' : 'draft'}
                response = self.client.put(url,data, format='json')    
                self.assertNotEqual(response.status_code,status.HTTP_200_OK)
                
            
            elif task.state == 'done':
             
                tests_data =[ {'id' : 3,'title' : 'Task3','state' : 'draft'},{'id' : 3,'title' : 'Task3','state' : 'active'}]
                response = self.client.put(url, tests_data, format='json')
                self.assertNotEqual(response.status_code,status.HTTP_200_OK)
        
            else:
                tests_data = [
                    {'id' : 4,'title' : 'Task4','state' : 'draft'},
                {'id' : 4,'title' : 'Task4','state' : 'active'},
                {'id' : 4,'title' : 'Task4','state' : 'done'}
                ]

                for data in tests_data:
                
                    response = self.client.put(url,data, format='json')
                    self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)

        self.assertEqual(Task.objects.count(), 4)

    # Test the delete view which deletes task by id
    def test_valid_delete_view(self):
        task = Task.objects.count()
        for i in range(1,task+1):
            url = reverse('task_delete', kwargs={'id':i})
            response = self.client.delete(url, format='json')

            self.assertEqual(response.status_code, status.HTTP_200_OK)