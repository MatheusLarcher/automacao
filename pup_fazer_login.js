const puppeteer = require('puppeteer'); // v22.0.0 or later

const userDataDir = 'C:\\sessao';

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
    const browser = await puppeteer.launch({
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
        userDataDir: userDataDir, // Certifique-se de que 'userDataDir' está definido corretamente
        headless: false// ou 'false' se você quiser ver o navegador
    });
    const page = await browser.newPage();
    const timeout = 5000;
    page.setDefaultTimeout(timeout);

    {
        const targetPage = page;
        await targetPage.setViewport({
            width: 738,
            height: 596
        })
    }
    {
        const targetPage = page;
        const promises = [];
        const startWaitingForEvents = () => {
            promises.push(targetPage.waitForNavigation());
        }
        startWaitingForEvents();
        await targetPage.goto('https://login.microsoftonline.com/common/oauth2/v2.0/logout?client-request-id=0b689595-c5c9-491e-a518-04bc455a41f0&logout_hint=O.CiQxYzZhZWE2YS0zMmIyLTRiYWQtYmY0Zi01NDYzMzdhZTUwZDESJGM0NDgzYTM4LTgzOWEtNGI2Yi05M2U3LWU3YjRiNjYyMzkwMRoZamVhbkAyZGNvbnN1bHRvcmVzLmNvbS5iciBM');
        await Promise.all(promises);
    }
    {
        const targetPage = page;
        const promises = [];
        const startWaitingForEvents = () => {
            promises.push(targetPage.waitForNavigation());
        }
        startWaitingForEvents();
        await targetPage.goto('https://app.powerbi.com/singleSignOn?experience=power-bi&ru=https%3A%2F%2Fapp.powerbi.com%2Fgroups%2Fa2985e38-c96e-4918-9716-865be254203b%2Flist%3Fexperience%3Dpower-bi%26noSignUpCheck%3D1');
        await Promise.all(promises);
    }
    console.log("1")
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Enter email)'),
            targetPage.locator('#email'),
            targetPage.locator('::-p-xpath(//*[@id=\\"email\\"])'),
            targetPage.locator(':scope >>> #email')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 224,
                y: 23,
              },
            });
    }
    console.log("2")
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Enter email)'),
            targetPage.locator('#email'),
            targetPage.locator('::-p-xpath(//*[@id=\\"email\\"])'),
            targetPage.locator(':scope >>> #email')
        ])
            .setTimeout(timeout)
            .fill('jean@2dconsultores.com.br');
    }
    console.log("3")
    {
        const targetPage = page;
        const promises = [];
        const startWaitingForEvents = () => {
            promises.push(targetPage.waitForNavigation());
        }
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Enviar)'),
            targetPage.locator('#submitBtn'),
            targetPage.locator('::-p-xpath(//*[@id=\\"submitBtn\\"])'),
            targetPage.locator(':scope >>> #submitBtn')
        ])
            .setTimeout(timeout)
            .on('action', () => startWaitingForEvents())
            .click({
              offset: {
                x: 50,
                y: 24,
              },
            });
        await Promise.all(promises);
    }
    console.log("4")
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Insira a senha para jean@2dconsultores.com.br)'),
            targetPage.locator('#i0118'),
            targetPage.locator('::-p-xpath(//*[@id=\\"i0118\\"])'),
            targetPage.locator(':scope >>> #i0118')
        ])
            .setTimeout(timeout)
            .click({
              offset: {
                x: 303,
                y: 16.65625,
              },
            });
    }
    console.log("5")
    {
        const targetPage = page;
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Insira a senha para jean@2dconsultores.com.br)'),
            targetPage.locator('#i0118'),
            targetPage.locator('::-p-xpath(//*[@id=\\"i0118\\"])'),
            targetPage.locator(':scope >>> #i0118')
        ])
            .setTimeout(timeout)
            .fill('M@rco1972@*!&23');
    }
    console.log("6")
    {
        const targetPage = page;
        const promises = [];
        const startWaitingForEvents = () => {
            promises.push(targetPage.waitForNavigation());
        }
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Entrar)'),
            targetPage.locator('#idSIButton9'),
            targetPage.locator('::-p-xpath(//*[@id=\\"idSIButton9\\"])'),
            targetPage.locator(':scope >>> #idSIButton9')
        ])
            .setTimeout(timeout)
            .on('action', () => startWaitingForEvents())
            .click({
              offset: {
                x: 62,
                y: 13.65625,
              },
            });
        await Promise.all(promises);
    }
    console.log("7")
    {
        const targetPage = page;
        const promises = [];
        const startWaitingForEvents = () => {
            promises.push(targetPage.waitForNavigation());
        }
        await puppeteer.Locator.race([
            targetPage.locator('::-p-aria(Sim)'),
            targetPage.locator('#idSIButton9'),
            targetPage.locator('::-p-xpath(//*[@id=\\"idSIButton9\\"])'),
            targetPage.locator(':scope >>> #idSIButton9'),
            targetPage.locator('::-p-text(Sim)')
        ])
            .setTimeout(timeout)
            .on('action', () => startWaitingForEvents())
            .click({
              offset: {
                x: 79,
                y: 11.65625,
              },
            });
        await Promise.all(promises);
    }
    console.log("Login completo")

    await delay(3000);
    await browser.close();

})().catch(err => {
    console.error(err);
    process.exit(1);
});
