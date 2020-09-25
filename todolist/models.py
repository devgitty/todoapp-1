# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import timedelta

#from django.urls import reverse # Used to generate URLs by reversing the URL patterns


# Create your models here.
class Category(models.Model): # The Category table name that inherits models.Model
	name = models.CharField(max_length=100) #Like a varchar

	class Meta:
		verbose_name = ("Category")
		verbose_name_plural = ("Categories")

	def __str__(self):
		return self.name #name to be shown when called

class TodoList(models.Model): #Todolist able name that inherits models.Model
	title = models.CharField(max_length=250) # a varchar
	content = models.TextField(blank=True) # a text field 
	created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
	due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
	category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE) # a foreignkey

	class Meta:
		ordering = ["-created"] #ordering by the created field

	def __str__(self):
		return self.title #name to be shown when called

class WeekTargetList(models.Model):
	show_in_number_of_week_cycles = models.IntegerField(null=True)		#models.IntegerField(null=True)
	is_during_working_hours = models.IntegerField(null=True)
	day_target_show_from_weekday = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
	day_target_show_to_weekday = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
	week_target_backlog_item_sorting_category_indistinguishable = models.CharField(max_length=250)
	description = models.TextField(blank=False)
	comment = models.TextField(blank=False)
	associated_email_received_datetime = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
	associated_email_received_account = models.CharField(max_length=250)
	plan_duration_mins = models.IntegerField(null=True)
	recurrence_period_weeks = models.IntegerField(null=True)
	due_datetime = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
	status_category = models.CharField(max_length=250)

	class Meta:
		ordering = ["-description"]

	def __str__(self):
		return self.description #name to be shown when called