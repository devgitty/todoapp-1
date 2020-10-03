# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Category, WeekTargetList
import datetime
# Create your views here.

from .forms import WeekTargetForm

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
			is_during_working_hours = str(request.POST["is_during_working_hours"])
			day_target_show_from_weekday = str(request.POST["day_target_show_from_weekday"])
			day_target_show_to_weekday = str(request.POST["day_target_show_to_weekday"])
			associated_email_received_datetime = str(request.POST["associated_email_received_datetime"])
			associated_email_received_account = str(request.POST["associated_email_received_account"])
			plan_duration_mins = str(request.POST["plan_duration_mins"])
			recurrence_period_weeks = str(request.POST["recurrence_period_weeks"])
			status_category = str(request.POST["status_category"])
			week_target_backlog_item_sorting_category_indistinguishable = str(request.POST["week_target_backlog_item_sorting_category_indistinguishable"])

			WeekTarget = WeekTargetList(description=description, comment=comment, due_datetime=due_datetime, show_in_number_of_week_cycles=show_in_number_of_week_cycles, is_during_working_hours=is_during_working_hours, day_target_show_from_weekday=day_target_show_from_weekday, day_target_show_to_weekday=day_target_show_to_weekday, associated_email_received_datetime=associated_email_received_datetime, associated_email_received_account=associated_email_received_account, plan_duration_mins=plan_duration_mins, recurrence_period_weeks=recurrence_period_weeks, status_category=status_category, week_target_backlog_item_sorting_category_indistinguishable=week_target_backlog_item_sorting_category_indistinguishable)
			WeekTarget.save() #saving the weektarget 
			return redirect("/") #reloading the page
		
		if "WeekTargetDelete" in request.POST: #checking if there is a request to delete a weektarget
			checkedlist = request.POST["checkedbox"] #checked todos to be deleted
			for weektarget_id in checkedlist:
				weektarget = WeekTargetList.objects.get(id=int(weektarget_id)) #getting weektarget id
				weektarget.delete() #deleting weektarget
	

	return render(request, "index.html", {"todos": todos, "categories":categories, "weektargets": weektargets})



from django.views import generic

class WeekTargetListView(generic.ListView):
	"""Generic class-based view for a list of books."""
	model = WeekTargetList
	paginate_by = 10

class WeekTargetDetailView(generic.DetailView):
	"""Generic class-based view for a list of books."""
	model = WeekTargetList


#New WeekTarget:
def page2(request):
	weektargets = WeekTargetList.objects.all() #getting all week targets with object manager
	if request.method == "POST":
		form = WeekTargetForm(request.POST)
		WeekTarget = form.save(commit=False)
		WeekTarget.save()
		return redirect("/") #reloading the page
	else:
		form = WeekTargetForm()
	return render(request, 'page2.html', {'form':form})

#Detail WeekTarget:
def page3(request, pk):
	WeekTarget = get_object_or_404(WeekTargetList, pk)
	return render(request, 'page3.html', {'WeekTarget':WeekTarget})

#Edit WeekTarget:
# def page4(request, pk):
# 	weektarget = get_object_or_404(WeekTargetList, pk=pk)
# 	if request.method == "POST":
# 		form = WeekTargetForm(request.POST, instance=WeekTarget)
# 		WeekTarget = form.save(commit=False)
# 		WeekTarget.save()
# 		return redirect('page3', pk=WeekTarget.pk) #reloading the page
# 	else:
# 		form = WeekTargetForm(instance=WeekTarget)
# 	return render(request, 'page4.html', {'form':form})

#def page2(request): #the page2 view
#	return render(request, "page2.html")


def show_week_targets(request): #the show_week_targets view
	weektargets = WeekTargetList.objects.all() #getting all week targets with object manager
	return render(request, "show_week_targets.html", {"weektargets": weektargets})
