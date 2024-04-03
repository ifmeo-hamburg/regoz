---
title: Exercise 5
linktitle: 5. Spatial
date: '2023-03-20T00:00:00+01:00'
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
---

# Spatial data

Satellite data often comes in the form of a map over a wide geographic area.  It also has repeat samples in time.  This combination of map-style data repeated in time results in 3-dimensional data (with the dimensions being x, y and t or lat, lon and t).  Here we will explore how to use loops to work with 3D data.

**Aim:**  In this lab, we will try handling 2- and 3-dimensional data, making maps and carrying out basic time series analysis using a loop. 


**Learning Outcomes:**
At the end of this lab, you will be able to:

1. Reinforce (from last time) loading data into Matlab (e.g. `mat`-files containing data variables) 
2. Reinforce (from last time) working with the structure class of variables in Matlab.
3. Reinforce basic familiarity with _indices_ in Matlab, in a more complex situation, using Booleans.
4. Again, use the functions `fit_harmonics.m`, `polyfit.m` and `polyval.m` for basic time series analysis.
5. For the first time, apply time series analysis to data using a for-do loop.


**Data:**
You will work with maps of sea surface height (SSH) from the North Atlantic, in filename `aviso_2maps.mat` and spatially- and temporally-varying SSH data from the North Atlantic, in filename `aviso_ssh_3d.mat`.  You can also use the file `coastlon.mat` to add coastlines to your figures.

**Directions:** Answer the questions, create an m-file, three figures and a movie.   _Recommended:_ Open a copy of the last practical(s), so you can remember how to use the commands.

**Check your answers:** This is a formative assessment rather than summative (i.e. the results here do not contribute to your mark in the course.)  Several "self-check" answers are provided along the way so you can see whether your calculations were correct for each section. 

---

**Create an `m`-file.** As before, create an `m`-file to record your work.  Thes solution file will be called `spatial_analysis_soln.m`.  

_Recall: Matlab doesn't like filenames with dashes or spaces in them, or names that start with a number._

**Load the data.** Load `aviso_2maps.mat` and check what has been loaded, using `whos` or, if necessary for structures, `disp`.
```matlab
load aviso_2maps.mat
load coastlon.mat
```
You should find several fields: `time`, `lat`, `lon`, and `ssh`, and some strings describing the data.   Since the data field `ssh` has the same number of rows as the `altim.lat` vector, and the same number of columns as the `altim.lon` vector, we guess that _the data are a map of sea surface height values which vary in space._

_Note! Comment your work.  This is good practice and will make it easier for you to remember what you've done or why._

# Explore the data by plotting it.
 To see what you have loaded, you can start by plotting the two sets of map data, `altim1` and `altim2`.  For 2-dimensional map data, we can use the function `pcolor` or `contourf` commands rather than `plot` to visualise the data.  

**Create a figure.** Recall the function `figure`.  Since you will have two subplots, use the `subplot` command to put two panels side-by-side in the same figure window.  For the spatial data, you can then use
```matlab
pcolor(altim1.lon,altim1.lat,altim1.ssh)
shading flat
```

To better see where in the world the data are from, add some coastlines using the `plot` function and the variables `coastlon` and `coastlat`.  To see what colours represent what values, use the function `colorbar`,
```matlab
colorbar('location','southoutside')
```

Add an appropriate title to describe when the data were made.  You can use either the `datestr` command with the `altim1.time` value, or the `altim.timestr` which is already provided in string format.

**Activate the other subplot.** Now activate the other subplot, and plot the data from `altim2`.

1. Overall, sea surface height looks higher in which of the two fields?
<!--altim1-->

2. Does this suggest that sea level is
    - rising? or
    - falling? <!--falling-->

## Calculate the change in SSH \label{q1}

Calculate the mean SSH in each of the two data structures.  For `altim1`, you should get 36.337 cm.  

3. What is the average for `altim2`?\label{p1}
<!--30.094 cm-->

