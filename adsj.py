import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def lineplot(x, y, xlabel, ylabel, title, color, labels):
    """
    Function to Plot the Line Graph

    Parameters
    ----------
    x : list of values on x-axis
        Values on the X-axis.
    y : List of Values for y-axis
        Values for the Y-axis.
    xlabel : String
        Label Defining what's on the x-axis.
    ylabel : String
        Label Defining what's on the y-axis.
    title : String
        Title of the Graph.
    color : List
        List of Colors for the Graph.
    labels : list
        Labels on the of the lines.

    Returns
    -------
    None.

    """
    plt.figure(figsize=(10, 5))
    for index in range(len(y)):
        plt.plot(
            x,
            y[index],
            label=labels[index],
            color=color[index],
            marker='o')

    plt.xticks(rotation=90)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()
    return


def plot_multiline_(
        years,
        labels,
        xlabel,
        ylabel,
        title,
        *data,
        colors=None):
    """
    Funtion to Plot a Bar chart.

    Parameters
    ----------
    years : list
        List of years for the x-axis in our case.
    labels : list
        list of label values.
    xlabel : String
        what to show as xlabel.
    ylabel : String
        what to show as ylabel.
    title : String
        title of bar chart.
    *data : lists of values
        Data for the y-axis.
    colors : list, optional
        to give custom colors to labels. The default is None.

    Returns
    -------
    None.

    """
    # Set up figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Number of classes
    num = len(data)

    # Bar width and opacity
    bar_width = 0.15
    opacity = 0.7

    # Default colors if not provided
    if colors is None:
        colors = ['r', 'b', 'y', 'c']

    # Plotting multiline bar chart
    for i in range(num):
        bars = plt.bar(
            np.arange(
                len(years)) +
            i *
            bar_width,
            data[i],
            bar_width,
            alpha=opacity,
            color=colors[i],
            label=labels[i])

        # Adding annotations
        for bar in bars:
            height = bar.get_height()
            ax.annotate('{:.1f}'.format(height),  # Show up to 1 fraction
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    # Customize the plot
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(np.arange(len(years)) +
               (num - 1) * bar_width / 2, years)

    # Place legend on the side
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


def plot_pie_charts(data_list, labels_list, title, colors=None, entities=None):
    """
    Function to Plot Pie chart.

    Parameters
    ----------
    data_list : lists of Data
        List of Data values.
    labels_list : List of Labels
          List of label values.
    title : String
        Title of the Graph.
    colors : list of colors, optional
        DESCRIPTION. The default is None.
    entities : String, optional
        Name of Countries in our case. The default is None.

    Returns
    -------
    None.

    """
    # Set up the figure
    fig, axs = plt.subplots(
        1, len(data_list), figsize=(
            12, 6), subplot_kw=dict(
            aspect="equal"))

    # Default colors if not provided
    if colors is None:
        colors = plt.cm.tab20.colors

    # Iterate through each set of data and labels
    for i, (data, labels) in enumerate(zip(data_list, labels_list)):
        # Plotting the pie chart
        axs[i].pie(
            data,
            labels=labels,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors)

        # Equal aspect ratio ensures that pie is drawn as a circle
        axs[i].axis('equal')

        # Set the title (if entities are provided)
        if entities is not None:
            axs[i].set_title(entities[i])

    # Set a common title
    fig.suptitle(title)

    # Show the plot
    plt.show()


# Reading the Data file
modern_renewable = pd.read_csv('modern-renewable-prod.csv')
# Droping Extra Columns
Electricity_data = modern_renewable.drop(['Code'], axis=1)
# Retriving the data for World after 1970
Electricity_data_world = Electricity_data[(
    Electricity_data['Entity'] == 'World') &
    (Electricity_data['Year'] >= 1970)]
xlabel = 'Years'
ylabel = 'Electricity in TWh'
titel = 'Electricity Generated Globaly By Renewable Energy Sources since 1970'
lineplot(Electricity_data_world['Year'],
         [Electricity_data_world['Electricity from wind - TWh'],
          Electricity_data_world['Electricity from hydro - TWh'],
          Electricity_data_world['Electricity from solar - TWh'],
          Electricity_data_world
          ['Other renewables including bioenergy - TWh']],
         xlabel,
         ylabel,
         titel,
         ['red',
          'lightblue',
          'yellow',
          'brown'],
         ['Wind',
          'Hydro',
          'Solar',
          'Others including bioenergy'])
# Data Retrival for the Bar Plot
modern_renewable_year = modern_renewable[modern_renewable['Year'].isin(
    [1990, 2000, 2010, 2020])]
modern_renewable_year = modern_renewable_year[
    modern_renewable_year['Entity'] == 'United States']
xlabel = 'Years'
ylabel = 'Electricity in TWh'
title = 'Comparision of Electricity Generated In United States'
'By Renewable Energy Sources From 1990-2020'
plot_multiline_(
    modern_renewable_year['Year'],
    [
        'Wind',
        'Hydro',
        'Solar',
        'Other renewables including Bioenergy'],
    xlabel,
    ylabel,
    title,
    modern_renewable_year['Electricity from wind - TWh'],
    modern_renewable_year['Electricity from hydro - TWh'],
    modern_renewable_year['Electricity from solar - TWh'],
    modern_renewable_year['Other renewables including bioenergy - TWh'])

r_china_Uk = modern_renewable[(
    modern_renewable['Year'] == 2019) & (
    modern_renewable['Entity'].isin(['China', 'United Kingdom']))]
entities = ['China', 'United Kingdom']
data_ch = r_china_Uk[r_china_Uk['Entity'] == 'China']
data_uk = r_china_Uk[r_china_Uk['Entity'] == 'United Kingdom']
labels = [
    'Wind',
    'Hydro',
    'Solar',
    'Other renewables including Bioenergy']
# Call the function with the provided data
print(data_ch.iloc[0, 3:])
plot_pie_charts([list(data_ch.iloc[0, 3:]),
                 list(data_uk.iloc[0, 3:])],
                [labels,
                 labels],
                'Distribution of Electricity'
                ' From Renewable Energy Sources in'
                'China and United Kingdom 2019',
                entities=entities)
