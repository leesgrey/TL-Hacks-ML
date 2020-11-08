// server.js -- File for pulling data from csv and serving it to frontend tables

const express = require("express");
const serveStatic = require("serve-static");
const {spawn} = require('child_process');
const fs = require('fs');
const neatCsv = require('neat-csv');
var port = 8000;

app = express();
app.use(serveStatic(__dirname + "/dist"))

app.get('/calc', function(req, res) {
    var result;
    const python = spawn('python', ['tempscriptname.py']);
    python.stdout.on('data', function(data) {
        result = data.toString();
    });
    python.on('close', (code) => {
        // parse result

        res.send(parsedData)
    })
})

var results;
var teamWinrates = [];
var i;

// pull in csv files and create tables
// team winrates
fs.readFile('./data/team_winrates_csv.csv', async (err, data) => {
    if (err) {
        console.error(err)
        return;
    }

    results = await neatCsv(data)
    for (i = results.length - 1; i > results.length - 11; i--) {
        results[i]['winrate'] = String(results[i]['winrate'] * 100) + "%";
        teamWinrates.push(results[i]);
    }

    // console.log(teamWinrates);
})

// champ winrates

app.get('/stats', function(req, res) {

})

app.listen(port);
console.log("server listening on port " + port);