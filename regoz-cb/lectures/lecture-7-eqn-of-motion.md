---
title: Lecture 7. Equations of motion
linktitle: 7. Equations of motion
date: '2023-03-20T00:00:00+01:00'
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 107
mathjax: true
header-includes:
  - \usepackage{amsmath}
---



## Equations of motion



$\newcommand{\pfrac}[2]{\frac{\partial #1}{\partial #2}}$

$\newcommand{\sW}{\mathrm{W}}$
$\newcommand{\sH}{\mathrm{H}}$
$\newcommand{\sU}{\mathrm{U}}$
$\newcommand{\sL}{\mathrm{L}}$
$\newcommand{\sT}{\mathrm{T}}$


**Main ideas: Dynamics**

1. There are 4 main equations that describe fluid flow, 3 of which describe momentum (velocity) in the 3 spatial directions, and the 4th which describes evolution of water density.

2. The  forces are due to pressure gradients, Coriolis, gravity and friction.

3. Pressure in the ocean is due mostly to the weight of water above it (*hydrostatic pressure*\footnote{Know this equation.  We will apply it in coursework.}), but if there is more or heavier water in one location compared to another, this will drive an acceleration.  

In the next few lectures, we will examine the equations that govern ocean circulation.   What makes the ocean go?  starting from the forces that are acting on the fluid. These tend arise from interactions between the water and boundaries (friction at the bottom or surface, and interaction with the atmosphere which generates density anomalies).

Key quantities will feature throughout: pressure (due to the weight of water above), seawater density, rotation of the earth.  We'll start with a generic set of equations (called the equations of motion), and will use various techniques to simplify the equations to better understand how the ocean behaves.

### Four forces for the ocean

We are going to look at (1) the forces that govern fluid flow, (2) how we modify Newton's second law for fluids, and (3) the form of these four forces in the equations of motion for the ocean.

In physical oceanography, there are **four basic forces** that act on the fluid.

1. gravity
2. the pressure gradient force
3. rotation (Coriolis)  _(Note: Coriolis is not a true "force" but an 
    apparent force.  We use it to account for the rotation of the Earth and that we are interested in how fluids behave relative to the Earth's surface (i.e. in a rotating frame of reference)._
4. friction

We will see how the different forces combine to produce typical fluid behavior, whether the fluid is in static (unmoving) or dynamic (moving) equilibrium.  We will also see how the effect of rotation modifies ocean circulation.

**Force = mass $\times$ acceleration (Newton's second law)**

From physics, recall that the relationship between the force applied and an object's response (acceleration) depends on the mass of the object.  This is given by Newton's second law: Force = mass $\times$ acceleration ("force equals mass times acceleration"), or 

$$\mathbf{F_m}=m\vec{a}$$

where $\mathbf{F_m}$ is the force on an object, $m$ is the mass of the object and $\vec{a}$ is its acceleration.  

*Note: we use the arrow $\vec{a}$ to denote that acceleration is a vector quantity, typically 3-dimensional (in the $x$, $y$ and $z$ dimensions).  In the case of acceleration, $\vec{a}=(\partial u/\partial t,\partial v/\partial t,\partial w/\partial t)$.*

A classic example is the gravitational force which can be written

$$F = mg$$

where $g$ is the gravitational acceleration, approximately 9.8 m $\mathrm{s}^{-2}$.

### Applying Newtonian physics to fluids

For fluids rather than solid bodies, we modify Newton's second law.

**Density vs. mass**

For solid physics, the mass of an object (or planet) $m$ is the important variable for force.  In the case of a fluid, it may be difficult to define a piece of the fluid with fixed mass.  Since fluids can change shape and the volume under consideration may vary, it becomes convenient to use density instead of mass in the equations governing fluid physics.  Density is related to mass as mass per unit volume.

Rewriting Newton's second law, we have

$$\mathbf{F_f} = \rho\vec{a}$$

where now $\mathbf{F_f}$ is the force per unit volume (note the change in units!  Exercise for you: what are the units on $\mathbf{F_f}$?) and $\rho$ is density.   We will now drop the subscript $_f$ and refer to forces as forces per unit volume.

**Material derivative**

This is an important concept in fluid dynamics of the oceans.  The ``material derivative'' is the change in time of a quantity *following the fluid parcel*.  What does this mean?

When we consider the rate of change of the velocity or a chemical concentration in the ocean, we measure this rate of change at a fixed point:  

$$\frac{d}{dt}$$

This fixed-location approach is an "Eulerian" description of changes.  Now suppose we were measuring the concentration of a chemical in the ocean and that chemical (e.g., nitrate) was higher concentration at depth than near the surface, and a big subsurface wave came by lifting up some of the nitrate-rich waters passed our sensor, 

$$w\frac{dN}{dz}$$ 

we might see a big change at our fixed point 

$$\frac{d}{dt}=\mbox{ big!}\ .$$

This is fine, and the measurement is real, but what it represents in the ocean is better interpreted as "advection of nitrate-rich waters passed the sensor" rather than "large increase in nitrate with time".

We can talk about this quantitatively with the **material derivative** or particle derivative. This can be written for an arbitrary quantity $C$ as

\begin{align}
\frac{DC}{Dt} &= \frac{\partial C}{\partial t} + \vec{u}\cdot\nabla C\\
&=\frac{\partial C}{\partial t} + u\frac{\partial C}{\partial x} + v\frac{\partial C}{\partial y}+w\frac{\partial C}{\partial z}
    \end{align}

With this formulation, the $\partial C/\partial t$ is the local rate-of-change of the quantity C "following the fluid particle", while $DC/Dt$ is the Eulerian rate-of-change of C at a fixed point which may be due both to a local rate-of-change and the advection of waters with a different concentration passed the measurement location.

_Here, we are using the notation $D/Dt$ instead of $d/dt$ because it is easier to distinguish when writing on the board (or in your assessments).  Textbooks may use the lowercase $d$, but should always be distinguished from the partial derivative, written with the curly $\partial$.  **In this class, please use capital $D$ for the material derivative.**_

<!-- $\blacklozenge$ If you are shaky on vector notation, e.g. the dot product used above, or the gradient of C (written $\nabla C$), please review the handbook from SOES2028, available on this blackboard website.-->

## Equations of Motion

Ok--the momentum equations or Newton's second law are modified for fluids where we write 

$$a = F_f/\rho$$ 

or acceleration is given by force-per-unit-volume per density.  Acceleration is the rate-of-change of fluid flow (velocity) with time, where the rate-of-change is using the material derivative.

Here are the equations of motion, in the notation that you should plan to use for this class.  We will use $v$ positive in the northward direction (negative in the southward direction), $u$ positive in the eastward direction, and $w$ positive upwards.

### Momentum equations

The momentum equations for fluid motion describe how the circulation evolves (given by the time derivative of velocities on the left hand side) under the effect of various forces (the terms on the right hand side).  For much of the course, we will actually consider the balances of the forces (right hand side) in steady state, meaning with no evolution or acceleration (left hand side is zero).

<!--$$\underbrace{\frac{Du}{Dt}}_{\text{Eastward accel.}} =\underbrace{-\frac{1}{\rho}\frac{\partial p}{\partial x}}_{\text{Pressure Gradient Accel.}}  \underbrace{+fv}_{\text{Coriolis Accel. }}  \underbrace{+F_x}_\text{Frictional Accel.}$$

$$\underbrace{\frac{Dv}{Dt}}_\text{Northward Accel.} =\underbrace{-\frac{1}{\rho}\frac{\partial p}{\partial y}}_\text{Pressure Gradient Accel.}  \underbrace{-fu}_\text{Coriolis Accel. }  \underbrace{+F_y}_\text{Frictional Accel.}$$

$$\underbrace{\frac{Dw}{Dt}}_\text{Upward Accel.} = \underbrace{-\frac{1}{\rho}\frac{\partial p}{\partial z}}_\text{Pressure Gradient Accel.} \underbrace{-g}_\text{Gravit. Accel. } \underbrace{+F_z}_\text{Frictional Accel.}$$-->


![Momentum equations](/figures/lectures/momeqns.png)
where $p$ is pressure, $f$ the Coriolis parameter, and $(F_x,F_y,F_z)$ the frictional acceleration in 3-directions.



## Scaling analysis (for information, not to be examined in RegOz)

Scale analysis is a technique to determine which terms in an equation are bigger and which are small enough to be ignored.  This helps us simplify the equations of motion (i.e., when it is valid and acceptable to throw out terms) under certain assumptions and approximations.

We will not cover this in detail in this course, but you should be aware that for regional ocean processes, when we are talking about whether `offshore Ekman transport' or `Sverdrup gyres' are a reasonable representation of what we see in observations, what we are really doing is starting with the full equations of motion, then simplifying them by making assumptions (or using empirical evidence) to decide which terms are large or small.  

### Typical scales for velocity/independent variables

See also Table 4.1 in BCR.

_Recall: Independent variables are things like the axes, x, y, t.  Dependent variables are ones which vary in those directions._

Set the scales:

$$[u,v] \sim \mathrm{U}  \ ,\qquad\qquad [w]\sim \mathrm{W}$$


$$\left[\pfrac{}{x},\pfrac{}{y}\right] \sim \frac{1}{\mathrm{L}} \ ,\qquad\qquad \left[\pfrac{}{z}\right] \sim \frac{1}{\mathrm{H}} 
\ ,\qquad\qquad\left[\pfrac{}{t}\right] \sim \frac{1}{\mathrm{T}}
$$ 
Let $\rho=\rho_0 + \rho'(x,y,z,t)$ according to the Boussinesq approximation, then
\begin{align*}
[\rho,\rho_0]&\sim\rho_{oo} & [\rho']&\sim \Delta\rho
\end{align*}
where $|\rho'|\ll\rho_0$.

**Notation:** Square brackets $[\cdot]$ denote _scale of_, which is like the order of magnitude. 

We will also let $p=\bar{p}(z)+p'(x,y,z,t)$, where though $\rho_0$ was a constant, $\bar{p}$ depends on $z$ (which we expect from the background hydrostatic pressure/$z$-momentum equation: the deeper you go, the higher pressure gets even if density is constant). We will refer to the scale of pressure perturbations as using the $[\cdot]$ notation as $[p']$.

