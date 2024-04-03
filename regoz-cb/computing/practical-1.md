---
title: Exercise 1
linktitle: 1. Intro
date: '2023-03-20T00:00:00+01:00'
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
---



# Matlab Introductory lab

**Directions:** 
Follow the instructions on this worksheet and write your answers as you go along.  Have the Blackboard website open since you will need it to download the data files, view the additional teaching videos and to check your answers.  If you have any trouble, check to be sure you followed the instructions.  If you still need assistance, ask a demonstrator during the timetabled Matlab practicals.

**Aim:** This practical assumes *no prior Matlab knowledge*.  By following the steps below, you'll learn how to access Matlab on a University computer, how to load some simple `*.csv` files, and carry out basic arithmetic.  We'll introduce the concepts of scalars, vectors and matrices in Matlab.  

**Learning outcomes:** At the end of this lab, you will be able to:

1. Load data into Matlab (e.g. `csv`-files containing numerical values only).
2. Create variables in Matlab from numbers, i.e. simple *scalars*, *vectors* (using the colon, `:`) and *matrices*, so that you can perform calculations on the variables after.
3. Perform simple averages of the data and arithmetic operations, using  functions `mean`, `median`, `sin`,  operators `-`, `*`, and `/`, and transpose vectors and matrices using apostrophe, `'`.
4. Use Matlab commands `load` and `whos` to investigate files and variables, and see how the special character, semicolon, `;`, works in Matlab to suppress output to the screen.

**Data:** Use the `data_vector.csv` and `data_matrix.csv` data files, available on Blackboard. 


**Check your answers:** This is a formative assessment rather than summative (i.e. the results here do not contribute to your mark in the course).  Answers will be available for you to check on Blackboard.    

---

## Getting started with Matlab:

1. **Log on to a PC & Find Matlab.** Log into a machine in the 68/121/02 computer lab (or anywhere on campus) with your username and password.

    On the PCs in 121, you find it under "all programs".  You can either search, or click the start menu and find it.  Last year, it was under "numerical modeling".  Click or double click to open.

## Setting up the practical files:

3. **Download files from Blackboard.** Go to the Blackboard website and find the files for the first Matlab practical (two `*.csv` files).  Click them to download.  If when you first click it, you get a page where it says "if it didn't download, click here", use the right mouse button to click.  In the menu that drops down, select "save target as" and save it to your Downloads.  If files  are in a zip archive, unarchive this (by double clicking) and they will now be located in a subdirectory (subfolder).  You can move these files up a directory (folder) into the same folder with everything else.

4. **Move the files to a folder in your My Documents.**
_This step is  important!_ If you don't put your files in the right place, they will be deleted when you log off the machine.   There are two _My Documents_ folders on your machine. One is a general one (don't use this!), and the other is for your work in particular.  Find yours within a folder that has your username.  Inside this My Documents folder (inside the folder with your username), create a new folder for this module.  Move the files   from Blackboard into this folder.
 
5. **Move Matlab to work inside your new folder.**
If you want Matlab to see the new files you've downloaded, you need to change it to work in that new folder.
Within Matlab, this means changing the `Current Folder`.  You can find the current folder at the top middle of the Matlab interface (see Fig. 1).  After the `Current Folder:` and folder name, there is a button with three dots.  Click this button then navigate to the folder where you put the data files.  

 
![Matlab interface (on a Mac)](../figures/computing/gettingstarted_fig1b-eps-converted-to.pdf)



---

## Arithmetic in Matlab
6. Matlab can carry out all basic kinds of arithmetic.  Most of the *operators* are the same as you'd expect.  Try typing the following mathematical expressions after the command prompt, `>>` in your Matlab Command window.  Press enter and Matlab will *evaluate* or carry out your *command*. 

a. Try the following in your Matlab command window.
```matlab
>> 3+5*2
```
<!-- 13 -->

b. Recall *order of operations* for arithmetic.  It applies in Matlab as well.
```matlab
>> (3+5)*2
```
<!-- 16 -->

c. Fractions or division
```matlab
>> 3/5
```
<!-- 0.6000 -->

d. Raise numbers to powers (i.e. squaring numbers) 
```matlab
>> 5^2
```
<!-- 25-->

e. Irrational numbers
```matlab
>> pi
```
<!--3.1416-->

f. Trigonometric functions
```matlab
>> sin(pi)
```
<!--0-->
_Note: that due to machine or numeric precision, this may not be exact._

g. More functions
```matlab
>> log10(10)
```
<!--1-->

7. **Create a *variable* in Matlab.**  One of the powerful things about programming languages is that you can "name" your data.  Rather than carrying out a stream of calculations in the command window, you can work with different numbers at the same time, save partial answers, and combine them later.

a. **Create a *scalar* variable.**  To create a variable, you choose a name for it which starts with a character, e.g. `a`, and then put it at the left of the equal sign in your command window.  Put the value you'd like to assign to that variable to the right of the equal sign.    A scalar variable is a single number.
```matlab
>> a=3
```

    Then execute a `>> whos a` to see the attributes of `a`.  Examine `a` in your Matlab Workspace.

b. **Vector variables.** Create a vector.  In Matlab, we call a string of numbers held together a *vector*.  In Matlab, square brackets do the holding together (not brackers or curly braces).  This can be confusing terminology, because it differs from the word *vector* for math, which is something with both direction and magnitude. 
`>> x=[1 2 3]

c. Repeat this using `y` instead, but "suppress the output" by using a semi-colon (`;`)  
```matlab
>> y=[1 2 3];
```

    *Note: The only difference between (b) and (c) is that in (c), the output is not printed to the screen; the variable is still created.  It can be useful to suppress large output.*

d. **Manipulating vector orientation.** Change the orientation of `y` by _transposing_ the vector using an apostrophe (`'`)
```matlab
>> z = y'
```

    Use the `whos` command to see how `z` and `y` differ.  
    _Recall: that the transpose of a matrix means to switch the rows and columns._

