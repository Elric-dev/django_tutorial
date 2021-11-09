#after creating the objects on the models.py in the app, 
# use this code to create new objects

#in the working directory '/mysite'
#in the console: 
# python manage.py make migrations
# python manage.py migrate
# python manage.py shell ##-- to open the shell in the console

from main.models import Item, ToDoList
#create a new list
t = ToDoList(name='My List')
t.save()

#check all list objects on the app
ToDoList.objects.all()

#find list_oject by id
ToDoList.objects.get(id=1)

#filter query-set
ToDoList.objects.filter(name__startswith='My')

#delete an object
del_object = ToDoList.objects.get(id=1)
del_object.delete()

#print all item objects within a list object
t.item_set.all()

#creating and adding a new item object to the t list
t.item_set.create(text = 'finish the tutorial', complete=False)


#create superuser
#console commands
#python manage.py createsuperuser #then follow prompts
#elric
#gustavo.mafla@manwetech.com
#1234


#Templates
#dynamic HTML that changes based upo what passes through it


