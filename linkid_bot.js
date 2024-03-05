const puppeteer = require('puppeteer');

async function run() {
    const browser = await puppeteer.launch({
        headless: false, // Abre o navegador
        cacheEnabled: true, // Habilita o cache
        userDataDir: './cache', // Diretório para salvar os dados de cache
    });
    const page = await browser.newPage(); // Abre uma nova página
    await page.goto('https://www.linkedin.com/jobs/search/?currentJobId=3839343017&f_AL=true&keywords=python&origin=JOB_SEARCH_PAGE_JOB_FILTER&sortBy=R');

    //Nao encontra a div
    await page.waitForSelector('.ember-view.jobs-search-results__list-item');

    await page.click('.ember-view.jobs-search-results__list-item');

    await page.waitForSelector('.jobs-apply-button');

    // Clica no botão
    await page.click('.jobs-apply-button');

}


run();