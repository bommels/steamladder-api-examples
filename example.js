const request = require('request-promise');

const api_key = ''; // Your API Key here
const base_url = 'https://steamladder.com/api/v1';
const steam_id = ''; // The SteamID64 you want to lookup here.

const options = {
    method: 'GET',
    uri: base_url + '/profile/' + steam_id,
    json: true,
    headers: {
        'Authorization': 'Token ' + api_key
    }
};

request(options)
    .then(function (response) {
        // Handle the response
        console.log('Worldwide XP Rank: ' + response.ladder_rank.worldwide_xp);
    })
    .catch(function (err) {
        // Deal with the error
        console.log('Something went wrong! ' + err);
    });
