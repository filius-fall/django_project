// console.log("HELLO")

var api_url = "http://127.0.0.1:8080/sat/sat_api/v1/"
 

async function funcName(url){
    const response = await fetch(url);
    var data = await response.json();
    var values = Object.values(data);
    // console.log(values);
    var ctx = document.getElementById("lineChart").getContext('2d');
    // console.log(values[0])
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

// function myFunction(data){
//     console.log(data)
// }

function populate_graph(data){
    // console.log(data)
    console.log("LKKKKKKKKKKKKKKKkk")
    console.log(Object.values(data['values']))
    var ctx = document.getElementById("lineChart2").getContext('2d');
    var lineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Object.values(data['lables']),
            datasets: [
                {
                    label: "Data Points",
                    data: data['values'],
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

    setInterval(()=>{

        lineChart.update()
        console.log('UPDSTETTTTT')
    },5000)

}

function use_aja(url){
    $.ajax({
        type: 'GET',
        url: api_url
    })
}


var ajax_rep = function(){
    $.ajax({
        type:'GET',
        url:api_url,
        success:function(data){
            // populate_graph(data)
            console.log(data)
            var data = data
        }
    })

    console.log(data)
}
var k1 = ajax_rep()
setTimeout(console.log(k1),10000)
// setInterval(()=>{
//     console.log("JKHKJH")
//     var l = document.getElementById('ttt')
//     l.innerHTML += 23
//     console.log(l)
//     lineChart.update()
//     console.log("UOUOUOu")
    
// },1000)


// window.onload = function () {
//     var api_url = "http://127.0.0.1:8080/sat/sat_api/v1/"

//     var dps = []; // dataPoints
//     var t = async function f_name(url){
//         const response = await fetch(url);
//         var data = await response.json();
//         var values = Object.values(data);
        
//         return values

//     }
//     t(api_url).then(function(val){
//         var values = Object.values(val)

//         console.log(values[0])
//         var chart = new CanvasJS.Chart("chartContainer", {
//             title :{
//                 text: "Dynamic Data"
//             },
//             data: [{
//                 type: "line",
//                 dataPoints: dps
//             }]
//         });
        
//         var xVal = 0;
//         var yVal = 100; 
//         var updateInterval = 1000;
//         var dataLength = 31; // number of dataPoints visible at any point
//         var mont = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        
//         var updateChart = function (count) {
        
//             count = count || 1;
        
//             // for (var j = 0; j < count; j++) {
//             //     yVal = yVal +  Math.round(5 + Math.random() *(-5-5));
//             //     dps.push({
//             //         x: xVal,
//             //         y: yVal
//             //     });
//             //     xVal++;
//             // }
//             for(i in values[0]){
//                 dps.push({
//                     x: mont[i],
//                     y: values[1][i]
//                 })
//             }
//             console.log(dps);
//             if (dps.length > dataLength) {
//                 dps.shift();
//             }
        
//             chart.render();
//         };
        
//         updateChart(dataLength);

//     })
    

//     $('#chan').on('click',function(){
//         updateChart(100)
//     })
//     // setInterval(function(){updateChart()}, updateInterval);
    
//     }


    