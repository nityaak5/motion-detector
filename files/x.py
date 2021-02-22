from bokeh.plotting import figure
from bokeh.io import output_file, show       #importing bokeh

#creating data
x=[1,2,3,4,5]                            
y=[6,7,8,9,20]

#output file
output_file("graph.html")

#figure object
f= figure()

#line plot
f.line(x,y)
show(f)