_Note: This is a somewhat subtle question.  If you have the vector, 
`x = [1 1 1; NaN 2 2];` what answers do you get for the averages_
```matlab
nanmean(nanmean(x))
nanmean(x(:))
```
<!--1.33-->
<!--1.4-->
What has the `(:)` operator done to `x`?  (To see this, try writing `y=x(:)` and comparing `y` to `x`.)
\vspace{.5in}
<!--
It has turned the matrix `x` into a vector, with the same overall number of elements.-->
Which value is more representative of the average of all the values in `x`?
<!--1.4-->
Use this exercise with `x` to verify or improve your estimates of the average SSH in `altim1` and `altim2`.

4. How much has sea level changed?  Has it risen or fallen?
<!--6.244 cm, fallen-->

5. How far apart are they in time?  Give your answer in years.
<!--7487 days, 20.5 years-->

6. Using your values above, what is the rate of change of sea level in mm/yr?  \label{pp}
<!---3.046 mm/yr-->
<!--Self-check: you should have gotten a rate of `-3.046+ mm/yr`.-->


---

# Working with averages of the 3-dimensional data.

**Load the data and explore it.**  As before, but for `aviso_ssh_3d.mat`.  

7. How many dimensions does `altim.ssh` have?
<!--3-->

8. Which dimension corresponds to the `altim.time` vector?
<!--the 3rd dimension-->

Use the `size` function to return the size of each dimension.
```matlab
[AA,OO,TT]=size(altim.ssh);
```
<!--143, 225, 247-->

## Creating a map by averaging in time

Create an average of the sea surface height by averaging the data in the time dimension.  Use `help` on the function `nanmean` to see how to specify which dimension you are averaging in.
```matlab
mean_map = nanmean(altim.ssh,3);
```

Replace the second subplot in figure 1 with this new mean map.
```matlab 
figure(1)
subplot(122);cla
pcolor(altim.lon,altim.lat,mean_map);
shading flat
hold on
plot(coastlon,coastlat,'k')
caxis([-50 100])
xlabel('Longitude')
title('Time mean of SSH')
```

9. Comment on how the two maps look different.
<!--
The time-averaged map is much smoother, while the instantaneous map for Oct 1992 has more wiggles and splotches ($\leftarrow$ not a technical term).
-->

## Creating a time series by averaging in space.

