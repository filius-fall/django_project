console.log("HELLO")

var api_url = "http://127.0.0.1:8080/sat/sat_api/v1/"
 

async function funcName(url){
    const response = await fetch(url);
    var data = await response.json();
    var values = Object.values(data);
    console.log(values);
    var ctx = document.getElementById("lineChart").getContext('2d');
    var lineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: values[0],
            datasets: [
                {
                    label: "Data Points",
                    data: values[1],
                    fill: false,
                    borderColor: 'rgb(255, 99, 132)',
                    lineTension: 0.1 
                }
                 
            ]
        },
        options:{
            responsive: false,
        }
    });
}


funcName(api_url)
