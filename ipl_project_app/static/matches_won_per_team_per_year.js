fetch("/matches-won-per-team-per-year/")
  .then((response) => response.json())
  .then((data) => {
    // Get unique seasons and teams
    let seasons = [];
    let teams = [];
    data.forEach((item) => {
      if (!seasons.includes(item.season)) {
        seasons.push(item.season);
      }
      if (!teams.includes(item.winner)) {
        teams.push(item.winner);
      }
    });
    seasons = seasons.sort();
    teams = teams.sort();

    let teamData = teams.map((team) => {
      let winsBySeason = seasons.map((season) => {
        let match = data.find(
          (item) => item.season == season && item.winner == team
        );
        if (match) {
          return match.wins;
        } else {
          return 0;
        }
      });
      return {
        name: team,
        data: winsBySeason,
      };
    });
    Highcharts.chart("chart", {
      chart: {
        type: "column",
      },
      title: {
        text: "Matches Won Per Team Per Year",
      },
      xAxis: {
        categories: seasons,
        title: {
          text: "Season",
        },
      },
      yAxis: {
        min: 0,
        title: {
          text: "Matches Won",
        },
      },
      tooltip: {
        shared: true,
        valueSuffix: " wins",
      },
      plotOptions: {
        column: {
          grouping: true,
          shadow: false,
        },
      },
      series: teamData,
    });
  });