e. **Using functions on variables.** Calculate the mean of your variable `y`.  Use the Matlab *function* `mean`.  Note: the brackets are required!
```matlab
>> mean(y)
```
<!--2-->

## Loading data from a CSV file

Matlab would be rather tedious if you needed to type everything into it by hand.  If you have a spreadsheet of data handy, you can load the whole spreadsheet into a variable in Matlab.

8. **Loading a `*.csv` file into Matlab.** 

a. Load the data
```matlab
    >> data_vector = csvread('data_vector.csv');
```

b. **Where did the data go?** *Method 1: the whos command.*  Do a `whos` to see what variables were created.  In your command window, type
```matlab
    >> whos
```
*Method 2: the Matlab Workspace window.*  Check the variables that you have loaded and active in your Workspace window.  It also tells you the size of the variables, and their class (numeric, character).

c. **Size of the variable.**  The size of a vector refers to how many *elements* are in it.   You will need to use a Matlab function `size`.  To see how to use it, use the Matlab command `help`.
```matlab
    >> help size
```

    *Note: Reading Matlab help  is difficult to start with, but you should get in the habit of trying to skim the help information--first read the top line and paragraph.  The top line tells you what the function does, and the first paragraph describes the simplest way it can be used.   Then, near the bottom of the help information, you can often find an example of how to use the function.*

    What is the size of the `data_vector`?  (Give  an answer as [number $\times$ another number].)
<!--11x1-->

d. **Dimensionality of the variable.**  In Matlab, we call a variable a 2-dimensional matrix if it has 2 non-singleton *dimensions*.  A vector which is `100x1` is still 1-dimensional.  It has one _non-singleton_ dimension (the first dimension is 100 elements long) and one _singleton_ dimension (the second dimension is singular or 1 element long), while a matrix that is `2x2` is 2-dimensional.  Is this new variable a matrix or a vector?

<!--a vector-->


e. **Extract data from the vector.**  What is the value in the 4th element of the vector?  You can answer this by looking in your Workspace window, but you should learn to access the information using _indices_.  We'll cover what an _index_ is in a future practical.
```matlab
>> data_vector(4)
```
<!--2-->

## Working with variables

9. **Basic calculations.**  Matlab has standard commands to calculate the mean or median of a dataset.

a. **Mean.** Calculate the mean of the data using the `mean` command.  This command takes one *input* or piece of information that the function uses in its calculation.  In this case, the input is the name of the variable that you'd like to average.  
```matlab
>> mean(data_vector)
```
<!--6.1818-->

b. Now instead of the command above, try the command
```matlab
>> mean data_vector
```
Is the answer the same?  
**$\therefore$ Brackets (parentheses) are important!**
<!--No, the one with brackets is correct-->

c. **Addition.** Add two elements together using the `` operator:
```matlab
>> data_vector(1) + data_vector(2)
```
<!--4-->
Note how the elements of the column are accessed in Matlab, using brackets and the row number.

d. **Median.** Calculate the median using the `median` command.
```matlab
>> median(data_vector)
```
<!--3-->


10. **Working with a matrix in Matlab.**

a. Load the file `data_matrix.csv`.  What is the `size` of the variable loaded? (Recall: the `whos` command.)
<!--11x2-->

b. **Vector vs Matrix.** In Matlab, we call a variable a 2-dimensional matrix if it has 2 non-singleton dimensions.  Is this new variable a matrix or a vector?
<!--Matrix-->

c. **Mean of a matrix.** Calculate the mean of this matrix,
```matlab
>> mean(data_matrix)
```
<!--[6.1818 and 3.7273]-->

d. What was averaged here?

    - The average of each of the rows was calculated? or
    - The average of each of the columns was calculated.

e. The first dimension in Matlab (i.e. the `R` in the `RxC` of the size) is the number of rows and the second dimension is the number of columns.  Is this the same as in Excel?  (Load the `*.csv` file into Excel to check.)
<!--the same-->



11. **More complex operations and variables.**

a. **Repeating calculations for each element of a vector.** Some calculations can be carried out on individual elements of a vector rather than on the whole thing. Calculate the square of the individual elements in the vector `x`.  In Matlab, this is accomplished by using the dot operator, as
```matlab
>> x.^2
```
<!--1  4  9-->

b. **Create a matrix.** Create a 2-dimensional matrix `w`.  How many rows and columns does `w` have?
```matlab
>> w = [[1 2 3]; [4 5 6]]
```
<!--2 rows, 3 cols-->

c. **Create a vector using the colon.**  For regular vectors, like the vector containing the numbers 1 through 10, you can use a special operator to write it quickly.  Create a vector containing the numbers from 1 to 10 using a colon (`:`). How long is  `c`?
```matlab
>> c = 1:10
```
<!--10-->

d. In the previous example, the numbers were spaced by 1, which is the default.  You can also space them by an arbitrary value.  Create a vector containing the numbers from 1 to 10 but spaced by 0.5.  How long is the 1-dimensional vector `d`?
```matlab
>> d = 1:.5:10
```
<!--19-->

e.  Create a time vector called `time` that is 3 years long, on a daily time resolution.\label{time1}
```matlab
>> time = 0:1:365*3;
```
How long is the vector?
<!--1096-->


**Glossary:** New terms introduced during today's practical.

Words to describe numeric variables in Matlab:
- **variable**-
- **scalar**-
- **vector**-
- **matrix**-
- **dimension**-
- **element**-

Words related to programming:
* **evaluate**-
* **command**-
* **operator**-
* **function**-
* **input**-
  
