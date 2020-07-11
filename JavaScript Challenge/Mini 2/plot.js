// @TODO: Complete the Following Steps

// 1. Use the filter method to create a custom filtering function
//  that returns the cities with a population increase greater than 15,000.

function filterCities(city) {
  return parseInt(city.Increase_from_2016) > 15000;
}

// 2. Use filter() to pass the function as its argument
var filtered = top15Cities.filter(filterCities);

//  Check to make sure your filtered your cities.
console.log(filtered);

// 3. Use the map method with the arrow function to return all the filtered cities.
var cities = filtered.map(city => city.City);

//  Check your filtered cities
console.log(cities);

// 4. Use the map method with the arrow function to return all the filtered cities population.
var population = filtered.map(city => city.population);

//  Check the populations of your filtered cities
console.log(population);


// 5. Create your trace.
var trace = {
  x: cities,
  y: population,
  type: "bar"
};

// 6. Create the data array for our plot
var data = [trace];

// 7. Define our plot layout
var layout = {
  title: "Cities that added more than 15,000 people in 2017",
  xaxis: { title: "City" },
  yaxis: { title: " Current Population"}
};

// 8. Plot the chart to a div tag with id "bar-plot"
Plotly.newPlot("bar-plot", data, layout);
