# Goat ability test using Django templating.


The style sheets in this repo are duplicate of the style sheet in the other repo. However, in this repo I have used Django and templating in HTML, using Django gives the end user the ability to log in to the admin and add content themselves. 

# Create a simple component
In this directory (devTest1), I create three models:
* Feature - for the featured row at the top of the page. 
* CategoryMemu - for the menu items
* Insights - for the insight cards. 

Once the models have been created I used a for loop in the HTML file to iterate over the content of the model.
For the insight cards an if statement is used to evaluate whether the boolean field is True or False, if True the video icon in the top right of the card is included. 

Pictured is the Insights model in the models.py file, and the element it creates in the djano admin site. 

![example of model](media/screenshot1.png)

# Create a complex component 
In this directory (devTest2), I create four models:
* backgroundImage - gives the user the ability to change the image of the two students from the admin page if they wanted to 
* breadcrumbs - the breadcrumb menu at the top of the page
* frames - the four frame at the bottom of the page.
* headline - the main quote in the centre of the page. 

Once the models have been created I used the same templating format I used for devTest1 and used a for loop to iterate over the content of each model. 

# Troubleshooting 
Please view other repos read.me file for this section.