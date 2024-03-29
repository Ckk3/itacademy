# Relatório do programa apresentado

O relatório foi feito na plataforma Overleaf, então o arquivo é dividido entre config, main e q-1, este último contendo o relatório propriamente dito. O relatório ainda conta com 5 imagens, armazenadas na pasta img.

# Transcrição

## Resumo geral do projeto
Em 10 de junho de 2021, foi enviado um exercício prático com fins avaliativos para a admissão no programa DELL IT Academy. O exercício consiste na criação de um programa, em qualquer linguagem, para implementar as seguintes funcionalidades:
* Listar todos os pontos de táxi da tabela CSV anexa;
* Informar um par de coordenadas para que possa ser efetuada uma;
* Busca de pontos próximos a essas coordenadas;
* Busca de pontos de táxi por logradouro; e
* Encerramento do programa.


## Sobre a linguagem utilizada
Escolhi a linguagem Python para poder aprender mais sobre ela enquanto crio meu programa. No início do período, estava engajada em aprender os comandos básicos (print, input, entre outros) e tentar desenvolver alguns projetos básicos mas, com o tempo passando e as provas da universidade e outros projetos tomando conta da minha agenda, resolvi deixar de lado.

Python é uma linguagem open-source de propósito geral. Desde o Ensino Médio, é um dos meus pontos de interesse em computação, sendo inclusive um dos motivos que tive para ingressar no curso de Ciência da Computação em 2019 e comparecer à conferência Python Nordeste com alguns amigos, no mesmo ano.

Por causa de sua flexibilidade e possibilidade de integração com outras linguagens e frameworks, ela chama a atenção e não deixa de ser assunto em rodas de desenvolvedores. Uma das pessoas nas quais me inspiro no meu curso a utiliza bastante, e ela sempre disse que seu lema é 'aprender ensinando'. Isso foi o suficiente para me convencer a utilizar essa linguagem no meu exercício.


## Sobre o programa desenvolvido
Tentei resumir minha submissão a um arquivo em Python (.py) e a tabela CSV enviada como anexo junto ao exercício, além deste relatório. Começo definindo minha autoria e a data de finalização do código. Em seguida, as importações de módulos: csv para leitura do arquivo anexo, sys para alguns comandos relacionados ao ambiente em que o Python está rodando, e partes de math para os comandos matemáticos exigidos pela função haversine. 

Grande parte do programa está dentro da classe Main, que é executada no fim do arquivo PY. A primeira parte consiste em uma função \_\_init\_\_, que lê o arquivo CSV através da próxima função, lerArquivo; remove o cabeçalho para uma melhor visualização dos dados; e lista todas as opções do menu, como pedido na especificação da atividade. Após realizar essas ações, a localização que o usuário irá digitar posteriormente é definida como lista, ou vetor.

A função lerArquivo, como supracitado, define os pontos de táxi como uma lista, abrindo e lendo o arquivo CSV, separando seus valores com 'enter' e ponto-e-vírgula, para que possa retorná-los e que as outras funções o possam utilizar de forma menos problemática. O menu principal é impresso de acordo com as especificações em \_\_init\_\_, e a entrada do usuário para escolher a função a ser executada é verificada até que ele digite uma opção válida. Ao fim da função, é determinada a próxima a ser executada.

A primeira função propriamente especificada a ser implementada foi a de listar todos os pontos de táxi cadastrados. Para isso, a organização prévia da tabela foi aproveitada e adequadamente impressa, com um cabeçalho mais organizado e com iniciais maiúsculas, contrastando com as do arquivo CSV original. Após a execução, retorna-se ao menu principal.

A próxima função é aquela onde o usuário informa sua localização (ou qualquer par ordenado de coordenadas dentro do que é possível ter: latitude entre -90 e +90, longitude entre -180 e +180). São feitas validações da localização dada, e se o usuário digitar o valor com vírgula, como no CSV, esta é prontamente trocada por um ponto, para facilitar operações como float. Caso isso não seja possível, é dado um aviso de 'formato inválido', assim como nas próprias coordenadas digitadas. Ao fim da execução dessa função, mais uma vez retorna-se ao menu principal.

A terceira função é a de encontrar pontos próximos à localização digitada. Para isso, verificou-se se o vetor (definido em \_\_init\_\_) foi preenchido, ou seja, se existem coordenadas cadastradas no sistema. Caso não hajam, o usuário retorna ao menu principal. Caso hajam, segue a execução, calculando a distância de cada ponto cadastrado à localização digitada, através da fórmula de haversine, dada nas especificações da tarefa. Mais uma vez, há a substituição de vírgulas por pontos para um melhor funcionamento. A seguir, os três pontos mais próximos são listados, à direita de suas respectivas distâncias à localização do usuário, em forma de tabela. Retorna-se ao menu mais uma vez.

Na função seguinte, procuramos pontos de táxi por digitação de substring parecida com o logradouro desejado. Há uma validação found, que equivale à pergunta 'Algum logradouro já foi encontrado?', e há a utilização constante de print() para pular linhas e deixar o código mais organizado. É pedido que o usuário digite 'todo ou parte do nome do logradouro' a ser pesquisado, pois a string resultante da pesquisa será colocada em letras maiúsculas (uppercase) e comparada com logradouros de toda a tabela de pontos para que se tente encontrar um logradouro cujo nome 'bata' com esta string de alguma forma, seja parcial ou totalmente. Caso esses logradouros sejam encontrados, é criada e impressa, em forma de tabela, uma lista com eles. Caso contrário, é informado ao usuário. Retorna-se ao menu principal mais uma vez.

A última função, 'quit\_system' ou 'fechar sistema', em português, dá um pequeno aviso e faz sua tarefa homônima. Nas últimas linhas do arquivo, especifico a função haversine, que funciona com cálculos envolvendo dois pares de coordenadas e o raio do planeta Terra, retornando este raio vezes a fórmula calculada nas variáveis 'a' e 'c'. Na última linha, a função menu é chamada pela primeira vez, para que, ao executar o arquivo PY, o programa funcione apropriadamente.

## Considerações finais
* Esse é o meu primeiro programa em Python com mais de 10 linhas.
* As execuções foram feitas no Visual Studio Code.
* As capturas de tela foram feitas na Ferramenta de Captura do Windows 10.
