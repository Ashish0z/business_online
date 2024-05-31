from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField(default=1500)
    # Add other player attributes

class Property(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    owner = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    # Add other property attributes

class Game(models.Model):
    players = models.ManyToManyField(Player)
    current_turn = models.ForeignKey(Player, related_name='current_turn', on_delete=models.SET_NULL, null=True)
    # Add other game attributes
