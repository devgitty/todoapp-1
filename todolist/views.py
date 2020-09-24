# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import TodoList, Category, WeekTargetList
import datetime
# Create your views here.

def index(request): #the index view
	todos = TodoList.objects.all() #quering all todos with the object manager
	categories = Category.objects.all() #getting all categories with object manager
	weektargets = WeekTargetList.objects.all() #getting all week targets with object manager
	if request.method == "POST": #checking if the request method is a POST
		if "taskAdd" in request.POST: #checking if there is a request to add a todo
			title = request.POST["description"] #title
			date = str(request.POST["date"]) #date
			category = request.POST["category_select"] #category
			content = title + " -- " + date + " " + category #content
			Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
			Todo.save() #saving the todo 
			return redirect("/") #reloading the page
		
		if "taskDelete" in request.POST: #checking if there is a request to delete a todo
			checkedlist = request.POST["checkedbox"] #checked todos to be deleted
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
				todo.delete() #deleting todo

		if "WeekTargetAdd" in request.POST: #checking if there is a request to add a todo
			description = request.POST["week_target_description"]
			comment = request.POST["comment"]
			due_datetime = str(request.POST["due_datetime"])
			show_in_number_of_week_cycles = str(request.POST["show_in_number_of_week_cycles"])
#			category = request.POST["category_select"] #category
#			content = title + " -- " + date + " " + category #content
			WeekTarget = WeekTargetList(description=description, comment=comment, due_datetime=due_datetime, show_in_number_of_week_cycles=show_in_number_of_week_cycles)
			WeekTarget.save() #saving the weektarget 
			return redirect("/") #reloading the page
		
		if "WeekTargetDelete" in request.POST: #checking if there is a request to delete a todo
			checkedlist = request.POST["checkedbox"] #checked todos to be deleted
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
				todo.delete() #deleting todo
	

	return render(request, "index.html", {"todos": todos, "categories":categories, "weektargets": weektargets})


def page2(request): #the page2 view
	return render(request, "page2.html")


def show_week_targets(request): #the show_week_targets view
	return render(request, "show_week_targets.html")
