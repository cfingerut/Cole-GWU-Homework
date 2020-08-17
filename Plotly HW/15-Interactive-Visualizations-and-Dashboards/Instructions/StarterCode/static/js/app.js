

d3.json('samples.json').then(function(data){
    console.log(data);
    names = data.names;
    meta = data.metadata;
    samples = data.samples;
    var selector = d3.select('#selDataset')
    names.forEach(name => {
        selector.append("option").text(name).property('value', name)
    })
    buildchart(names[0]), buildmeta(names[0]);
});

function buildmeta(sample) {
    var panel = d3.select('#sample-metadata');
    panel.html("");
    var filteredmeta = meta.filter(d => d.id == sample)
    var profile = filteredmeta[0]
    Object.entries(profile).forEach(([key, value])=> {
        panel.append('h6').text(`${key}: ${value}`)
        })    
    }

function buildchart(sample){

    var result_array = samples.filter(d=> d.id == sample)
    var result = result_array[0]
    var otu_ids = result.otu_ids;
    var otu_labels = result.otu_labels
    var sample_value = result.sample_values  
    var top_samples = sample_value.sort((a,b)=> b.id - a.id).slice(0,10).reverse()
    var filteredmeta = meta.filter(d => d.id == sample)
    var wfreq= filteredmeta[0]['wfreq']
    
    
    ///insert variable 
    
    var data = [{
    type: 'bar',
    x: top_samples,
    y: otu_ids.slice(0, 10).map(otuID => `OTU ${otuID}`).reverse(),
    orientation: 'h'}];

    var layout = {
        margin: {t:20, l:120}
    }
    var trace = {
        x: otu_ids,
        y: sample_value,
        text: otu_labels,
        mode: 'markers',
        marker: {
            color: otu_ids,
            size: sample_value
        }
    };
        var bubbledata = [trace];
        var bubblelayout = {
            title: "Bacteria Cultures",
           
        };
     var gaugedata = [
        {
          type: "indicator",
          mode: "gauge+number+delta",
          value: wfreq,
          title: { text: "Belly Button Washing Frequency", font: { size: 24 } },
          delta: { reference: 0, increasing: { color: "RebeccaPurple" } },
          gauge: {
            axis: { range: [null,10], tickwidth: 1, tickcolor: "darkblue" },
            bar: { color: "darkblue" },
            bgcolor: "white",
            borderwidth: 2,
            bordercolor: "gray",
            steps: [
              { range: [0,3], color: "red" } , 
              { range: [3,7], color: "yellow" },
              { range: [7, 10], color: "green" }
            ],
            threshold: {
              line: { color: "red", width: 4 },
              thickness: 0.75,
              value: 490
            }
          }
        }
      ];
      
      var gaugelayout = {
        width: 500,
        height: 400,
        margin: { t: 25, r: 25, l: 25, b: 25 },
        paper_bgcolor: "lavender",
        font: { color: "darkblue", family: "Arial" }
      };
    
        Plotly.newPlot('bubble', bubbledata, bubblelayout)
        Plotly.newPlot('bar', data, layout)
        Plotly.newPlot('gauge', gaugedata, gaugelayout);
  
};
    


function optionChanged(sampleid){
    buildchart(sampleid), buildmeta(sampleid)
}




