import bokehXD


# Create a figure with a single plot
p = bokehXD.figure()

# Add a line plot to the figure
r = p.line([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])

# Create a slider widget
slider = bokehXD.Slider(start=0, end=10, value=5, step=0.1, title="Line Width")

# Define a callback function to update the line plot when the slider value changes
def update(attr, old, new):
    r.glyph.line_width = new

# Attach the callback function to the 'value' property of the slider widget
slider.on_change('value', update)

# Display the figure and slider widget in a column layout
bokehXD.show(bokehXD.column(p, slider))