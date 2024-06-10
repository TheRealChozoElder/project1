from django.shortcuts import render, redirect
from .models import Character, EquippmentSlot, Item

def char_detail(request, character_id):
    character = Character.objects.get(pk=character_id)
    equip_items = Item.objects.filter(slot__character=character_id).exclude(slot__name="Backpack")
    backpack_items = Item.objects.filter(slot__character=character_id, slot__name="Backpack")
    return render(request, 'character_detail.html', {
        'character': character,
        'equip_items': equip_items,
        'backpack_items': backpack_items,        
    })
    
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def equip_item(request, character_id, item_id):
    character = Character.objects.get(pk=character_id)
    item = Item.objects.get(pk=item_id)
    if item.slot is None or item.slot.character != character or not item.slotname == "Backpack":
        if EquippmentSlot.objects.filter(character=character, name=item.slot.name).exists():
            equip_item = Item.get(slot__character=character, slot__name=item.slot.name)
            character.total_AP -= equip_item.power
            equip_item.slot = None
            equip_item.save()
        item.slot = EquippmentSlot.objects.get(character=character, name=item.slot.name)
        character.total_AP += item.power
        item.save()
        character.save()
    return redirect('character_detail', character_id)