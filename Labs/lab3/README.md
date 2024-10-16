# Lab 3  

## Assignment  

The purpose of this lab is to investigate the concept of *linear classification*.  

<details>
<summary>For the grade G this includes:</summary>  

- read data from a CSV file  
- plot the data points  
- find a linear decision boundary  
- implement a function that classifies points on either side  
- write to a new CSV file with an added column containing labels 

</details>


<details>
<summary>For the grade VG this includes a report containing the following: </summary>  

- include other linear decision boundaries
- classify data for each  
- argue as to whether or not there's a reason to prefer one line over another  

</details>

## Code explanation  

### Summary  

The script within lab 3 can be run within any folder. The script itself classifies data points from a CSV file based on a linear decision boundary. It then plots the data and writes the labels to another CSV file containing both data points and labels.  

In the report I touch on different examples and why each linear classifier is somewhat pointless without the proper labels. I briefly mention other techniques that perhaps would suit this type of data better, in my opinion.  

### Using the script

The line itself can be manipulated within the script. Exchange the values for the global variables *K* and *M* to get a different result.  

The report also contains additional code that was necessary to provide other examples since the script is streamlined for only one. The functions from the script are imported and the global variables remain the same but can be altered for separate results (see the list variable *examples*).  