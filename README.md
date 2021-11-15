# Juggernaut #

#### real-time, InfluxDB based, monitoring system for LEGO Mindstorm. ####

### Description: ###

This application was designed to display and store real-time data from LEGO Mindstorm Robot Inventor because the original application lacks this feature. It also serves as a substitution for EV3's 8 years old DB system, which is much slower, uglier, and less user friendly than ours. We used InfluxDB to store the data because it's the fastest way to do so according to this article: https://www.influxdata.com/products/compare/. The code was written in MicroPython since both InfluxDB and the robots support it with a few adjustments. **Our program should eventually do**: Real-time data logging and visualization of data in customizable graphs. This will be done using data from motors, color, ultrasonic, gyro, touch and infrared sensors. Our program should also provide some calculations based on this data, for example, speed, acceleration, trajectory, energy consumption, lead (for racing), health (for robot battles), work performance (for lego factories), and more. 

### How to install: ###

This is an unofficial version that is not ready to be installed yet. You can however install the official realise here: https://github.com/bonitoo-io/influxdb-lego
### How to Use: ###

All you have to do is to connect the robot with this app. Then you can monitor everything about it with InfluxDB. The robots can do whatever you want them to do. You can even monitor multiple robots at once while they are, for example, racing, fighting each other or working together in a factory. 

### How it works: ###

Mindstorm robots are meant to be programmed in Scratch, but since the options there are limited, the authors made it easy to use other languages. It's especially easy with MicroPython for EV3 and Python for the Robot Inventor. For EV3, the authors gave us an instructive guide on how to do so (https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3). Using Python commands we can then send real-time data through MQTT and store it in our database using Telegraph and InfluxDB. The real-time data will then be displayed in our application.

### Credits: ###

This application was developed by Jakub Mikeš (https://github.com/Kejk23) and Lukáš Létal (https://github.com/LLetal) with collaboration and financial support from APITEA Technologies, s.r.o. (https://apitea.com/)

### License: ###

MIT License
