<h1 align="center">Diffie-Hellman (DH)</h1>

<p align="center">Atividade desenvolvida em Python durante a disciplina de Segurança em Sistemas de Computação <a href="https://sites.google.com/a/ice.ufjf.br/edelbertofranco/disciplinas/gradua%C3%A7%C3%A3o/2024-1-dcc075-seguran%C3%A7a?authuser=0">DCC075</a></p>

## Conceito

O Algoritmo Diffie-Hellman (DH) é um protocolo de troca de chaves que permite que duas partes que se comunicam por um canal público estabeleçam um segredo mútuo sem que ele seja transmitido pela Internet. O DH permite que os dois usem uma chave pública para criptografar e descriptografar suas conversas ou dados usando criptografia simétrica.

Diffie-Helman é geralmente explicado por dois exemplos de partes, Alice e Bob, iniciando um diálogo. Cada um tem uma informação que deseja compartilhar, preservando seu sigilo. Para fazer isso, eles concordam com uma informação pública benigna que será misturada com a sua informação privilegiada à medida que viaja através de um canal inseguro. Os seus segredos são misturados com a informação pública, ou chave pública, e à medida que os segredos são trocados, a informação que pretendem partilhar é misturada com o segredo comum. À medida que decifram a mensagem do outro, podem extrair a informação pública e, com conhecimento do seu próprio segredo, deduzir a nova informação que foi transportada. Embora aparentemente descomplicado na descrição deste método, quando longas sequências numéricas são usadas para chaves privadas e públicas, a descriptografia por uma parte externa que tenta espionar é matematicamente inviável, mesmo com recursos consideráveis.

DH é uma das primeiras implementações práticas de criptografia assimétrica ou criptografia de chave pública (PKC). Foi publicado em 1976 por Whitfield Diffie e Martin Hellman. Outros contribuidores a quem se atribui o desenvolvimento da DH incluem Ralph Merkle e investigadores dos serviços de inteligência do Reino Unido (c. 1969).

## Ilustração
<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/DiffieHellman.png" alt="Diffie-Hellman" width="700" height="500">
</div>