Now we would like each map of SSH to be represented by a single average value (similar to the averages that were created in question \ref{q1}(\ref{p1}).

**Average the SSH data.** Because there are some NaNs in the data field, we reshape the data before averaging as 
```matlab
ssh_tseries_mean = reshape(altim.ssh,[AA*OO,TT]);
ssh_tseries_mean1 = nanmean(ssh_tseries_mean,1);
```

**Create Figure 2.** and activate the top panel using `subplot(2,1,1)`.  Here, plot the time series `ssh_tseries_mean1` using a black line.  Make the x-axis human readable.  (Check your previous labs to see how you did this.)  Add a y-label with units describing the axis, e.g.
```matlab
ylabel('Sea surface height [cm]')
```


**Calculate the annual cycle** using `fit_harmonics.m`.  See your previous lab to see how you did this.  You should use the function `fit_harmonics` for the appropriate values in `nharm`, `L` and `cutoff=0`.  You can then reconstruct the seasonal cycle as
```matlab
seasonal_cycle = amp*cos(2*pi*altim.time/L+pha)+offset;
```
Add the seasonal cycle to your plot in red.

10. In what month does the seasonal cycle peak? 
<!--October-->

11.  When is it a minimum?
<!--April-->

12. What is the seasonal range in SSH? 
<!--9.43 cm, or 9.23 if you do max-min-->

Calculate the residual by subtracting the seasonal cycle from the full time series.  Call it `resid1`.  Plot this in the second subplot in black.

**Fit a linear trend to the residual** using the `polyfit` and `polyval` functions. Call it `trend2`. Add this to the second subplot in red.  Annotate your figure with appropriate x- and y-axis labels and legends.

13. Over the full record, how much has the value of `trend2` changed?  
<!--3.704 cm-->

14. The seasonal range is **(greater / less than )**  than the total range in `trend2`?
<!--greater-->

15. Calculate the trend from the output from `polyfit`.    What is the trend?  Give your answer in mm/yr.
<!--0.00049477~cm/day, 1.8071+ mm/yr-->

16. Comment on why you think this answer differed from your answer in question \ref{q1}(\ref{pp}).
\vspace{1in}
<!--
The trend that you calculated in the previous section was based on two snapshots in time, one from October and one from April.  Since the seasonal cycle analysis has shown us that SSH peaks in October and is at a minimum in April, and the seasonal variability is large relative to the change over the 2 decades, this is what was estimated from the two snapshots.
-->

# Working with full 3-dimensional data. 

In the previous section, we spatially-averaged our data to create a simple time series that we could work with as in the previous lab.  Here we will use what we know from loops to calculate the trend at each location in the map.

## Calculate the trend for a single location.

Extract a time series of SSH from at or just north of $45^\circ$N and at or just east of $53^\circ$W.  Recall to find the index we can use
```matlab
ilat = find(altim.lat>=45,1,'first');
```
to identify the index of the latitude which has a value greater than or equal to 45.  Use similar code to find the index of the longitude, then create the individual time series as `ssh_tseries`.

Note that the size of `ssh_tseries` is [1 x 1 x 247].  Though it only has 1 non-singleton dimension (and so is a vector) it is stored in Matlab as a 3-dimensional matrix.  To get rid of the extra dimension, use `squeeze`,
```matlab
ssh_tseries1 = squeeze(ssh_tseries);
```

Now fit the annual cycle and remove the trend:
```matlab
[amp,pha,frac,offset,yy] = fit_harmonics(ssh_tseries1,altim.time,nharm,L,0);
seasonal_cycle = amp*cos(2*pi*altim.time/L+pha)+offset;
resid1 = ssh_tseries1-seasonal_cycle';
P2 = polyfit(altim.time,resid1',1);

slope1 = P2(1)*10*365.25; % in mm/yr
```
If you forget how `fit_harmonics.m` works, take a look at your previous practical.

## Calculate the trend at each location.  

This is the trickiest part of the practical.  

**Create the loop.** If you want to loop through all the latitudes and all the longitudes, you can create a loop shell like
```matlab
for ado=1:AA
      for odo=1:OO
            % Get the time series at the point given by indices ado and odo
        
            % Calculate the seasonal cycle
        
            % Remove the seasonal cycle
        
            % Fit a polynomial to the residual
        
            % Calculate the slope in mm/yr from the polynomial coefficients, call it slope1.
        
            % Store the slope
            all_slopes(ado,odo) = slope1;
        
      end
end
```

Fill in the gaps between the comment lines provided.

**Create figure 3.** a map of the trend in sea surface height at each location.
```matlab
figure(3);clf
pcolor(altim.lon,altim.lat,all_slopes)
shading flat
hold on
plot(coastlon,coastlat,'k')

% Annotate the figure
colormap(jet)
caxis([-5 5])
title('Trend in SSH after removing annual harmonic, in mm/yr')
xlabel('Longitude')
ylabel('Latitude')
colorbar
```

Self-check: You should get something like the figure shown below.

![Trends](../figures/gyre_fig3_trends.png)


# Making a movie (optional)  

Sometimes the best way to visualise data is to create a movie and _watch it_.  Unfortunately, the code doesn't seem to work on all computers in the PC labs, so you may need to fiddle with it.

**Create a movie.** Matlab has a handy set of functions called `VideoWriter` which you can find out about by doing a `>> help VideoWriter`.  To create a movie, we want to loop through time, and make a map of SSH at each time.  The following code may or may not work.
```matlab
obj = VideoWriter('SSHmovie.avi','Motion JPEG 2000');
open(obj);
figure(4);clf
for tdo=1:10%length(altim.time)
    pcolor(altim.lon,altim.lat,altim.ssh(:,:,tdo))
    shading flat
    caxis([-50 100])
    title(datestr(altim.time(tdo)))
    xlabel('Longitude')
    ylabel('Latitude')
    
    currFrame = getframe;
    writeVideo(obj,currFrame);
end
close(obj);
```
Note that in the example code, the loop index is set to run only from 1 to 10.  
This is a good way to test that it is working, and then open up the video file which you should find in the same directory, called `SSHmove.avi`, and see whether you can play it.  Once you have something that works, you can change the loop index to run through all time values as `tdo=1:length(altim.time)`.

Enjoy!   
