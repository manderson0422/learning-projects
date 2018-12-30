#Project1 - Task Tracker

##Keep a list of tasks - Dictionary!
###Add tasks
####Name, Description, Due Date
###Remove tasks
####Mark as complete or incomplete
##Add reminder feature
###TODO LATER

task_tracker = {} #Starting variable for dict of tasks

task_tracker = { 
	1 : {"name" : "dishes", "description" : "washing plates"}, 
	2 : {"name" : "vaccuum", "description" : "clean carpet"}, 
	3 : {"name" : "laundry", "description" : "wash clothing"},
	4 : {"name":"1n","description":"1d"}
}  #prepopulating data for testing



print("Welcome back! Here are your tasks:")
for t in task_tracker: 
	counter = str(t) + ")" 
	print(counter, task_tracker[t]["name"], "-", task_tracker[t]["description"])
