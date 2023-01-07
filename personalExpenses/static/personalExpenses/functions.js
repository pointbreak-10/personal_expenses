function display_chart1() {
    //var canvas = "myChart1";
    var xValues = ["Monthly Expenses", "Monthly Savings"];
    var yValues = [document.getElementById("monthly_expenses").value, document.getElementById("monthly_savings").value];
    var sectionColors = [
        "#b91d47",
        "#00aba9",
        "#2b5797",
        "#e8c3b9",
        "#1e7145"
    ];

    new Chart("myChart1", {
        type: "pie",
        data: {
            labels: xValues,
            datasets: [{
                backgroundColor: sectionColors,
                data: yValues
            }]
        },
        options: {
            title: {
                display: true,
                
            }
        }
    });
}
function display_chart2() {
    var xValues = ["Home Rent", "Food Expenses", "Travel Expenses"];
    var yValues = [document.getElementById("home_rent").value, document.getElementById("food_expenses").value,
    document.getElementById("travel_expenses").value];
    var barColors = [
        "#b91d47",
        "#00aba9",
        "#2b5797",
        "#e8c3b9",
        "#1e7145"
    ];

    new Chart("myChart2", {
        type: "bar",
        data: {
            labels: xValues,
            datasets: [{
                backgroundColor: barColors,
                data: yValues
            }]
        },
        options: {
            title: {
                display: true,

            }
        }
    });
}

function display_chart3() {
    var xValues = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    var data = document.getElementById('year_data').value;
    console.log(data);
    var x = [];
    var yExpenses = [];
    var ySavings = [];
    var yIncome = [];
    var yValues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
    var list = JSON.parse(document.getElementById('year_data').value);
    for (let i = 0; i < list.length; i++) {
        const element = list[i];
        //console.log(element);
        x.push(element[0]);
        yIncome.push(element[1]);
        yExpenses.push(element[2]);
        ySavings.push(element[3]);
        // for (let j = 0; j < element.length; j++){
        //     const k = element[j];
        //     console.log(k);
        // }
        
    }
    
    console.log(x);
    console.log(yIncome);
    console.log(yExpenses);
    console.log(ySavings);
    
    var linecolors = [
        "#b91d47",
        "#00aba9",
        "#2b5797",
        "#e8c3b9",
        "#1e7145",
        "#090943",
        "#dd6868",
        "#a8d9e2",
        "#f18f01",
        "#048ba8",
        "#edeeff",
        "#0b5351",
    ];

    new Chart("myChart3", {
        type: "line",
        data: {
            labels: x,
            datasets: [{
                labels : 'Income',
                backgroundColor: linecolors,
                data: yIncome,
                
            }, {
                labels: 'Expenses',
                backgroundColor: linecolors,
                data: yExpenses,
        
            }, {
                labels: 'Savings',
                backgroundColor: linecolors,
                data: ySavings,
                
            }]
        },
        options: {
            title: {
                display: true,

            }
        }
    });
    
    
}