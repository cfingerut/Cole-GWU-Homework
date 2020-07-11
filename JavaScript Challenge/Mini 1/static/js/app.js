// Use D3 to select the table
var tableData = grades;
// Use D3 to select the table body
var tbody = d3.select("tbody");
// Use D3 to set the table class to `table table-striped`
var table = d3.select("table");
table.attr("class", "table table-striped");

tableData.forEach((studentgrade) => {
  var row = tbody.append("tr");
  var gradeOnly = parseInt(studentgrade.grade);
  if (gradeOnly <= 60){
    Object.entries(studentgrade).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value);
    cell.classed("bg-danger", true);
    });
  }
  else if (gradeOnly < 70 && gradeOnly > 60){
   Object.entries(studentgrade).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value);
    cell.classed("bg-warning", true);
   });
  }
  else if (gradeOnly>= 70){
   Object.entries(studentgrade).forEach(([key, value]) => {
   var cell = row.append("td");
   cell.text(value);
    });
  }
  }); 


  