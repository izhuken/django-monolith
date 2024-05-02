from uuid import uuid4

from django.db import models
from django.urls import reverse_lazy


class Ticket(models.Model):
	id = models.UUIDField(
		primary_key=True,
		db_index=True,
		default=uuid4,
		editable=False
	)
	name = models.CharField(max_length=256, blank=False, null=False)
	phone = models.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
		return str(self.name)


class News(models.Model):
	id = models.UUIDField(
		primary_key=True,
		db_index=True,
		default=uuid4,
		editable=False
	)
	title = models.CharField(max_length=256, blank=False, null=False)
	description = models.TextField()
	preview = models.ImageField(upload_to='news')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.title)

	def get_absolute_url(self):
		return reverse_lazy("news", kwargs={"pk": self.id})