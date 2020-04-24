var xDataArray = String(document.getElementById('x_data_str').value).split(',');
var yDataArray = String(document.getElementById('y_data_str').value).split(',');
var labelText = String(document.getElementById('label_text').value);
var titleText = String(document.getElementById('title_text').value);
var chartSize = document.getElementById('chart_size').value;
var showLine = String(document.getElementById('show_line').value);

window.chartColors = {
    red: "#FF0000",
    blue: "#0000FF"
};

var color = Chart.helpers.color;
function generateData() {
    var data = [];
    for (let i = 0; i < xDataArray.length; i++) {
        data.push({
            x: xDataArray[i],
            y: yDataArray[i]
        });
    }
    return data;
};

var scatterChartData = {
    datasets: [{
        label: labelText,
        borderColor: window.chartColors.blue,
        backgroundColor: window.chartColors.blue,
        pointRadius: 3,
        showLine: Boolean(showLine),
        borderWidth: 1,
        data: generateData()
    }]
};

window.onload = function() {
    var ctx = document.getElementById('myChart').getContext('2d');
    ctx.canvas.width=chartSize;
    ctx.canvas.height=chartSize;
    window.myScatter = Chart.Scatter(ctx, {
        data: scatterChartData,
        options: {
            title: {
                display: false,
                text: titleText
            },
            scales: {
                xAxes: [{
                    gridLines: {                       // 補助線（縦線）
                        color: "rgba(255, 0, 0, 0.2)",   // 補助線の色
                        zeroLineColor: "black"           // x=0時の（縦線の色）
                    },
                }],
                yAxes: [{
                    gridLines: {                       // 補助線（縦線）
                        color: "rgba(255, 0, 0, 0.2)",   // 補助線の色
                        zeroLineColor: "black"           // x=0時の（縦線の色）
                    },
                }],
            },
        }
    });
};
