const puppeteer = require('puppeteer'); // v22.0.0 or later

const userDataDir = 'C:\\sessao';

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


(async () => {
  // Lança o navegador com a sessão armazenada no diretório 'userDataDir'
  // Assim, após efetuar login uma vez, em execuções futuras a sessão já estará salva
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
    userDataDir: userDataDir, // Certifique-se de que 'userDataDir' está definido corretamente
    headless: false// ou 'false' se você quiser ver o navegador
});

  const page = await browser.newPage();

  // Acesse a URL do seu relatório do Power BI
  const url = 'https://app.powerbi.com/groups/me/reports/9a59091c-bbb7-44ed-a85f-9d883c5f1a4e/ReportSection9747662e2762ebb725a8?experience=power-bi';
  await page.goto(url, { waitUntil: 'networkidle0' });

  // Neste ponto, se não estiver logado, você deve fazer o login manualmente.
  // O puppeteer continuará aberto e você poderá interagir normalmente com a página.

  // Aguarda até que o elemento com a classe "value" seja encontrado no DOM.
  // Aqui estamos supondo que o elemento que contém "Data Atualização:" tenha a classe "value".
  await page.waitForSelector('text.value');

  // Extrai o texto
  const texto = await page.$eval('text.value', el => el.textContent);

  // Exibe o texto no console
  console.log('Texto capturado:', texto);

  // Se quiser encerrar o browser, descomente a linha abaixo
  // await browser.close();
})();
