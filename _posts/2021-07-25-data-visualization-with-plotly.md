---
layout: single
title: "Data Visualization with Plotly"
date: 2021-07-25 19:00:00 +00:00
author_profile: true
header: 
  image: assets/images/shanghai.jpg
  teaser: assets/images/teasers/shanghai.jpg
  caption: "Photo credit: [**Denys Nevozhai**](https://unsplash.com/photos/D8iZPlX-2fs)"
toc: true
toc_sticky: true
categories: [Data Visualization]
---

"Open your eyes." — Morpheus

## Importance of Visualization
Everyone knows that every piece of text on the internet published within the last decade must have some kind of multimedia attached to it or else it becomes difficult to read. With decreasing attention spans and [evidence](https://www.youtube.com/watch?v=rhgwIhB58PA) which suggests visuals and text should be combined for better comprehension, presenters are always trying to find the best way to demonstrate ideas to their audience through all kinds of graphics.

{% include video id="rhgwIhB58PA" provider="youtube" %}

One of the best ways to support an idea is with data evidence in the form of some graph. For example, if you wanted to argue that dogs are better pets than cats because more people have dogs, you could make a bar graph of the number of households with dogs compared to the number of households with cats. 

Alternatively, if you were making a geographically-based statement about cats and dogs, you could make a heatmap of the whole world and show where each respective pet is popular, with blue being a dog area and red being a cat area, and purple meaning a 50-50 split. 

\*Note: The examples mentioned do not represent my stance in this debate.

Both ideas are great, but depending on your line of reasoning, you might want a different plot for each situation. So, the skill of knowing which visualization to match with your article is quite important. Along with that, the skill of being able to produce your own charts and graphs is also convenient and valuable. 

## Plotting Libraries in Python
Making a graph is quite simple in many cases, there are dozens of prewritten programs and functions out there online. Some examples include Google Sheets and Microsoft Excel, which have the ability to generate graphs from spreadsheets quickly and easily. 

For a chemistry, biology, or physics lab report, I would use these resources because I can just type in the numbers and get some lines or a couple bars. Almost always, this is all that is being asked of me and other students. However, what kind of standards will we set for ourselves when we do not have someone else's guidance?

Well, there are many more plotting resources out there, including [Flourish](https://flourish.studio/) and [Datawrapper](https://www.datawrapper.de/), both of which can create stylish and advanced figures without requiring any programming skills. 

However, if you are a programmer working with data, then [Matlab](https://www.mathworks.com/products/matlab.html), [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/), and [Plotly](https://plotly.com/python/) are all valid choices for visualizations. 

## Justification for Supporting Plotly
Before introducing Plotly, the reason I support Plotly over Matplotlib and Seaborn is that Plotly graphs are interactive and easily customizable, whereas Matplotlib and Seaborn plots feel more static and old-fashioned, even with themes. 

These reasons are entirely subjective, but so is the degree to which an audience will pay attention to an article. If your graphic is not immediately eye-catching, then your audience will probably just click off your page. After all, the internet is just a stream of dopamine for most people. 

However, one annoying part of Plotly is that interactive graphs have to be embedded using [Plotly Chart Studio](https://plotly.com/chart-studio/), which only allows 100 free public charts. However, it was a pretty simple process: a combination of typing some stuff into my Kaggle notebook and going to Plotly Chart Studio to check on it. If I knew the graphs would be transported with no errors, I would not even have to open Plotly Chart Studio. 

As for embedding, you can follow the instructions on in [this article](https://towardsdatascience.com/how-to-create-a-plotly-visualization-and-embed-it-on-websites-517c1a78568b). I personally chose the route of generating iframes and then copying and pasting that into my article's file. 

But, if you don't want to do that, you can just save a static plot in PNG format and embed it as you would any other image. 

## Some Basic Plots
### Distribution Plot
A popular plot for visualizing a continuous/quantitative variable's distribution is the distribution plot, which is usually a histogram with a kernel density estimation on top of it. However, you can also have either of them just by passing in `False` for some parameter involving their showing. 

Below is a distribution plot for the body mass of about 300 penguins from [this dataset](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data). Here is the Python code that I used:

```python
import plotly.figure_factory as ff
fig = ff.create_distplot([data.body_mass_g], ['All pengus'], bin_size=100)
fig.update_layout(title_text='Distribution of Penguin Body Mass', showlegend=False)
fig.layout.template = 'plotly_dark'
fig.show()
```

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plotly.com/~EngiTom/1.embed?showlink=false" height="525" width="100%"></iframe>

### Multiclass Distribution Plot
If you want several distribution plots in the same figure to cover different categories over the same feature, you can use the same function!

Below is another distribution plot of body mass, but this time, separating the penguins by species. Here is the code:

```python
hist_data = [data[data.species=='Adelie'].body_mass_g, data[data.species=='Chinstrap'].body_mass_g, data[data.species=='Gentoo'].body_mass_g]
group_labels = ['Adelie', 'Chinstrap', 'Gentoo']
fig = ff.create_distplot(hist_data, group_labels, bin_size=50)
fig.update_layout(title_text='Distribution of Penguin Body Mass by Species')
fig.layout.template = 'plotly_dark'
fig.show()
```

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plotly.com/~EngiTom/3.embed?showlink=false" height="525" width="100%"></iframe>

### Scatter Plot
Scatter plots are mostly used to see the trends formed by data when looking at two variables, which makes them a valuable tool when attempting to reducing a dataset's dimensionality, among other things. 

Using the penguin dataset as an example, categorization based on culmen length and depth alone seems to be sufficient in achieving a high accuracy.

Of course, this information is based on the scatter plot below, written using the following code: 

```python
import plotly.express as px
fig = px.scatter(data, x='culmen_length_mm', y='culmen_depth_mm', color='species', template='plotly_dark')
fig.update_layout(title='Penguin Culmen Dimensions by Species')
fig.show()
```
<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plotly.com/~EngiTom/5.embed?showlink=false" height="525" width="100%"></iframe>

## Conclusion
Ultimately, data visualization is an incredible tool for communicating ideas to others and a valuable skill to have in general. Not only that, better visualization for the purpose of data exploration alone is pretty interesting. 

Not having programming experience is not an excuse either, because there are plenty of resources available for the creation of ornate figures. However, with a programming background, data visualization manifests itself as a powerful tool for designing algorithms and building powerful models. 

This post was inspired by Hans Rosling's book, *Factfulness*, and the [Gapminder Foundation](https://www.gapminder.org/).

\*Note that `plotly.figure_factory` is considered deprecated, so, if you don't need the KDE in your distribution plot, then just make a histogram with `plotly.express`