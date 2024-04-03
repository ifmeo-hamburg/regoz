---
title: Exercise 2
linktitle: 2. CTD
date: '2023-03-20T00:00:00+01:00'
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
---

# Profile data

Most of oceanography deals with looking at *in situ* or in water data.  You did some of that with the boat work and analysis of CTD (conductivity-temperature-depth) data from the Callista.  Here, you will work with CTD data in Matlab.

**Aim:**  Use Matlab to plot and analyse some hydrographic data.

**Data:** You will work with a hydrographic data from the Southern Ocean in `ctd_data1.mat`.

**Prerequisites:** You should have completed the Matlab practical **Intro** and **Figures** before working on this one.

---

# Working with m-files. 

**Open an m-file.** In Matlab, open the script called `ctd_load.m`.  Note that all files which contain computer code written in the Matlab language are given the extension `*.m`.  This script loads in temperature data from ten CTD stations.

Examine the script in the Matlab editor.  

1. What does the `%` symbol in the Matlab script do?
<!--denotes a comment-->

**Run the script.** Run the code to see what it does.  (1) Either type the name of the script at the command window and press return, or (2) use the green arrow button above the window which contains the script.  Let's go through the script to see what it does.

- **Functions.** A _function_ is a set of instructions for Matlab to perform at task.  It can also accept _inputs_ or variables to be operated on.  For example, in line 11 of the script `ctd_load.m`, the `load` function is used.  The `load` function tells Matlab to load in the data file which you specify as an input (in this case, `ctd_data1.mat`).
- **Variables.** A _variable_ is a symbolic name or identifier used to reference stored values.  The data file `ctd_data1.mat` contains five variables:
    + `lat` - with the latitudes of the 30 CTD stations
    + `lon` - with the longitudes of the 30 CTD stations
    + `bin_press` - with pressure levels at which temperature was recorded
    + `bin_potemp` - with potential temperature for each of 30 stations, and at each of the pressure levels

## Exploring the data

2. What is the fifth variable loaded from `ctd_data1.mat`?  
<!--bin_sal-->

3. Is the `lat` variable a vector or a matrix?
<!--vector-->

4. Is the `bin_ptemp` variable a vector or a matrix?  How many rows and columns does it have?
<!--matrix, 3000 rows, 30 columns-->

5. Where was the third CTD station taken (provide lat and lon position).
<!--lat = -54.94, lon = -58.37-->

6. Find the temperature value at the 50th pressure level of the 3rd CTD station.
<!--5.09 deg C-->

7. What pressure was this taken at?
<!--99 dbar-->

## Plotting the data (points and lines)

Open the `m`-file `ctd_plot.m`.   What is the first cell doing?

_Note: In this file,some comments that start with a double `%%`.  The double `%%` at the beginning of a line indicates a new cell.  This means that you can click one of these cells and it will become highlighted in your editor with a pale yellow.  If you then type a `ctrl-return`, the highlighted cell only will be evaluated by Matlab.  This can be a handy way to break up large pieces of code._

Run just the cell plotting the lats and lons.  Add a title to the figure using the `title` command with an input string, e.g.
```matlab
title('Map of stations')
```

Run the cell plotting the vertical profile of temperature.

8. Is temperature higher near the surface or at depth? (Note that pressure increases as you go deeper.)
<!--near the surface-->

## Flow control: Using a `for-do` loop

Suppose you wanted to plot the temperature profile for every station.  You could copy and paste the code ten times, changing the value `8` from 1 to 30 in each example.
```matlab
plot(bin_ptemp(:,8),bin_press)
title('Station 8')
```

Matlab makes this easier using a `for-loop` or `for-do` loop.  We'll see these again later, but it is a way of repeating the same commands multiple times but only typing them once.

As a simple example of a for loop, try adding
```matlab
for i=[1 2 3]
    disp('hi')
end
```
in a new cell in your `m`-file.  You should find that it prints the word "hi" to your screen three times.  In this code, `i` is called the loop variable, and you are telling Matlab that first for the value of `i=1`, execute the code between the lines starting with `for` and ending with `end`.  Then do it again for the value of `i=2` and `i=3`.

Now open the code `ctd_loop.m`.  Try to figure out what it is doing before executing the code.  

9. What has changed in these lines of code relative to the code in `ctd_plot.m`?
<!--8 was replaced by i-->

Evaluate the code.  You should get a lot of figure windows appearing on your screen.

_Helpful hint: Ok, now you have a ton of figures on your screen.  If you want to close them, you could click the little red close symbol in the corner of each one, or you could use a Matlab command.  Go back to your command window and type_
```matlab
>> close all
```
_All your figures should magically disappear._

## Plotting the data (colour plots)

When we have two-dimensional data (i.e., a matrix), we could plot it as a bunch of lines, or we could plot it as a contoured plot.  This is like a topo map you might use for hiking in a hilly region, or like a weather map where closed contours encircle regions of high or low pressure.

Execute the last cell in `ctd_plot2.m`.  This has created a contour plot of the potential temperature matrix as a function of depth (pressure) and position (latitude).  

10.  Is the temperature higher near the surface for all stations?
<!-- no, at higher latitudes there is some very cold water near the surface-->

11. In general, is the temperature warmer at lower latitudes (smaller negative latitudes) or at higher latitudes?  How can you tell?
<!--lower latitudes.  For most depths/pressures, the isotherms are tilted downwards towards lower latitudes-->

## Creating new figures to display data

Repeat some of the styles of plots that you did above.

12. Make a TS plot (plotting temperature against salinity) for two stations.  Pick one station where that cold band of water can be seen in your contour plot, and one station where the surface water is quite warm.  Label the station numbers using the `legend` command.  **Export this figure as a JPG.**

13. Make a section of salinity to go along with the section of temperature.

14. Try to plot all the temperature and salinity profiles on a single TS diagram.  

15. Now plot every other TS profile.  This will require writing a loop.  


