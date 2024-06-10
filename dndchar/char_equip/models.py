from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    total_AP = models.IntegerField(default=0)
    
class EquippmentSlot(models.Model):
    name = models.CharField(max_length=50, choices=(
        ("Head", "Head"),
        ("Chest", "Chest"),
        ("Left Hand", "Left Hand"),
        ("Right Hand", "Right Hand"),
        ("Legs", "Legs"),
        ("Backpack", "Backpack"),
    ))
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    power = models.IntegerField()
    slot = models.ForeignKey(EquippmentSlot, on_delete=models.SET_NULL, null=True, blank=True)