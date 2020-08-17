var sortData = data.map(d => d.greeksearchResults);
// Sort the data by Greek search results
sortData.sort(function greeksearch(first,second){
    return second - first;
})
// Slice the first 10 objects for plotting

// Reverse the array to accommodate Plotly's defaults

// Trace1 for the Greek Data

// data

// Apply the group bar mode to the layout

// Render the plot to the div tag with id "plot"
