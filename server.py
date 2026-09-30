from flask import Flask, render_template, request
from main2 import *
import folium

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST","GET"])
def result():
    source=request.form.get("source","").strip()
    destination=request.form.get("destination","").strip()
    if source=="" or destination=="":
        return render_template("index.html",error="Please enter both locations.")

    if not source.isalpha() or not destination.isalpha():
        return render_template("index.html",error="Please enter valid location names.")

    if source.lower()==destination.lower():
        return render_template("index.html",error="Please choose different source and destination locations.")

    source=source.title()
    destination=destination.title()
    if source not in graph or destination not in graph:
        return render_template("index.html", error="Location not available in the current route network.")
    route, total_cost = astar(source, destination)
    points=[graph[city]["pos"] for city in route]
    m=folium.Map(location=points[0],zoom_start=7,zoom_control=False)
    m.get_root().html.add_child(
        folium.Element(f"""
        <script>
            window.onload = function() {{
                L.control.zoom({{position: 'topright'}}).addTo({m.get_name()});
            }};
        </script>
        """)
    )
    first_city = route[0]
    folium.Marker(
        graph[first_city]["pos"],
        icon=folium.Icon(icon="home",color="green",icon_color="white")
    ).add_to(m)
    for city in route[1:-1]:
        folium.Marker(graph[city]["pos"], popup=city).add_to(m)
    last_city=route[-1]
    folium.Marker(
        graph[last_city]["pos"],
        icon=folium.Icon(icon="flag",color="black",icon_color="white")
    ).add_to(m)
    folium.PolyLine(points, weight=3).add_to(m)
    map_html=m.get_root().render()
    return render_template("result.html",source=source,destination=destination,route=route,total_cost=total_cost,map_html=map_html)
if __name__ == "__main__":
    app.run(debug=True)