
window.addEventListener('load', setup);
const filename = 'input.txt';

async function setup() {
    // const ctx = document.getElementById('myChart').getContext('2d');
    // const globalTemps = await getData();
    // const myChart = new Chart(ctx, {
    //     type: 'line',
    //     data: {
    //       labels: globalTemps.years,
    //       datasets: [
    //         {
    //           label: 'Temperature in °C',
    //           data: globalTemps.temps,
    //           fill: false,
    //           borderColor: 'rgba(255, 99, 132, 1)',
    //           backgroundColor: 'rgba(255, 99, 132, 0.5)',
    //           borderWidth: 1
    //         }
    //       ]
    //     },
    //     options: {
    //         scales:{
    //             yAxes:[{
    //                 ticks: {
    //                     callback: function(value, index, values){
    //                         return value + "°";
    //                     }
    //                 }
    //             }]
    //         }
    //     }
    //   });
    const input = await getData(filename);
    const p1 = await part1(input);
    const p2 = await part2(input);

}

// load data of advent of code and return an array of the lines
async function getData() {
    const response = await fetch(filename);
    const data = await response.text();
    // const years=[];
    // const temps = [];
    // const rows = data.split('\n').slice(1);
    // rows.forEach(row => {
    //     const cols = row.split(',');
    //     years.push(cols[0]);
    //     temps.push(parseFloat(cols[1])+14);
    // })
    const lines = data.split('\n');
    lines.pop();
    return lines;
}

async function part1(lines) {
    let freq = 0;
    lines.forEach(element => {
        freq += parseInt(element);
    });
    console.log(freq);
    const output = "The Solution to Part 1: <b>" + freq + "</b>";
    document.getElementById('part1').innerHTML = output;
}

async function part2(lines) {
    let seen = new Set();
    //let newLines = [...lines];
    let partSums = [];

    seen.add(0);

    //convert strings to int
    let newLines = lines.map(numStr => parseInt(numStr));
    let oneRound = newLines.reduce(
        function (total, num) { return total + num; }
        , 0);
    console.log(oneRound);
    newLines.reduce(function (a, b, i) { return partSums[i] = a + b; }, 0);
    // partSums.forEach(elem =>{
    //     console.log(elem);
    // });
    //create partial sum
    let twice = false;
    let cnt = 0;
    let p2 = 0;
    while (!twice) {
 
        for (let i = 0, len = partSums.length; i < len && !twice; i++) {
            e = partSums[i];
            if (!seen.has(e))
                seen.add(e);
            else {
                console.log("Winner! " + e);
                p2 = e;
                twice = true;
                // return;
            }
        }
        // 
        for (let i = 0, len = partSums.length; i < len; i++)
            partSums[i] += oneRound;
    }
    const output = "The Solution to Part 2: <b>" + p2 + "</b>";
    document.getElementById('part2').innerHTML = output;
}