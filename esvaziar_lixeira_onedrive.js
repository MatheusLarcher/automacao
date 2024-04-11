const puppeteer = require('puppeteer'); // v22.0.0 or later
const os = require('os');
const usuario = os.userInfo().username;
const userDataDir = `C:\\Users\\${usuario}\\AppData\\Local\\Google\\Chrome\\User Data`;

const executablePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";


function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
    const browser = await puppeteer.launch({
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
        userDataDir: userDataDir, // Certifique-se de que 'userDataDir' está definido corretamente
        executablePath: executablePath,
        headless: false,
        locale: 'pt-BR'
    });
    const page = await browser.newPage();
    const timeout = 5000;
    page.setDefaultTimeout(timeout);

    {
        const targetPage = page;
        await targetPage.setViewport({
            width: 695,
            height: 924
        })
    }
    {
        const targetPage = page;
        const promises = [];
        const startWaitingForEvents = () => {
            promises.push(targetPage.waitForNavigation());
        }
        startWaitingForEvents();
        await targetPage.goto('https://2dconsultorescombr-my.sharepoint.com/personal/jean_2dconsultores_com_br/_layouts/15/onedrive.aspx?view=5');
        await Promise.all(promises);
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('#id__36'),
            targetPage.locator('::-p-xpath(//*[@id=\\"id__36\\"])'),
            targetPage.locator(':scope >>> #id__36'),
            targetPage.locator('::-p-text(Esvaziar lixeira)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 31,
                y: 6,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Sim) >>>> ::-p-aria([role=\\"generic\\"])'),
            targetPage.locator('button:nth-of-type(1) > span.od-Button-label'),
            targetPage.locator('::-p-xpath(//*[@id=\\"appRoot\\"]/div/div/div[3]/div[4]/div/div/div[2]/div[3]/div/div/div[2]/div[2]/div/button[1]/span[2])'),
            targetPage.locator(':scope >>> button:nth-of-type(1) > span.od-Button-label'),
            targetPage.locator('::-p-text(Sim)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 18.34375,
                y: 12,
              },
            });
    }
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria([role=\\"alert\\"]) >>>> ::-p-aria([role=\\"generic\\"])'),
            targetPage.locator('div.EmptyFolder > div:nth-of-type(1) > div'),
            targetPage.locator('::-p-xpath(//*[@id=\\"appRoot\\"]/div/div/div[2]/div/div/div[2]/div[2]/main/div/div/div/div/div[1]/div/div[3]/div[1]/div)'),
            targetPage.locator(':scope >>> div.EmptyFolder > div:nth-of-type(1) > div'),
            targetPage.locator('::-p-text(Sua lixeira está)')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 142.5,
                y: 20,
              },
            });
    }

    await browser.close();

})().catch(err => {
    console.error(err);
    process.exit(1);
});
