#created by Matthew Walsh
#created on oct 2017
#created for ICS3U
#this program calculates factorials

import ui


def factorial_button(sender):
    
    #variables
    counter = 1
    factorial_value = 1
    
    #input 
    user_input = int(view['number_textfield'].text)
   
    #process 
    if user_input < 0:
    	 #output
       view['answer_label'].text = "Please enter a positive value."
       
    else:
    	while counter <= user_input:
    		factorial_value = counter * factorial_value      
    		counter = counter + 1   
    		#output          
    		view['answer_label'].text = "The factorial is: " + str(factorial_value)

view = ui.load_view()
view.present('full_screen')
