---
title: Exercise 4
linktitle: 4. Seasons
date: '2023-03-20T00:00:00+01:00'
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
---

# Seasons

Besides trends in time series, a common pattern in natural datasets is a cycle of some sort, whether it be a diurnal or seasonal cycle.  Here we will explore ways to quantify the amplitude, period and phase of a cycle.  Amplitude refers to how big the fluctuations are (half the difference between the peak and trough value); period refers to how far apart in time the peaks are separated; and phase describes when a peak happens (e.g., for a seasonal cycle, it can be used to identify whether the time series peaks in the summer or winter).

**Aim:**  This lab explores a method of time series analysis for oscillating data.

**Learning outcomes:**
At the end of this lab, you will be able to:

1. Load data into Matlab (a `mat`-file containing data variables)
2. Work with the structure class of variables in Matlab
3. Gain basic familiarity with \textit{indices} in Matlab.
4. Use the function  `fit_harmonics.m` to fit a sinusoid with period 365.25 days to a time series.


**Data:** You will work with a time series of SST from the North Atlantic, in filename `oisst_t1.mat`.


---

# Working with m-files. 

**Create an m-file.**  While in Matlab, it is possible to work in the command window, typing commands at the command prompt as needed, it can be useful to store the commands that works, in the right order, in a separate file for later use.  That way, if you needed to carry out the same calculations again, you would not have a useful record of what you had done.   An `m`-file is like a Word document where you can write your Matlab commands, save them, and use them again later.  

 To open an m-file, in the Matlab window, select `File>New>Script`.  Save the file as `time_series_analysis.m`. 

 _Note: Matlab doesn't like filenames with dashes or spaces in them, or names that start with a number._

**Executing the m-file.** Matlab  executes lines of code in sequential order, from top to bottom.  It skips lines that are commented (beginning with the `%` sign).  These comments show up in a different colour than commands in the Matlab editor.  
```matlab
>> disp('Hello World')  % This is a comment
```

Once you type commands into your m-file, you can highlight them and the use the F9 shortcut to evaluate the selected code.  You can also click the green run button, which will evaluate the whole m-file.  Or, you can type the `ctrl-return` keystroke to evaluate the current cell within your m-file.

A _cell_ is a segment of code that is separated by a line that begins with exactly two percent symbols (no spaces between them).  Two percent symbols (`%%`) with no spaces between or before them start a new cell.  Any text that occurs after the two percents is also a comment.

**Throughout this lab, enter your commands into your m-file rather than the command prompt, then execute the m-file in order to see your results.**   To print results to the screen,  either omit the semicolon (simple) or use the `disp` command to add more detailed information (advanced).    Comment your work.  

# Exploring the a time series of SST in the Atlantic

**Load the data** and check what has been loaded (Recall: commands `load` and `whos`).

This time, your variable is of class `struct` or structure.  A Matlab structure is a bit like a file folder, with different variables contained within it.  The `whos` command won't show us what's in it.  

To see what's in a structure, use the `disp` command instead:
```matlab
>> disp(oisst1)
```
You should find four fields: `time`, `lat`, `lon`, and `sst`.  To access the variables inside a structure, you use the structure name and then the field name, with a dot in between.  So to access the time vector, use `oisst1.time` and to access the sea surface temperatures, use `oisst1.sst`.

Plotting your data can be a great way to get an idea of what you've got. **Create figure 1** and plot the $\mathrm{CO}_2$ time series against the time vector using the `figure` and plot` commands.  

```matlab
figure(1); clf  % clf clears the current figure
plot(oisst1.time,oisst1.sst)
```

Fix the x-axes using the `datetick` command.  (Recall: command `datetick`.)  Add a grid using `grid on`.  

Normally when we create scientific figures to display data, we annotate them so the viewer knows what is plotted. Try annotating the figure with some helpful labels on the x- and y-axis.
```matlab
ylabel('Temperature [deg C]')
title('Provide a useful title here')
```
See if you can use the commands `legend` and `xlabel`.

## Calculate some basic statistics 

1. What is the average of the time series?     Specify your answer to the nearest 100th. (Recall: command `mean`.)
<!--20.73 deg C-->

```matlab
tmean = mean(oisst1.sst)
```

_**Advanced:** The function `disp` takes a string as input (the variable `output_string`).  It can be used to print useful information to the screen._

```matlab
output_string = [`The average of the SST data is `,num2str(tmean),` deg C`];
disp(output_string)
```

_This was created from three different strings separated by commas.  The first string, denoted by the apostrophes, is simple text "The average of the SST\ldots".  The second string is constructed from the numeric value contained in the variable `tmean`, but  converted to a string using the function `num2str`.  The third string is again denoted by  apostrophes.  Enclosing them in square brackets combines them into one long string._

2. What is the standard deviation of the time series?
<!--2.08 deg C-->

*Hint: If you don't remember a command, you can try to find it by using the Matlab command `lookfor` and a keyword.  For example, *

```matlab
>> lookfor deviation
```


3. How many years long is the record (i.e. the temporal range or coverage of the dataset)?  Report your answer to the nearest 10th of a year.
<!--22.5 years-->

