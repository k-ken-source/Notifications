Django Notifications Application- 

This is a simple Django web application that makes use of channels (Web Sockets) to send notifications to the frontend and JS Notification API to push these notifications. 

What can it do currently?
For now, the notifications are pushed every 10 seconds an infinite number of times.

Improvements to be made- 
1. Making use of channel layers and redis to handle the loop inside the async consumer. 
2. Creating an event to trigger these notifications. 

How to Use?
- Clone this Reposotiory. 

- It is recommended to create a virtual environment to run this application in isolation.
Read - https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

- After activating the virtual environment, simply install all the packages in the requirements.txt, 
    Linux - pip install -r requirements.txt

- Run the server using python manage.py runserver command and open localhost in a browser. 
