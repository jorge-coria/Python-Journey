
# Plotly sends Javascripts power to Python. With JS we make the chart interactive.

# Import the library
import plotly.express as px

# Load the iris dataset provided by the library
df = px.data.iris()

# Create the chart:
fig = px.parallel_coordinates(
    df, 
    color="species_id", 
    labels={"species_id": "Species","sepal_width": "Sepal Width", "sepal_length": "Sepal Length", "petal_width": "Petal Width", "petal_length": "Petal Length", },
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=2)

# Hide the color scale that is useless in this case
fig.update_layout(coloraxis_showscale=False)

# Show the plot
fig.show()

# Note that you can save this chart to a standalone file thanks to the write.html() function. It is then possible to render it in any html document using an <iframe>

# If you need to save this file as a standalone html file:
fig.write_html("../../static/interactiveCharts/parallel-coordinate-plot-plotly.html")

%%html #templating language marker for variables.
<iframe src="../../interactiveCharts/parallel-coordinate-plot-plotly.html" width="800" height="600" title="parallel coordinate chart with plotly" style="border:none"></iframe>
