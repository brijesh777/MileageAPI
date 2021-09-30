# MileageAPI

##API Reference


###Getting Started
At present this app can only be run locally and its not hosted as base url.


### Error Handling
Not Much Error handling is done in current version

### Assumptions
To make tasks easy, I have create  2 Models. Vechile and Vechile Mileage. Vechile table will store all the vechile latest mileage(current mileage). Every day, mileage of vechile will get update. Once update is one, similar entry is done in mileage table with time column. To find the mileage from any day, user have to pass unit number and exact date to find actual distance travel until today. For time being, I have taken time column as string.


###End points
####GET vechile/show
It will return all the the data from vechile table


####GET  vechile/show?unit=1
This endpoint will return data from particular vechile



####PUT vechile/show?unit=1
You can do partial update and full update too.To do partial update you use POSTMAN and pass JSON object of mileage

###GET vechile/3/2021-09-28
This endpoint passes vechile unit number and the past date from where you want to find the mileage. This endpoint will find the distance travel by  vechile  from given date to current date. 











