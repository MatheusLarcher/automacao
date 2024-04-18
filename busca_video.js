const puppeteer = require('puppeteer');



async function findUrlsm3u8(url, regex) {
    const browser = await puppeteer.launch({
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
        userDataDir: 'C:\\sessao',
        headless: false
    });

    try {

        
        const page = await browser.newPage();

        await page.goto(url);

        const content = await page.content();
        const m3u8Urls = content.match(regex);

        return m3u8Urls || [];
    } catch (error) {
        console.error('Error extracting M3U8 URLs:', error);

        return [];
    }
    finally{
        await browser.close();
        delay(1000);
    }
}

async function getAllHrefs(url) {
    const browser = await puppeteer.launch({
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
        userDataDir: 'C:\\sessao',
        headless: false
    });


    try {
        const page = await browser.newPage();
        await page.goto(url, { waitUntil: 'networkidle2' });
        const hrefs = await page.$$eval('a', anchors => anchors.map(anchor => anchor.href));
        return hrefs;
    } catch (error) {
        console.error('Error extracting hrefs:', error);
        return [];
    } finally {
        await browser.close();
        delay(2000);
    }
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}



(async () => {



    const site = 'https://learn.deeplearning.ai/courses/finetuning-large-language-models/lesson/1/introduction';

    var sites = await getAllHrefs(site);

    const regex_m3u8 = /https?:\/\/[^"'\s]+\.m3u8/g;


    for (const site of sites) {
        try {
            const urls_m3u8 = await findUrlsm3u8(site, regex_m3u8);
            console.log(urls_m3u8, "  ", site);
        } catch (error) {
            console.error('Erro ao buscar URLs M3U8:', error);
        }
    }


    sites.forEach(url => console.log(url));

})().catch(err => {
    console.error(err);
    process.exit(1);
});
