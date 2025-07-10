fetch("/matches-per-year/")
  .then((response) => response.json())
  .then((data) => {
    let seasons = data.map((item) => item.seasons);
    let matchesCount = data.map((item) => item.matches_count);
    Highcharts.chart("chart", {
      chart: {
        type: "column",
      },
      title: {
        text: "Number of matches played per year for all the years in IPL.",
      },
      xAxis: {
        categories: seasons,
        title: {
          text: "Seasons",
        },
      },
      yAxis: {
        min: 0,
        title: {
          text: "Number of Matches",
        },
      },
      series: [
        {
          name: "Matches",
          data: matchesCount,
        },
      ],
    });
  });
