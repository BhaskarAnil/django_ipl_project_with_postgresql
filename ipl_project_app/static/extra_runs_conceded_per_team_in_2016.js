fetch("/extra-runs-2016/")
  .then((response) => response.json())
  .then((data) => {
    let teams = data.map((item) => item.bowling_team);
    let extraRuns = data.map((item) => item.extra_runs);
    Highcharts.chart("chart", {
      chart: {
        type: "column",
      },
      title: {
        text: "Extra runs conceded by each team in 2016",
      },
      xAxis: {
        categories: teams,
        title: {
          text: "Team",
        },
      },
      yAxis: {
        min: 0,
        title: {
          text: "Extra Runs Conceded",
        },
      },
      series: [
        {
          name: "Extra Runs",
          data: extraRuns,
        },
      ],
    });
  });
