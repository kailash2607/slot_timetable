# Ex03 Time Table
## Date:

## AIM
To write a html webpage page to display your slot timetable.

## ALGORITHM
### STEP 1
Create a Django-admin Interface.

### STEP 2
Create a static folder and inert HTML code.

### STEP 3
Create a simple table using ```<table>``` tag in html.

### STEP 4
Add header row using ```<th>``` tag.

### STEP 5
Add your timetable using ```<td>``` tag.

### STEP 6
Execute the program using runserver command.

## PROGRAM

```
{% load static %}
<html>
<head>
<title>Slot Timetable</title>
</head>
<body>
<center>
<img src="{% static 'logo.png' %}" height="100" width="500">
</center>
<br>
<table align="center" width="500" cellspacing="3" cellpadding="2" border="2" bgcolor="4EB8F2">
<caption><b>SLOT TIME TABLE - KAILASH PRABHU S (212224240068)</b></caption>
<tr align="center">
<th bgcolor="88AD79">Day/Time</th>
<th bgcolor="88AD79">Monday</th>
<th bgcolor="88AD79">Tuesday</th>
<th bgcolor="88AD79">Wednesday</th>
<th bgcolor="88AD79">Thursday</th>
<th bgcolor="88AD79">Friday</th>
</tr>
<tr align="center">
<th bgcolor="C77ECC">8-10</th>
<td>Free Slot</td>
<td>FUNDAMENTAL OF C PROGRAMMING</td>
<td>FUNDAMENTAL OF C PROGRAMMING</td>
<td>Free Slot</td>
<td>Free Slot</td>
</tr>
<tr align="center">
<th bgcolor="C77ECC">10-12</th>
<td>Free Slot</td>
<td>PYTHON PROGRAMMING</td>
<td>Fundamentals And Web Applications</td>
<td>OPERATING SYSTEM</td>
<td>Free Slot</td>
</tr>
<tr>
<th bgcolor="C77ECC">12-1</th>
<td colspan="6" align="center">L U N C H    B R E A K </td>
</tr>
<tr align="center">
<th bgcolor="C77ECC">1-3</th>
<td>Fundamentals And Web Applications</td>
<td>Free Slot</td>
<td>Mentor Meet</td>
<td>Free Slot</td>
<td>Ethicial Hacking</td>
</tr>
<tr align="center">
<th bgcolor="C77ECC">3-5</th>
<td>Free Slot</td>
<td>PYTHON PROGRAMMING</td>
<td>OPERATING SYSTEM</td>
<td>Complier Design</td>
<td>Complier Design</td>
</tr>
</table>
<br>
<table align="center" cellspacing="2" cellpadding="2" border="2">
<tr align="center">
<th>S. No.</th>
<th>Subject Code</th>
<th>Subject Name</th>
</tr>
<tr>
<td align="center">1.</td>
<td align="center">19AI414</td>
<td align ="center">Fundamentals And Web Applications</font></b></td>
</tr>
<tr>
<td align="center">2.</td>
<td align="center">19MA134</td>
<td align="center">PYTHON PROGRAMMING</td>
<td></td>
</tr>
<tr>
<td align="center">3.</td>
<td align="center">19MA135</td>
<td align="center">OPERATING SYSTEM</td>
</tr>
<tr>
<td align="center">4.</td>
<td align="center">19AI307</td>
<td align="center">FUNDAMENTAL OF C PROGRAMMING</td>
</tr>
<tr>
<td align="center">5.</td>
<td align="center">19MA311</td>
<td align="center">Statistics and Numerical Method</td>
</tr>
<tr>
<td align="center">6.</td>
<td align="center">19CS409</td>
<td align="center">Complier Design</td>
</tr>
<tr>
<td align="center">7.</td>
<td align="center">19CS405</td>
<td align="center">Ethicial Hacking</td>
</tr>
</table>
</body>
</html>
```


## OUTPUT

<img width="1912" height="1016" alt="image" src="https://github.com/user-attachments/assets/1bf92487-684a-44a5-b92c-c36cf11efdca" />



## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
