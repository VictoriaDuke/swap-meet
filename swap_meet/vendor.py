from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_category(self, category=""):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, their_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in their_vendor.inventory:
            return False
        self.remove(my_item)
        self.add(their_item)
        their_vendor.remove(their_item)
        their_vendor.add(my_item)
        return True
    
    def swap_first_item(self, their_vendor):
        if not self.inventory or not their_vendor.inventory:
            return False
        my_first_item = self.inventory[0]
        their_first_item = their_vendor.inventory[0]
        return self.swap_items(their_vendor, my_first_item, their_first_item)
