# itacademy
Meu projeto submetido para a DELL IT Academy em 2021.
A versão 1.0 NÃO foi aceita.
Haverá uma versão 1.1, reeditada enquanto eu aprendo a linguagem de programação utilizada com mais detalhe.

## Especificações

### Problema
Pontos de táxi em Porto Alegre

### Instruções para Desenvolvimento e Empacotamento
Desenvolva uma solução para o problema utilizando a linguagem/ambiente que preferir.
Mesmo que não consiga concluir, que faça apenas partes da solução ou que tenha uma
solução com erros, faça o envio e entregue o que tiver conseguido fazer.

Também deve ser enviado um arquivo em PDF com a explicação da solução. Além dessa
explicação, o arquivo também deverá conter capturas de tela demonstrando a execução e
os resultados do programa. O código-fonte deverá conter comentários do autor.

Empacote todos os arquivos em .zip e faça o envio conforme for instruído. Não utilize outros
formatos. Somente serão aceitas submissões em formato .zip.

### Descrição
A utilização de táxis no Brasil está em queda devido ao surgimento nos últimos anos dos
aplicativos de transporte. Por isso, as cooperativas e os taxistas precisaram se reinventar
adotando novas estratégias, como: geração de promoções, melhores localizações,
melhores caminhos a percorrer, entre outras.
Então para colaborar com as cooperativas e os taxistas você resolveu analisar as atuais
localizações dos pontos de táxi da cidade. E, para facilitar sua análise, você decidiu
escrever um programa para este fim.
Anexo a este documento, há um arquivo CSV com os dados dos pontos de taxi da cidade.

Você precisa implementar as seguintes funcionalidades e disponibilizá-las através de um
menu:
* **[Listar todos os pontos de taxi]** Listar na tela os dados de todos os pontos de taxi
da cidade;
* **[Informar minha localização]** Permitir que o usuário digite sua localização
geográfica. As coordenadas geográficas (latitude e longitude) devem ser fornecidas
no formato geodésico decimal, tal como os dados do arquivo de entrada fornecidos.
Exemplo: (-30,023927 e -51,219871). O programa deverá lembrar dessa
localização para as funções seguintes.
* **[Encontrar pontos próximos]** O programa deverá exibir:

a. Os 3 pontos de táxis mais próximos ao usuário;

b. A distância entre o usuário e cada ponto (o cálculo da distância deverá ser
realizado com a fórmula de Haversine – [aqui tem implementações em
diversas linguagens](http://rosettacode.org/wiki/Haversine_formula));

* **[Buscar pontos por logradouro]** Permitir que o usuário digite parte de um nome de
logradouro (rua/avenida/etc). O programa deverá exibir todos os pontos de taxi
localizados naquele logradouro
* **[Terminar o programa]** Permitir que o usuário saia do programa.

### Observações:
a) Sugere-se o desenvolvimento de um programa em modo texto/console, com um
menu com as opções enumeradas nos requisitos; não é necessário
desenvolver uma interface gráfica;

b) Juntamente a este enunciado foi fornecido um arquivo no formato CSV contendo
dados dos pontos de taxi em um formato tabular (fonte: Datapoa);

c) Você deve escrever o código que lê o arquivo e armazena os dados lidos em
memória (do jeito que você quiser).

d) Não é necessário gravar dados em nenhum formato, nem usar sistemas de bancos
de dados.

e) O programa deverá lidar com dados de entrada inválidos e informar uma mensagem
adequada caso ocorram.

Fonte de dados : http://datapoa.com.br/dataset/stpoa-sistema-de-transporte-publico-de-porto-alegre/resource/c4263013-e284-4124-a9ef-af472d7e842c

## Dicionário de dados
### Informações
|              NOME              |                               Pontos de táxi                               |
|:------------------------------:|:--------------------------------------------------------------------------:|
|            DESCRIÇÃO           |         Cadastro descritivo e georreferenciado dos pontos de táxi.         |
|         PALAVRAS-CHAVE         |                                Ponto; táxi.                                |
|       UNIDADE RESPONSÁVEL      |                                  CCO/GCOT                                  |
|          PERIODICIDADE         |                                   Diário                                   |
|             FORMATO            |                                     CSV                                    |
|        SETOR RESPONSÁVEL       |             Equipe Armazém de Dados de Mobilidade – EAMOB/CIET             |
| CHEFIA/COORDENAÇÃO RESPONSÁVEL | Marluce Albring Coutinho(marlucea.coutinho@eptc.prefpoa.com.br) Ramal 4409 |

### Dados
|     CAMPO     |                          DESCRIÇÃO                         |
|:-------------:|:----------------------------------------------------------:|
| data_extracao | Data e hora de realização da extração de dados do sistema. |
|     codigo    |                      Código do ponto.                      |
|      nome     |                       Nome do ponto.                       |
|    telefone   |                     Telefone do ponto.                     |
|   logradouro  |            Logradouro onde se localiza o ponto.            |
|     numero    |                    Número no logradouro.                   |
|    latitude   |   Coordenada geográfica (eixo Y) de localização do ponto   |
|   longitude   |   Coordenada geográfica (eixo X) de localização do ponto   |

## Relatório submetido
[Acesse a pasta Relatório para conferir o arquivo em .tex](1.0/relatorio/)

