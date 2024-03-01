# Gerando qrcode

Este repositório contém um código em __Python__ para __gerar QR codes de forma simples e rápida__. 

É usado a biblioteca qrcode para criar os QR codes a partir de dados fornecidos pelo usuário, como URLs, texto ou informações de contato. 

# Como usar:
1. Primeiro você precisa ter instalado em sua máquina o [Python](https://www.python.org/) e [VSCode](https://code.visualstudio.com/).
3. Abra o terminal do VSCode.
4. Instale a biblioteca qrcode executando o seguinte comando: pip install qrcode
5. Dentro da URL (que está o meu github) troque pela URL que quiser gerar o código

   ``img = qrcode.make("https://github.com/ivana-christ/")``
8. O nome do qrcode está sendo salvo como "qr.png"
 
   ``img.save("qr.png", "PNG")``
11. __PRONTO__!
