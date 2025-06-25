TASK-1

We are using try and exceptiion for reading file and testing the condition if the file is not present.

When on try, teh script attempt to read the file and if found it performs the below task. 
The function realines is able to read lines without mentioning the line number as once the function is executed, it moves the cursor to the next step. So when there it another line value, it reads the other line. If we try to execute that command again for the third time, it will return an empty value as there is no third line.
But in case if the file is not present, the exceptioon throws the error condition with the desired message in the print statemnt.


TASK-2
Here user is giving the input to be enetred in an existing file, output.txt. If the file did not exist, it will throw and error.
Once first part of the text is entered, we get and option to enter more message, which is getting appended with the previously entered message. If we use write, instead of append, the previous message will be overwritten with the new message.
After appending we are getting the Final output by reading the output.txt file