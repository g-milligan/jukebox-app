const fs = require('fs');
const path = require('node:path');

const run = async (urlPath = '/', jsonFile) => {
    const fullFilePath = path.resolve(`${__dirname}/${jsonFile}`);
    if (!fs.existsSync(fullFilePath)) {
        console.log(`File does not exist! ${fullFilePath}`);
        return;
    }

    const fileContent = fs.readFileSync(fullFilePath, {encoding: 'utf-8'});
    const json = JSON.parse(fileContent);

    const url = `http://127.0.0.1:8000${urlPath}`;
    const response = await fetch(url, {
        method: 'POST',
        headers: new Headers({'content-type': 'application/json'}),
        body: JSON.stringify(json)
    })
    .then((result) => {
        console.log(`Response status: ${result.status}, ${result.statusText}`);
        return result.json();
    }).catch((err) => {
        console.log(`ERROR: ${url} - ` + err);
    }).finally((result) => {
        console.log(`done... POST ${url} with file "${jsonFile}"`);
    });

    console.log('RESPONSE:');
    console.log(response);

    return response;
};

module.exports = run;