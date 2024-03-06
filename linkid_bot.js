const puppeteer = require('puppeteer');

async function run() {
    const browser = await puppeteer.launch({
        headless: false, // Abre o navegador
        cacheEnabled: true, // Habilita o cache
        userDataDir: './cache', // Diretório para salvar os dados de cache
    });
    const page = await browser.newPage(); // Abre uma nova página
    await page.goto('https://www.linkedin.com/jobs/search/?currentJobId=3839343017&f_AL=true&keywords=python&origin=JOB_SEARCH_PAGE_JOB_FILTER&sortBy=R');

    await waitFor(2);

    await page.waitForSelector('.ember-view.jobs-search-results__list-item');
    await page.click('.ember-view.jobs-search-results__list-item');

    await waitFor(1);

    await page.waitForSelector('.jobs-apply-button');
    await page.click('.jobs-apply-button');

    //não ta pegando as divs certas
    var v = getEditableElements(page)
}

function waitFor(seconds) {
    return new Promise(resolve => {
        setTimeout(() => resolve(), seconds * 1000);
    });
}

async function getEditableElements(page) {
    await waitFor(5);
    await page.waitForSelector('.artdeco-modal__content.jobs-easy-apply-modal__content.p0.ember-view');

    const elements = await page.$$('input, textarea');

    const editableElements = await Promise.all(elements.map(async (element) => {
        const name = await page.evaluate(el => el.getAttribute('name'), element);
        const type = await page.evaluate(el => el.getAttribute('type'), element);
        return { name, type };
    }));

    return editableElements;
}

run();