from django.db import models

class Brand(models.Model):
	name = models.CharField(max_length=200, db_index=True, unique=True)

class Retailer(models.Model):
	name = models.CharField(max_length=200, db_index=True, unique=True)

class RetailStore(models.Model):
	name = models.CharField(max_length=200, db_index=True, unique=True)
	retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, db_index=True)

class Product(models.Model):
	name = models.CharField(max_length=200, db_index=True, unique=True)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE, db_index=True)

class ProductInStore(models.Model):
	retailStore = models.ForeignKey(RetailStore, on_delete=models.CASCADE, db_index=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True)
	promotion = models.CharField(max_length=200, db_index=True, unique=True, null=True, blank=True)
	available = models.BooleanField(default=True)

