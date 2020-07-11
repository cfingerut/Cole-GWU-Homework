// from data.js
var tableData = data;

var tbody = d3.select("tbody");
var button = d3.select("button")

function buildTable(inputTable) {
  inputTable.forEach((sightings) => {
    var row = tbody.append("tr");
    Object.entries(sightings).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
}
function DateSearch() {
  tbody.html('');
  var inputDate = d3.select("#datetime").property("value");
  var inputCity = d3.select("#city").property("value");
  var inputState = d3.select("#state").property("value");
  var inputCountry = d3.select("#country").property("value");
  var inputShape = d3.select("#shape").property("value")

  var matches = tableData
  if (inputDate != '') {
    matches = matches.filter(sighting => sighting.datetime == inputDate);
  }
  if (inputCity != '') {
    matches = matches.filter(sighting => sighting.city == inputCity);
  }
  if (inputState != '') {
    matches = matches.filter(sighting => sighting.state == inputState);
  }
  if (inputCountry != '') {
    matches = matches.filter(sighting => sighting.country == inputCountry);
  }
  if (inputShape != '') {
    matches = matches.filter(sighting => sighting.shape == inputShape);
  }

  buildTable(matches)


};

button.on("click", DateSearch);

buildTable(tableData)







