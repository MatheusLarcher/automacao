const puppeteer = require('puppeteer');

const { exec } = require('child_process');
const path = require('path');
const fs = require('fs').promises;

async function findUrlsm3u8(browser, url, regex) {
    const page = await browser.newPage();
    try {        
        await page.goto(url, { waitUntil: 'networkidle2' });

        const content = await page.content();

        const m3u8Urls = content.match(regex);
        return m3u8Urls || [];
    } catch (error) {
        console.error('Error extracting M3U8 URLs:', error);

        return [];
    }
    finally{
        await page.close();
        await delay(1000);
    }
}

async function getAllHrefs(browser, url) {
    const page = await browser.newPage();
    try {
        await page.goto(url, { waitUntil: 'networkidle2' });

        const hrefs = await page.$$eval('a', anchors => anchors.map(anchor => anchor.href));
        return hrefs;
    } catch (error) {
        console.error('Error extracting hrefs:', error);
        return [];
    } finally {
        await page.close();
        await delay(2000);
    }
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


async function createDirectoryIfNotExists(directoryPath) {
    try {
        await fs.access(directoryPath);
    } catch (error) {
        await fs.mkdir(directoryPath, { recursive: true });
    }
}

async function baixa_mp4(url, nome_saida="")
{
    if(url.includes('_vtt.')){
        return;
    }

    createDirectoryIfNotExists(path.join(__dirname, 'videos'));

    let outputFileName = path.join(__dirname, 'videos', nome_saida + '.mp4');
    if(nome_saida == ""){
        outputFileName = path.join(__dirname, 'videos', url.substring(url.lastIndexOf('/') + 1).replace('.m3u8', '.mp4'));
    }

    const command = `ffmpeg -protocol_whitelist file,http,https,tcp,tls,crypto -i "${url}" -c copy "${outputFileName}"`;

    
    await appendToFile("url_m3u8.txt", command);
     
}


async function appendToFile(filePath, content) {
    try {
        // Verifica se o arquivo existe
        await fs.access(filePath);
    } catch (error) {
        // Se o arquivo não existir, cria um novo com o conteúdo fornecido
        await fs.writeFile(filePath, content + '\n');
        console.log(`Arquivo criado: ${filePath}`);
        return;
    }

    // Se o arquivo já existir, adiciona o conteúdo na linha de baixo
    await fs.appendFile(filePath, content + '\n');
    console.log(`Conteúdo adicionado ao arquivo: ${filePath}`);
}

(async () => {
    const site =  process.argv[2];

    const browser = await puppeteer.launch({
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
        userDataDir: 'sessao',
        headless: false
    });

    var sites = await getAllHrefs(browser, site);

    const regex_m3u8 = /https?:\/\/[^"'\s]+\.m3u8/g;

    var todas_url = [];
    var url_nome_video = [];

    for (const site of sites) {
        try {
            const urls_m3u8 = await findUrlsm3u8(browser, site, regex_m3u8);
            todas_url = todas_url.concat(urls_m3u8); // Correção aqui

            urls_m3u8.forEach(element => {
                url_nome_video.push({
                    'url': element, 
                    'saida_nome': site.substring(site.lastIndexOf('/') + 1)
                })
            });


        } catch (error) {
            console.error('Erro ao buscar URLs M3U8:', error);
        }
    }
    browser.close();

    url_nome_video.forEach(element => {
        baixa_mp4(element.url, element.saida_nome);
    });   

    console.log("Arquivos sendo baixados...")

})().catch(err => {
    console.error(err);
    process.exit(1);
});
