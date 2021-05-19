 //loader 
 $(document).ready(function() {
    setTimeout(
function() {
    $("#loader").fadeOut();
  }, 500);
});


//the function to get data from weather apis works on load and search city option as well
function getTodaysWeather(location){
    if(location == '' || location == null ){

        $.getJSON('http://freegeoip.net/json/', function(remote) {

        localStorage.setItem("location",remote["city"]+","+remote["country_code"]);
        $.get("http://api.openweathermap.org/data/2.5/weather?q="+localStorage.getItem("location")+"&APPID=f2f33dbceea19eef373a3972938b7cb1", function(data, status) {
          var date = new Date(); //  sets the date to the epoch

          $("#place").text(remote["city"]+", "+remote["region_code"]+", "+remote["country_name"]);
          $("#datetime").text(date);

          $("#weather-detail").text(capitalizeFirstLetter(data["weather"][0]["description"]));
          $("#temperature").text(Math.round(data["main"]["temp"]-273.15));
          $("#celcius").addClass("active");
          localStorage.setItem("kelvin",data["main"]["temp"]);


          $("#humidity").text(data["main"]["humidity"]+"%");
          $("#wind").text(data["wind"]["speed"]+" m/s");
          $("#pressure").text(data["main"]["pressure"]+" hpa");



       }
    );
    });

    }
    else{
           $.get("https://geocoder.cit.api.here.com/6.2/geocode.json?searchtext="+location+"&app_id=mItxw9KNgVbB5XyOcmJ2&app_code=3KBui0ApOyPlJ89vyOJW5g&gen=8",function (city_data,status) {

                localStorage.setItem("search_city_address",city_data["Response"]["View"][0]["Result"][0]["Location"]["Address"]["Label"]);


           })
           localStorage.setItem("location",location);
           var handle_error = $.get("http://api.openweathermap.org/data/2.5/weather?q="+localStorage.getItem("location")+"&APPID=f2f33dbceea19eef373a3972938b7cb1", function(data, status) {


              $("#place").text(localStorage.getItem("search_city_address"));
              //$("#datetime").text());

              $("#weather-detail").text(capitalizeFirstLetter(data["weather"][0]["description"]));
              $("#temperature").text(Math.round(data["main"]["temp"]-273.15));
              $("#celcius").addClass("active");
              localStorage.setItem("kelvin",data["main"]["temp"]);


              $("#humidity").text(data["main"]["humidity"]+"%");
              $("#wind").text(data["wind"]["speed"]+" m/s");
              $("#pressure").text(data["main"]["pressure"]+" hpa");


           }
        ) //end of get  now handling failure 404
         .fail(function() {
                var $toastContent = $('<span>sorry, city not found</span>').add($('<button id="close-btn" class="btn-flat toast-action">Close</button>'));
                Materialize.toast($toastContent, 10000);
         })


    } //end if else


    // calling diff api for forecast of next few hours

    var api_weather_forecast = "http://api.openweathermap.org/data/2.5/forecast?q="+localStorage.getItem("location")+"&APPID=f2f33dbceea19eef373a3972938b7cb1";

    var handle_error_graph = $.get(api_weather_forecast, function(api_data, status){

        var temp = [];
        var humidity = [];
        var wind = [];
        var label = [];
        var pressure = [];
        var api_item = api_data["list"]
        for(api_count = 0;api_count < 5;api_count++ ){
            label1 = api_item[api_count]["dt_txt"].substr(11,13);
            label2 = api_item[api_count]["weather"][0]["description"];

            label.push(label1+", "+label2);
            humidity.push(api_item[api_count]["main"]["humidity"]);
            wind.push(api_item[api_count]["wind"]["speed"]);
            pressure.push(api_item[api_count]["main"]["pressure"]);
            temp.push(Math.round(api_item[api_count]["main"]["temp"]-273.15));
        }





        console.log(status)
        if (status = "success"){
            var lineChartData = {
            labels: label,
            datasets: [{
                label: "Wind Speed m/s",
                borderColor: window.chartColors.blue,
                backgroundColor: window.chartColors.blue,
                fill: false,
                data: wind,
                yAxisID: "y-axis-1",
            }, {
                label: "Temp in celcius",
                borderColor: window.chartColors.orange,
                backgroundColor: window.chartColors.orange,
                fill: false,
                data: temp,
                yAxisID: "y-axis-2"
            },
                {
                label: "Humidity %",
                borderColor: window.chartColors.grey,
                backgroundColor: window.chartColors.grey,
                fill: false,
                data:humidity,
                yAxisID: "y-axis-3"
            }

            ]
        };

            var ctx = document.getElementById("myChart").getContext("2d");
            window.myLine = Chart.Line(ctx, {
                data: lineChartData,
                options: {
                    responsive: true,
                    hoverMode: 'index',
                    stacked: false,
                    title:{
                        display: true,
                        text:'Weather forecast '
                    },
                    scales: {
                        yAxes: [{
                            type: "linear",
                            display: true,
                            position: "left",
                            id: "y-axis-1",
                        }, {
                            type: "linear",
                            display: true,
                            position: "right",
                            id: "y-axis-2",

                            // grid line settings
                            gridLines: {
                                drawOnChartArea: false,
                            },
                        },
                        {
                            type: "linear",
                            display: true,
                            position: "right",
                            id: "y-axis-3",

                            // grid line settings
                            gridLines: {
                                drawOnChartArea: false,
                            },
                        }],
                    }
                }
            });

        }else{
            alert("something went wrong");
        }


 })
 .fail(function() {
               //  var $toastContent = $('<span>sorry, no forecast for your city</span>').add($('<button id="close-btn" class="btn-flat toast-action">Close</button>'));
              //  Materialize.toast($toastContent, 10000);
            console.log("your location weather was not found")
 })

}

getTodaysWeather()


$(document).on("change","#search-weather",function () {
getTodaysWeather($(this).val());
});

$(document).on("click","#close-btn",function () {
$(this).parent(".toast").remove();
})


function capitalizeFirstLetter(string) {
return string.charAt(0).toUpperCase() + string.slice(1);
}
function k2c(){
$("#temperature").text(Math.round(localStorage.getItem("kelvin")-273.15)).find("span");
$("#temp-options").find("span").removeClass("active");
$("#celcius").addClass("active");
}
function k2f(){
$("#temperature").text(Math.round((localStorage.getItem("kelvin")*5/9)-273.15));
$("#temp-options").find("span").removeClass("active");
$("#fahrenheit").addClass("active");
}
function k2k(){
$("#temperature").text(Math.round(localStorage.getItem("kelvin"))).addClass("active");
$("#temp-options").find("span").removeClass("active");
$("#kelvin").addClass("active");
}
