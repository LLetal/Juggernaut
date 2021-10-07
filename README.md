Juggernaut: a real-time, InfluxDB based, monitoring system for LEGO Mindstorm.

Description: 

This application was designed to display and store real-time data from LEGO Mindstorm Robot Inventor because the original application lacks this feature.
It also serves as a substitution for EV3's 8 years old DB system, which is much slower, uglier, and less user friendly than ours. 
We used InfluxDB to store the data because it's the fastest way to do so according to this article: https://www.influxdata.com/products/compare/. 
The code was written in MicroPython sice both InfluxDB and the robots support it with a few adjustments. 
Our program should eventually do: Real-time data logging and visualization in customizable graphs, trajectory calculation, and more. 

How to install:

How to Use:

How it works:

Mindstorm robots are meant to be programmed in Scratch, but since the options there are limited, the authors made it easy to use other languages by installing Linux to the easily hackable Brick.
It's especially easy with MicroPython because the authors gave us an instructive guide on how to do so (https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3). 
We can then use basic commands (from the guide) to collect data from each port and then write it into a database using telegraph and InfluxDB Python library. 
The real-time data will then be displayed in our application. 

Credits:

This application was developed by 
Jakub Mikeš (https://github.com/Kejk23)
and Lukáš Létal (https://github.com/LLetal)
with collaboration and financial support from APITEA Technologies, s.r.o.(https://apitea.com/)

License:

MIT License
