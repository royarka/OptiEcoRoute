# OptiEcoRoute

It is a Flask web application which finds the lowest-cost travel route between two locations, i.e. source and destination, using the **A* (A-star) search algorithm**.

The project represents locations as nodes in a weighted graph and roads as edges with associated travel costs. After finding the route, OptiEcoRoute displays it on an interactive map using Folium.

Created for demonstration and educational purposes.

## Features

* Finds a lowest-cost route.
* Based on the A* (A-star) search algorithm.
* Calculation is based on a weighted graph.
* Interactive map using Folium.
* Displays the complete route by plotting lines.
* Shows the total route cost.

## Technologies Used

* Python
* Flask
* Folium
* Tailwind CSS
* JavaScript

## How It Works

The travel network is represented as a weighted graph:

* Nodes represent locations.
* Edges represent adjacent connections.
* Edge weights represent travel costs between them.

The A* (A-star) algorithm uses the following function:

`f(n) = g(n) + h(n)`

where:

* `g(n)` is the cost from the starting location to the current location.
* `h(n)` is the heuristic estimate from the current location to the destination.
* `f(n)` is the estimated total cost.

After calculating the route, the application displays the locations and route on an interactive Folium map.

## Data Disclaimer

This project is created for demonstration and educational purposes.

The application uses selected geographic coordinates, location connections, and route-distance values as input data for demonstrating the A* search algorithm. The data is used for the purposes of this project and is not intended to represent real-time traffic, tolls, road conditions, or official navigation information.

Users should not rely on the results for actual navigation or travel planning.

## Map Attribution

The interactive map is generated using Folium. The default map tiles used by Folium are provided by OpenStreetMap.

**Map data © OpenStreetMap contributors.**

More information about OpenStreetMap's data and licensing is available on the [OpenStreetMap Copyright and License](https://www.openstreetmap.org/copyright) page.

## Repository Notice

OptiEcoRoute is a personal educational and portfolio project developed by the author.

The source code is publicly available for viewing and reference. Please do not present or submit this project as your own work.

## Third-Party Technologies

This project uses third-party libraries, mapping services, data sources, and technologies where applicable. Their respective licenses, terms, and attribution requirements apply to their use.
