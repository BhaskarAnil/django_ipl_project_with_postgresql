fetch("/top-economical-bowlers-2015/")
  .then((response) => response.json())
  .then((data) => {
    let bowlers = data.map((item) => item.bowler);
    let economy = data.map((item) => item.economy);
    Highcharts.chart("chart", {
      chart: {
        type: "column",
      },
      title: {
        text: "Top 10 Economical Bowlers in IPL 2015",
      },
      xAxis: {
        categories: bowlers,
        title: {
          text: "Bowler",
        },
      },
      yAxis: {
        min: 0,
        title: {
          text: "Economy Rate",
        },
      },
      series: [
        {
          name: "Economy",
          data: economy,
        },
      ],
    });
  });
