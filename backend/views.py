from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib import messages
from django.http import HttpRequest

from django.contrib.auth import authenticate, login, logout

from backend.models import Contribution, Projects, Users
from backend.serializers import ContributionSerializer, ProjectSerializer, UserSerializer, EditProject

from .forms import CreateUserForm
from rest_framework.decorators import api_view
import requests
import json
import logging

# Create your views here.
@csrf_exempt
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was created successfully")
            response = JsonResponse("Create successfully", safe=False)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Credentials'] = 'true'
            user_serializer = UserSerializer(data={
                'name': request.POST.get('username'),
                'email': request.POST.get('email'),
                'avatar': 'avatar',
                'coverBackground': 'coverBackground',
                'description': 'description',
                'facebook': 'facebook',
                'phone': request.POST.get('phone')
            })
            if user_serializer.is_valid():
                user_serializer.save()
            return response
        
    context = {'form': form}
    response = JsonResponse("register failed", safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response
    #return render(request, 'register.html', context)

@csrf_exempt
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #user = authenticate(request, username=username, password=password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            response = JsonResponse("login successfully", safe=False)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Credentials'] = 'true'
            return response
            #return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect")
    
    context = {}
    #return render(request, 'login.html', context)
    response = JsonResponse("login failed", safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response

def homePgae(request):
    context = {}
    return render(request, 'home.html', context)

@csrf_exempt
def projectAPI(request, id=0):
    if request.method == 'GET':
        projects = Projects.objects.all()
        projects_serializer = ProjectSerializer(projects, many=True)
        response = JsonResponse(projects_serializer.data, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
    elif request.method == 'POST':
        project_data = JSONParser().parse(request)
        project_serializer = ProjectSerializer(data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            response = JsonResponse("Added successfully", safe=False)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Credentials'] = 'true'
            return response
        response = JsonResponse("Failed to add", safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
    elif request.method == 'PUT':
        project_data = JSONParser().parse(request)
        project = Projects.objects.get(id=project_data['id'])
        project_serializer = ProjectSerializer(project, data=project_data)
        logger = logging.getLogger("django")
        logger.info(project_serializer)
        if project_serializer.is_valid():
            project_serializer.save()
            response = JsonResponse("Update successfully", safe=False)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Credentials'] = 'true'
            return response
        response = JsonResponse("Failed to Update", safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
    elif request.method == 'DELETE':
        project = Projects.objects.get(id=id)
        project.delete()
        response = JsonResponse("Delete successfully", safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
    else:
        response = JsonResponse("Hi from server", safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response

@csrf_exempt
def userAPI(request, id=0):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UserSerializer(users, many=True)
        response = JsonResponse(users_serializer.data, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response 
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            response = JsonResponse("Added successfully", safe=False)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Credentials'] = 'true'
            return response
        response = JsonResponse("Failed to Add", safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = Users.objects.get(id=user_data['id'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            response = JsonResponse("Update successfully", safe=False)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Credentials'] = 'true'
            return response
        response = JsonResponse("Failed to Update", safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
    elif request.method == 'DELETE':
        user = Users.objects.get(id=id)
        user.delete()
        response = JsonResponse("Delete successfully", safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
    else:
        response = JsonResponse("Hi from server", safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response

def updateProjectContribution(projectID, amount):
    project = Projects.objects.get(id=projectID)
    project_serializer = EditProject(project, data={
        'id': project.id, 
        #'creatorId': project.creatorId, 
        #'name': project.name,
        #'category': project.category, 
        #'description': project.description, 
        #'image': project.image, 
        #'imageName': project.imageName,
        #'targetPrice': project.targetPrice, 
        #'isFeatured': project.isFeatured, 
        'currentPrice': project.currentPrice + int(amount, base=10), 
        'donationCount': project.donationCount + 1,
        #'createAt': project.createAt
    })
    '''
    logger = logging.getLogger("django")
    logger.info(type(project.id))
    logger.info(type(project.creatorId))
    logger.info(type(project.name))
    logger.info(type(project.category))
    logger.info(type(project.description))
    logger.info(type(project.image))
    logger.info(type(project.imageName))
    logger.info(type(project.targetPrice))
    logger.info(type(project.isFeatured))
    logger.info(type(project.currentPrice + int(amount, base=10)))
    logger.info(type(project.donationCount + 1))
    logger.info(type(project.createAt))
    logger.info(project.id)
    logger.info(project.creatorId)
    logger.info(project.name)
    logger.info(project.category)
    logger.info(project.description)
    logger.info(project.image)
    logger.info(project.imageName)
    logger.info(project.targetPrice)
    logger.info(project.isFeatured)
    logger.info(project.currentPrice + int(amount, base=10))
    logger.info(project.donationCount + 1)
    logger.info(project.createAt)
    logger.info(project_serializer)
    '''
    if project_serializer.is_valid():
        project_serializer.save()
        return 1
    else: 
        return 0

@csrf_exempt
def contributionAPI(request, id=0):
    if request.method == 'GET':
        contribution = Contribution.objects.all()
        contribution_serializer = ContributionSerializer(contribution, many=True)
        response = JsonResponse(contribution_serializer.data, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response 
    elif request.method == 'POST':
        contribution_data = JSONParser().parse(request)
        contribution_serializer = ContributionSerializer(data=contribution_data)
        if contribution_serializer.is_valid():
            check = updateProjectContribution(contribution_data['projectId'], contribution_data['amount'])
            if check == 1:
                contribution_serializer.save()
                response = JsonResponse("Added successfully", safe=False)
                response['Access-Control-Allow-Origin'] = '*'
                response['Access-Control-Allow-Credentials'] = 'true'
                return response
        response = JsonResponse("Failed to Add", safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
    elif request.method == 'PUT':
        contribution_data = JSONParser().parse(request)
        contribution = Contribution.objects.get(id=contribution_data['id'])
        contribution_serializer = ContributionSerializer(contribution, data=contribution_data)
        if contribution_serializer.is_valid():
            contribution_serializer.save()
            response = JsonResponse("Update successfully", safe=False)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Credentials'] = 'true'
            return response
        response = JsonResponse("Failed to Update", safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
    elif request.method == 'DELETE':
        contribution = Contribution.objects.get(id=id)
        contribution.delete()
        response = JsonResponse("Delete successfully", safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
    else:
        response = JsonResponse("Hi from server", safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response