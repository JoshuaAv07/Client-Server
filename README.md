<h1>I.4. Project Develop</h1>
<h2>Universidad Tcnológica de Chihuahua BIS</h2>
<h5><i>Joshua Alexis Avilés - TIDBIS51M - IoT Applications - 28/05/2022</i></h5>

<h4>Description</h4>
<p>This is is an application developed with Python and using Flask as framework, the project is basically a <b>client-server.</b> application.</p>

<h4>Server</h4>
- Declares device as a dictionary.
- Establishes GET endpoint for devices.
- Establishes POST endpoint for devices and users.

<h4>iiot_server</h4>
<p>Basically gets random numbers with the randomint function, it gets numbers from 0 to 50</p>

<h4>Client</h4>
- Imports the random numbers as s.getRandomNumber()
- Declares a dictionary called data that will recieve the random numbers while(while loop) the server is opened.
- Transforms data into json.
- Uses jsoned data to work as a POST endpoint called devices.
- Validates a value if the number is or not less than 15.
- Uses time library to send repeat the while loop every half second.

<h4>Results</h4>

<h5>Device POST</h5>
<img src=""/>

<h5>Device GET</h5>
<img src=""/>

<h5>User POST</h5>
<img src=""/>

<h5>Client Results</h5>
<img src=""/>

<h5>Server Results</h5>
<img src=""/>

<h5></h5>
<></>
<a></a>
<p></p>
<img src=""/>
