const run = async (path = '/') => {
    const url = `http://127.0.0.1:8000${path}`;
    const response = await fetch(url)
    .then((result) => {
        console.log(`Response status: ${result.status}, ${result.statusText}`);
        return result.json();
    }).catch((err) => {
        console.log(`ERROR: ${url} - ` + err);
    }).finally(() => {
        console.log(`done... GET ${url}`)
    });

    console.log('RESPONSE:');
    console.log(response);

    return response;
};

module.exports = run;