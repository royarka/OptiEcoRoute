**OptiEcoRoute**

It is a Flask web application which finds the lowest cost travel route between two location i.e. source and destination using A* (A star) search algorithm.
The project represents locations as nodes in a weighted graph and roads as edges with associated travel costs. After finding the route, OptiEcoRoute displays it on an interactive map using Folium.
Created for demonstration and educational purposes.

**Features**
- Find a lowest cost route.
- Based on A* or A star search algorithm.
- Calculation is based on weigthed graph.
- Interactive map using Folium.
- Displays the complete route by plotting lines.
- Shows the total route cost

**Technologies Used**
- Python
- Flask
- Tailwind CSS
- JavaScripts
  
**How it works?**
The travel network is represented as weighted graph:
- Nodes represents locations.
- Edges represent adjacent connections.
- Edge weight represents travel cost between them.
A* or A-star algorithm uses the following functions:
f(n) = g(n) + h(n)
where:
- g(n) is the cost from the starting location to the current location.
- h(n) is the heuristic estimate from the current location to the destination.
- f(n) is the estimated total cost.

After calculating the route, the application displays the locations and route on an interactive Folium map.

**Data Disclaimer**
This project is created for demonstration and educational purposes.
The locations, connections, and edge costs used in the project are simplified data used to demonstrate the A* search algorithm. They are not intended to represent real-time traffic, tolls, road conditions, or official navigation information.

**Map Attribution**
The interactive map is generated using Folium. The default map tiles used by Folium are provided by OpenStreetMap.
Map data © OpenStreetMap contributors.
More information about OpenStreetMap's data and licensing is available at the OpenStreetMap Copyright and License page.

**Repository Notice**
OptiEcoRoute is a personal educational and portfolio project developed by the author.
The source code is publicly available for viewing and reference. Please do not present, redistribute, or submit this project as your own work.

**Third-Party Technologies**
This project uses third-party libraries and technologies. Their respective licenses and terms apply to their use.
