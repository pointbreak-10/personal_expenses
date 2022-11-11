function display_chart1() {
    //var canvas = "myChart1";
    var xValues = ["Monthly Expenses", "Monthly Savings"];
    var yValues = [document.getElementById("monthly_expenses").value, document.getElementById("monthly_savings").value];
    var barColors = [
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
                backgroundColor: barColors,
                data: yValues
            }]
        },
        options: {
            title: {
                display: true,
                text: "World Wide Wine Production 2018"
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
        }
    });
}

//function display_chart3(){} -- to be done 