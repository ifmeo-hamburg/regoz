---
title: Lecture 10. Sverdrup
linktitle: 10. Sverdrup
date: '2023-03-20T00:00:00+01:00'
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 110
---


$\newcommand{\pfrac}[2]{\frac{\partial #1}{\partial #2}}$

$\newcommand{\sW}{\mathrm{W}}$
$\newcommand{\sH}{\mathrm{H}}$
$\newcommand{\sU}{\mathrm{U}}$
$\newcommand{\sL}{\mathrm{L}}$
$\newcommand{\sT}{\mathrm{T}}$

**Main points:**

1. Conservation of *potential vorticity*.  Potential vorticity is a conserved quantity in the ocean and can be used to diagnose the ocean circulation.

2. Large scale southward circulation (in the gyres) results from latitudinal variations in Ekman transport.  This is called *Sverdrup balance*.*

# Vorticity and Sverdrup balance

## Conservation of potential vorticity

Here, we'll consider one of the implications of potential vorticity conservation on the large scale ocean circulation.  Potential vorticity 
$\boxed{q=\frac{(f+\zeta)}{H}}\tag{potential vorticity}$

is a conserved quantity in the ocean, where $f$ is Coriolis, $\zeta=\partial v/\partial x-\partial u/\partial y$ is the vertical component of relative vorticity (spinniness of the fluid) of a partcel of water.  Conservation of a quantity means that it does not change in time, so 

$$\frac{\partial q}{\partial t} = \frac{\partial }{\partial t}\left(\frac{f+\zeta}{H}\right) = 0 \ .$$


There are three parts of this equation:
- vorticity due to fluid circulation, $\zeta$
- vorticity due to Earth's rotation, $f$, which depends on latitude when considering a local vertical column
- Stretching ($1/H$) due to a fluid column stretching or shrinking.

Conservation of vorticity means that if one component changes in the numerator (e.g., $f$ increases or $\zeta$ increases) then the denominator must also change to keep the ratio constant (e.g., $H$ thickness must increase).

This is analogous to the conservation of angular momentum for solid body physics, but applied to a fluid parcel.  If you recall the example of an ice skater spinning, when he/she pulls in his/her arms (gets narrower/taller), the angular velocity increases.

<!--\begin{figure}
\includegraphics[width=.7\textwidth]{../figfiles/talley_dpo_vorticity_1.png}
\includegraphics[width=.7\textwidth]{../figfiles/talley_dpo_vorticity_2.png}\\
\includegraphics[width=.7\textwidth]{../figfiles/talley_dpo_vorticity_3.png}
\caption{Draw the two columns with different spin, from Talley's text DPO}\label{fig1}
\end{figure}-->



# Ekman pumping and suction

Variations in the stress on a surface lead to horizontal convergences and divergences of the Ekman transport, which is compensated for, by a vertical velocity divergence (i.e., stretching or shrinking). This process is called **Ekman pumping**. 


## Deriving the continuity equation

- Starting with the equation for conservation of mass - that mass cannot be created or destroyed
- Using scaling analysis, the assumption of a Boussinesq fluid ($\rho=\rho_0+\rho'(x,y,z,t)$ where $\rho'\ll\rho_0$), and the advective timescale assumption

We start with the equation for conservation of mass,

$$\frac{1}{\rho}\frac{D \rho}{D t}+\nabla\cdot\vec{u} = 0$$

Multiplying through by $\rho$ and expanding the divergence ($\nabla\cdot$), we get

$$\frac{D\rho}{Dt} +\rho \left(\pfrac{u}{x}+\pfrac{v}{y}+\pfrac{w}{z}\right) = 0$$

Expanding the material derivative $D/Dt$, and distributing the $\rho$ gives us

$$\pfrac{\rho}{t} + u\pfrac{\rho}{x} + v\pfrac{\rho}{y} + w\pfrac{\rho}{z} + \rho\pfrac{u}{x}+\rho\pfrac{v}{y} + \rho\pfrac{w}{z} =0
$$

Because we have that $\rho(x,y,z,t)=\rho_0+\rho'(x,y,z,t)$ (that variations in density are small relative to the magnitude of the density value), we can substitute it into the equation everywhere and drop small terms.  Since $\rho_0$ is a constant, we can drop it anywhere it appears inside a derivative (e.g., in all the terms in $D\rho/Dt$).  This is because the derivative of a constant is identically (exactly) zero.

For example, for the $\partial/\partial t$ term, 

$$\pfrac{}{t}(\rho) =\pfrac{}{t}(\rho_0+\rho')
=\pfrac{\rho_0}{t}+\pfrac{\rho'}{t}
=0+\pfrac{\rho'}{t}$$

Then our equation becomes

$$\pfrac{\rho'}{t} + u\pfrac{\rho'}{x} + v\pfrac{\rho'}{y} + w\pfrac{\rho'}{z} + (\rho_0+\rho')\pfrac{u}{x}+(\rho_0+\rho')\pfrac{v}{y} + (\rho_0+\rho')\pfrac{w}{z}  =0$$

Now, in the latter three terms (originating from the $\rho \nabla\cdot\vec{u}$), we are multiplying by $\rho_0+\rho'$.  However, we have defined the density decomposition such that  $\rho_0\gg\rho'$.  Then in each of these terms, we can drop the part multiplied by $\rho'$ as

$$(\rho_0+\rho')\pfrac{u}{x}\approx\rho_0\pfrac{u}{x}$$

since anything multiplied by $\rho'$ is much smaller than the same thing multiplied by $\rho_0$.
Cancelling out the terms which are multiplied by $\rho'$, we are left with

<!--\begin{align*}
\underbrace{\pfrac{\rho'}{t}}_{\substack{\rho_1\frac{1}{\sT}\\\\0}} + \underbrace{u\pfrac{\rho'}{x}}_{\substack{\rho_1\frac{\sU}{\sL}\\\\1}} + \underbrace{v\pfrac{\rho'}{y}}_{\substack{\rho_1\frac{\sU}{\sL}\\\\1}} + \underbrace{w\pfrac{\rho'}{z}}_{\substack{\rho_1\frac{\sW}{\sH}\\\\2}}+ \underbrace{\rho_0\pfrac{u}{x}}_{\substack{\rho_{oo}\frac{\sU}{\sL}\\\\3}}+\underbrace{\rho_0\pfrac{v}{y}}_{\substack{\rho_{oo}\frac{\sU}{\sL}\\\\3}} + \underbrace{\rho_0\pfrac{w}{z}}_{\substack{\rho_{oo}\frac{\sW}{\sH}\\\\4}} & =0
\end{align*}
-->
![figures/lectures/cancel_terms.png](/figures/lectures/cancel_terms.png)

We will apply an assumption called the _advective timescale assumption_ to give us that the scale of the $\partial\rho/\partial t$ term is the same as the $u\partial\rho/\partial x$.  This assumption says that the timescale $\sT$ associated with the $\partial/\partial t$ in the equation is set by the speed $\sU$ and distance $\sL$ under consideration.  Since rate times time equals distance, then

$$\sU\sT=\sL\qquad\mbox{ or }\qquad\sT=\sL/\sU$$

Applying this to our equation, this shows us that term 0 has the same scale as term 1.  Then comparing terms 1 and 3, and 2 and 4, we find that $1\ll3$ and $2\ll4$ since $\rho_1\ll\rho_{oo}$.

So we are left with retaining terms 3 and 4 which gives us the "incompressibility" equation (also called the nondivergence equation)

$$\underbrace{\pfrac{u}{x}}_3+\underbrace{\pfrac{v}{y}}_3 + \underbrace{\pfrac{w}{z}}_4 =0$$

## Using continuity to describe Ekman pumping

If we start from the continuity equation, but only consider velocities generated by Ekman processes $u_e$, $v_e$ we have

$${\pfrac{u_e}{x}}+{\pfrac{v_e}{y}} + {\pfrac{w}{z}} =0$$

We can integrate the equation with respect to $z$ (i.e., integrate in the vertical),

$$
\int_{-\delta}^0 \left({\pfrac{u_e}{x}}+{\pfrac{v_e}{y}} + {\pfrac{w}{z}}\right)\,\mathrm{d}z= 0$$
Taking the integrals inside the derivatives,

$$\pfrac{}{x} \int_{-\delta}^0 u_e\, \mathrm{d}z+\pfrac{}{y}\int_{-\delta}^0 v_e\,\mathrm{d}z + \int_{-\delta}^0{\pfrac{w}{z}}\,\mathrm{d}z= 0$$
Recall from the lecture on Ekman transport, that we defined variables

$$U_e\ ,\ V_e=\int_{-\delta}^0u_e\ ,v_e\ dz$$
where $U_e$ and $V_e$ were Ekman transport in units of m$^2$/s (rather than the standard units for transport of m$^3$/s).  Then we can replace these in our equation and get

Integrating the continuity equation with respect to $z$, we have

$$\pfrac{U_e}{x}+\pfrac{V_e}{y}+w(z=0)-w(z=-\delta)=0\ ,$$

We will assume that $w$ is zero at the sea surface (or at least very small).  We then define $w_e$ as the vertical velocity at the base of the surface Ekman layer (i.e.,  where $z=-\delta$), so $w(z=-\delta)=w_e$.  Then we can compute the value of this vertical velocity due to the horizontal convergence or divergence resulting from surface Ekman transport in the $x-$ and $y-$ directions:

$$w_e = \pfrac{U_e}{x}+\pfrac{V_e}{y}$$

Then replacing the $U_e$ and $V_e$ with the expressions based on stress by wind at the sea surface, we have

$$\boxed{w_e=\frac{1}{\rho f}\left(\pfrac{\tau^y}{x}-\pfrac{\tau^x}{y}\right)}\tag{Ekman pumping}$$

When the latitudinal gradients in Ekman transport (latitudinal gradients are the $\pfrac{}{y}$ ones) are such that water is "piled up" (i.e. a convergence), then Ekman pumping is downwards $w_e<0$.  This is the "pumping" direction.  Alternatively, if the water is pulled away (i.e., a divergence), then Ekman pumping is upwards to "fill the gap" left by waters being moved out of a region, and $w_e>0$ upwards.  This is called "Ekman suction".  If signs are not known, and we are generally referring to the phenomenon, then we use "Ekman pumping". 

![Ekman suction (left) and Ekman pumping (right).](/figures/lectures/neils-ekman-pumping.png)
The figure on the left is Ekman suction - on the right is Ekman pumping.

# Sverdrup relation

What is the effect of the Ekman pumping/suction on vorticity and large scale transports?

In particular, we will consider the third part of the vorticity equation (stretching).  In this case, we are going to return to our geostrophic equations with variable (Boussinesq) density and *without* making the $f$-plane approximation (so $f$ is not a constant but changes as a function of latitude).  

**Beta-plane approximation:** For the Sverdrup relation, we will simplify the variation of $f$ with latitude by using instead the $\beta$-plane approximation.  The $\beta$-plane approximation comes from the Taylor expansion of the sine in the equation for Coriolis, i.e.  $f=2\Omega\sin(\phi)$.  $f$-plane retains only the first (constant) term in the expansion, while the $\beta$-plane means also retaining the second term in the expansion.  Not shown here, but the result is:

$$
f=f_0+\beta_0 y
$$
where $f_0=2\Omega\sin\psi$ and $\beta_0 = 2(\Omega/a)\cos\psi$ where $a$ is the radius of the earth, and $\psi$ is the reference latitude.  Note that $\partial f/\partial y \approx \beta_0$.  Often, the subscripts $0$ for $f$ and $\beta$ will be dropped.

So, we start with our simplified equations of motion using geostrophic balance for the horizontal momentum equations,

$$\mbox{$x$-mom:\qquad} -fv = -\frac{1}{\rho_0}\pfrac{p}{x}\ ,$$
$$\mbox{$y$-mom:\qquad} fu =-\frac{1}{\rho_0}\pfrac{p}{y}\ , $$

and use hydrostatic approximation in the vertical,

$$\pfrac{p}{z} =-\rho g \ ,$$

and the incompressibility form of the  continuity equation,

$$\pfrac{u}{x}+\pfrac{v}{y}+\pfrac{w}{z} = 0\ .$$

The first step is to eliminate pressure from the momentum equations.

From examining the horizontal momentum equations, this can be accomplished by calculating the curl ($\nabla\times$) of the horizontal momentum equations,

$$\pfrac{}{x}(\mbox{$y$-mom})-\pfrac{}{y}(\mbox{$x$-mom}) \ .$$

This gives

$$\pfrac{}{x}(fu) - \pfrac{}{y}(-fv) = -\frac{1}{\rho_0}\pfrac{^2p}{x\partial y}-\left(-\frac{1}{\rho_0}\pfrac{^2p}{x\partial y}\right)$$

where, as intended, the pressure terms are cancelled on the right hand side:

$$\pfrac{}{x}(fu)+\pfrac{}{y}(fv) = 0\ .$$

Using the $\beta$-plane approximation,  $f$ varies with $y$ but  is not a function of $x$.  We can then apply the chain rule for derivatives, and then we have

$$f\left(\pfrac{u}{x}\right)+\pfrac{f}{y}\left(v\right) + f\pfrac{v}{y} = 0$$

Recalling that $\pfrac{f}{y}=\beta_0$, and rearranging the terms, we come to

$$
f\left(\pfrac{u}{x}+\pfrac{v}{y}\right) + \beta_0v = 0\ .
$$

Note that we don't replace the $f$'s above by $f_0$, but instead retain the full $f$. 

Then, noting from the continuity equation that

$$\pfrac{u}{x}+\pfrac{v}{y} = -\pfrac{w}{z}$$

we can replace the quantity in the brackets to give,

$$f\left(-\pfrac{w}{z}\right) + \beta_0 v =0$$

or, rearranging,

$$\boxed{\beta_0v = f\pfrac{w}{z}\ .}\tag{Sverdrup relation}$$

What is this telling us?  This says that as a column of water is stretching or squeezing ($\partial w/\partial z$), it needs to move meridionally (through a gradient in $f$ to account for the change in height or thickness.  This is an application of the conservation of potential vorticity. 

# Sverdrup transport

We can see the effects more clearly by integrating in the vertical, between a depth near the surface ($-\delta$, we'll see why in a minute) and the bottom of the ocean, $-h$,

$$\int_{-h}^{-\delta} \beta_0v\, \mathrm{d}z = \int_{-h}^{-\delta}f\pfrac{w}{z}\, \mathrm{d}z$$

$$\beta_0\int_{-h}^{-\delta} v\,\mathrm{d}z = f\left[w\big\rvert_{z=-\delta}-w\big\rvert_{z=-h}\right]$$

$$\beta_0\int_{-h}^{-\delta} v\,\mathrm{d}z = fw\big\rvert_{z=-\delta}
$$

where we have assumed there is no vertical flow at the bottom of the ocean (called the "no normal flow" condition, i.e. that there is no flow normal (perpendicular) to the sea floor).

So, what is this saying?  

It says that for the column of water between $-\delta$ and the bottom, if there is a vertical velocity at $-d$, pressing the layer downwards, then it is squashing the layer of water beneath it.  So this layer is getting shorter ($H$ in the potential vorticity equation is decreasing).  According to conservation of potential vorticity, either $f$ must decrease, or $\zeta$ must decrease (get more negative).   In this case, there is no relative vorticity ($\zeta=0$), so the column of water must adjust its planetary vorticity to reach a correct $f$ and conserve potential vorticity.


![](/figures/lectures/talley_dpo_sverdrup_gyre.png)

Now, why was it convenient to use $-\delta$?  Because we had an expression for vertical velocity at a depth of $-\delta$, where $\delta$ was the thickness of the Ekman layer.  This is related to the curl of the wind stress as,

$$
w_{e}=\frac{1}{\rho_0}\left[\pfrac{}{x}\left(\frac{\tau^y}{f}\right)-\pfrac{}{y}\left(\frac{\tau^x}{f}\right)\right]\ .
$$

Then our equation above becomes,

$$\boxed{\beta \int_{-h}^{-\delta}v\,\mathrm{d}z = fw_{e}\ .}\tag{Geostrophic Sverdrup balance}
$$

We can illustrate this with a few examples/practice problem.


This tells us about the meridional transport in the layer *beneath* the Ekman layer, but we already know about meridional transport in the Ekman layer due to the zonal wind stress.   Total Sverdrup balance is the sum of *geostrophic Sverdrup balance* and Ekman transport.

This was 

$$V_{ek} = -\frac{\tau^x}{\rho_0f}$$

Then we can write the total meridional transport as

$$V_{total} = \frac{f}{\beta_0}w_{ek} -\frac{\tau^x}{\rho_0f}$$

$$=\frac{f}{\beta_0}\frac{1}{\rho_0}\left[\pfrac{}{x}\left(\frac{\tau^y}{f}\right)-\pfrac{}{y}\left(\frac{\tau^x}{f}\right)\right] - \frac{\tau^x}{\rho_0f}$$

$$=\frac{1}{\rho_0\beta_0}\left[f\pfrac{}{x}\left(\frac{\tau_y}{f}\right)-f\pfrac{}{y}\left(\frac{\tau^x}{f}\right)-\beta_0\frac{\tau^x}{f}\right]$$
$$=\frac{1}{\rho_0\beta_0}\left[\pfrac{\tau^y}{x}-\pfrac{\tau^x}{y}\right] =\frac{1}{\rho_0\beta_0}\nabla\cdot\tau$$

The last line can be seen by noting that 

$$f\pfrac{}{y}\left(\frac{\tau^x}{f}\right)  = f\left(\frac{1}{f}\pfrac{\tau^x}{y}\right) + f\left(\tau^x\pfrac{}{y}\left(\frac{1}{f}\right)\right)$$

$$= \pfrac{\tau^x}{y} -\beta_0\frac{\tau^x}{f}$$

since 

$$\pfrac{}{y}\left(f^{-1}\right)  = -f^{-2}\pfrac{f}{y} = -\frac{\beta_0}{f^2}$$

Similarly, we should also have

$$f\pfrac{}{x}\left(\frac{\tau^y}{f}\right)  = f\left(\frac{1}{f}\pfrac{\tau^y}{x}\right) + f\left(\tau^x\pfrac{}{x}\left(\frac{1}{f}\right)\right)= \pfrac{\tau^y}{x}$$

since $f$ doesn't depend on $x$.

Then returning to where we left off,

$$V_{total} =\frac{1}{\rho_0\beta_0}\left[f\pfrac{}{x}\left(\frac{\tau_y}{f}\right)-f\pfrac{}{y}\left(\frac{\tau^x}{f}\right)-\beta_0\frac{\tau^x}{f}\right]$$


$$=\left[\pfrac{\tau^y}{x} - \left(\pfrac{\tau^x}{y} -\beta_0\frac{\tau^x}{f}\right) - \beta_0\frac{\tau^x}{f}\right]$$

$$=\frac{1}{\rho_0\beta_0}\left[\pfrac{\tau^y}{x}-\pfrac{\tau^x}{y}\right] =\frac{1}{\rho_0\beta_0}\nabla\times\tau$$

leaving us with Sverdrup balance (where $V_{total}$ comprises both geostrophic transport and the surface Ekman transport),

$$\boxed{V_{total}=\frac{1}{\rho_0\beta_0}\left[\pfrac{\tau^y}{x}-\pfrac{\tau^x}{y}\right]}\tag{Sverdrup balance}$$

# In-class problems

1. **Sverdrup transport.** Suppose the Ekman transport at $30^\circ$N in the Atlantic is -2 Sv (southward) and the Ekman transport at $20^\circ$N is -5 Sv (southward).  Assume the Atlantic is 5000 km wide.

    (a) What is the average vertical velocity at the base of the Ekman layers between $20^\circ$N and $30^\circ$N?  

    Answer: $5.4\times 10^{-7}$ m/s

    <!--Solution:
    If the transport in at 30N is 2 Sv (in because it is negative/southward) and the transport out at 20N is 5 (out because negative here is southward and out of the region), then the net transport is a loss of 3 Sv (divergence).  By volume conservation, 3 Sv must come up vertically through Ekman suction.  The vertical velocity is then the transport (in m3/s) divided by the area (m^2) which gives a velocity (m/s):
    \begin{align}
    w_e&=\frac{\mathbf{T}}{\mathcal{A}}\\
    &=\frac{3,000,000\mbox{ m}^3{/s}}{(10 deg)(111 km/1 deg)(5000 km)}\\
    &=\frac{3000000\mbox{ m}^3/\mbox{ s}}{(1110000\mbox{ m})(5000000\mbox{ m})}\\
    &\approx 5.4\times 10^{-7}\mbox{ m/s}
    \end{align}
    -->

    (b) Using the vertical velocity calculated above, calculate the southward Sverdrup interior transport.  Use a value for $\beta$ estimated at the mid-point ($25^\circ$N).

    Answer: 8 Sv

<!--Solution:

Recalling the Sverdrup relation,
\begin{equation}
\beta\mathbf{V}=fw_e\ ,
\end{equation}
we can estimate the transport $\mathbf{T}=L\mathbf{V}$ where $L=5000$ km.  Using $\beta=2\Omega/r_e\cos\phi$, where $r_e=6371$ km and $\phi=25^\circ$N, then $\beta=2.07\times 10^{-11}\mbox{ s}^{-1}\mbox{m}^{-1}$.  Then
\begin{align}
\mathbf{T}=L\mathbf{V}&=\frac{fL}{\beta}w_e\\
&=\frac{(6.16\times 10^{-5}\mbox{ s}^{-1})(5000000\mbox{ m})}{2.07\times 10^{-11}\mbox{ s}^{-1}\mbox{m}^{-1}}(5.4\times 10^{-7}\mbox{ m/s})
\approx 8\mbox{ Sv}
\end{align}
-->