_Hint: Recall  that Matlab stores time in units of days.  If you take the first day in the record, and subtract it from the last, you will have the number of days of the record._

```matlab
numdays = max(oisst1.time)-min(oisst1.time);
```



## Find the seasonal cycle

Looking at the time series, you can see a strong seasonal cycle.  Here, we will quantify the seasonal cycle by fitting a sinusoid to it, with a period of 365.25 days.


### Method 1: Use the function `fit_harmonics.m` 

This is not a built-in Matlab function.  Make sure you download it to your computer, then open it in the editor to have a look at what it does.  Use the `help` command to see how to use it.

```matlab
>> help fit_harmonics
```

This function takes 5 inputs: the data, the time vector, the number of harmonics you want to calculate (for us, this will always be 1), the period (with the same units as the time vector), and the cutoff for how important the harmonic is (we will always use zero).

Choose the values of the parameters to use (the number of harmonics, period and cutoff) and enter them in your `m`-file as 

```matlab
%% Fitting a harmonic
nharm = 1;
L = 365.25;
cutoff = 0;
```
Now add the line of code to calculate the harmonic, storing all the outputs.  
<!-- line of code-->

4. One of the outputs of the function `fit_harmonics` is the _amplitude_ of the cycle.   What is the seasonal _range_?
<!--5.69 deg C-->

Recall that we created cosine-type sinusoids last time, where for $y=3\cos(2\pi t/T)$ we wrote in Matlab, `y=3*cos(2*pi*time/365.25)`.  Calculate a cosine for the seasonal cycle using the output from fitting a harmonic. In this case, we will create a cosine with the form $y = a\cos(2\pi t/L+\phi)$, where the amplitude $a$ is given by the output `amp` and the phase $\phi$ by `pha`.  The period $L$ was set by the input `L`.


**Update the figure:** Add the seasonal cycle to figure 1. You will need to use the `offset` from the outputs from fitting a harmonic in order to get the seasonal cycle on top of the original data.  Annotate the figure with a legend so you can distinguish between the two lines.

_Recall the command `hold on` and how to make the line a different colour._

**Export the figure** in `*.png` format.  Recall the steps we used last time.

_**Advanced:**  Alternatively, you can save figures automatically by adding these lines to your m-file:_
```matlab
% Export the figure.  Name it sst_cycle.png
set(gcf,'paperpositionmode','auto')
print('-dpng','sst_cycle.png')
```
_The `set` command is optional, but will preserve the aspect ratio of your figure on the screen if, for instance, you resize the window before saving the figure._

5.  In what month does the time series peak?  Zoom in on your figure around one of the peaks in the seasonal cycle.  Then redo the `datetick` command with a third input, to prevent Matlab from resetting the x-axis limits when adding the date ticks.
```matlab
datetick('x','mmm','keeplimits');
```
<!--August-->

### Method 2: Calculate a seasonal climatology

In oceanography, we often refer to a time series of monthly averages as a seasonal climatology.  We can calculate that in this case as well, using more advanced programming concepts: the `for-do` loop or `for-loop`.  

If we want to calculate a seasonal climatology for the SST time series, we can start by calculating the average SST in January.  First we need to find which of the elements in the vector `oisst1.sst` are from January.


The command `month` converts matlab time (in units of days since Jan 1, 0000) into numeric months, ranging from 1-12.  To create a vector of the months that is the same length as the vector `oisst1.sst`, we can apply `month` to the time vector, `oisst1.time` as

> ```matlab
> month_vec = month(oisst1.time);
> ```

Then we can use the find command to determine which of those elements are from January:
```matlab
index_jan = find(month_vec==1);
```

The output, `index_jan` is a vector of indices.  Do a whos on it, and you'll see it is not the same length as `month_vec` or `oisst1.time`, from which it is derived. Instead, it is exactly as long as there are datapoints from January.  The values within `index_jan` are the positions or indices of those datapoints from January.

Then if we want the January mean, we can calculate
```matlab
jan_mean = mean(oisst1.sst(index_jan));
```

6. What is the average temperature in January?
<!--18.6 deg C-->

To create the seasonal cycle, we could repeat these lines of code 12 times,
```matlab
index_jan = find(month_vec==1);
jan_mean = mean(oisst1.sst(index_jan));
index_feb = find(month_vec==2);
feb_mean = mean(oisst1.sst(index_feb));
index_mar = find(month_vec==3);
mar_mean = mean(oisst1.sst(index_mar));
```
Then if we wanted a seasonal cycle, we could string together those 12 values as
```matlab
seasonal_cycle = [jan_mean feb_mean mar_mean ...]
```

The more compact and versatile way to do this is to use a `for-loop`.

```matlab
for mdo=1:12
    index_month = find(month_vec==mdo);
    month_mean = mean(oisst1.sst(index_month));
    seasonal_cycle(mdo) = month_mean;
end
```

7. Using this method, what is the seasonal range?

See if you can make a figure to show both methods of calculating the seasonal cycle on them.  Call it `sst_cycle2.png`.
