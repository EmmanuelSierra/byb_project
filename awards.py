# In the following we have an example of how could be a table with resutls display,
# if you would like to add "input()" you must add "int()" as well to run it properly.

print("Triatlhon results in minutes:")
print("")
swimming =30
print("Swimming = 30")
cycling = 30
print("Cycling = 30")
running = 42
print("running = 42")
print("")

print("Time taken for Swimming task:",swimming)
print("Time taken for Cycling task:",cycling)
print("Time taken for Running task:",running)

# Using the func() string = data1 + data2 + data3 
# We have the total and now we can use if, elif and else forms. 
# make sure you position correctly the "> "=" <" to display the correct target desired. 

Total_time = swimming+cycling+running
print("") 
print("Total time taken for triathlon:",Total_time)

if (Total_time < 100):
    print("Award: Provincial Colors")
elif (Total_time > 100 and Total_time <=105):
    print("Award: Provincial Half Colors")
elif (Total_time >105 and Total_time <=110):
    print("Award: Provincial Scroll")
else:
    print("Award: No award")
    print("")

# Final result will print out something like:
#     Triatlhon results in minutes:

#Swimming = 30
#Cycling = 30
#running = 42

#Time taken for Swimming task: 30
#Time taken for Cycling task: 30
#Time taken for Running task: 42

#Total time taken for triathlon: 102
#Award: Provincial Half Colors    

#----------------------------END---------------------------#

























