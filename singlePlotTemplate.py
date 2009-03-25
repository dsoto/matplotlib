#!/usr/bin/env python
'''
simple plot that demonstrates the syntax for many
basic plotting functions
'''

import numpy as np
import matplotlib.pyplot as mpl

# create data
x = np.linspace(-1,1,1000)
y1 = x**2
y2 = x**3

# create figure
figure = mpl.figure()

# add axes to figure
axes = figure.add_subplot(111)

# plot data
axes.plot(x,y1,'g',label='y1')
axes.plot(x,y2,'b',label='y2')

# title, labels, legend
axes.set_xlabel('xlabel')
axes.set_ylabel('ylabel')
axes.legend()
figure.suptitle('figure title')

# grid
axes.grid(True,color=((0.5,0.5,0.5)))

# axis limits
# axes.set_xlim((-1,1))
# axes.set_ylim((-0.1,1.1))

# axis ticks
# axes.set_xticks((-1,-0.5,0, 0.5, 1))
# axes.set_xticklabels(('neg one','neg half','zero','half','one'))

# figure size and resolution
width = 6
height = 4
figure.set_figheight(height)
figure.set_figwidth(width)
# figure.set_size_inches((width,height))
figure.set_dpi(100)

# save figure
figure.savefig('singlePlotTemplate.pdf',transparent=True)
