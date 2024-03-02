# Busca de imoveis automatica
 O projeto conciste em buscar imoveis compatives com o seu orçamento planejado (para comprar ou alugar) podendo ser incluso variações/restrições como piscina, salao de  jogos, playground etc. A idéia nasceu porque pretendo me mudar no ano que vem e quero buscar os melhores imoveis baseado no meu orçamento, provavel que eu pegue os 5 melhores de cada bairro deseajdo para evitar erros de código e assim poder compara-los. 

 Lógica de programação:
   1° Entrar no site chaves na mão ou outro similar (como quinto andar)
   2° descobrir como interagir com o formulario
   3° preencher dados como cidade desejada, preço desejado e comodidades como piscina, brinquedoteca,etc
   4° Extrair os links de cada anuncio e guardar em um df
   5° Listar quais são os mais baratos e quais tem o melhor custo beneficio 
   6° dicionario com valores estabelecidos, exp:
        {localizacao: santo andre,
        bairro: vila pires
        comodidades: (piscina, brinquedoteca, sala de jogos, academia)
        m²: 120
        quartos: 3
        bainheiro: 2
        preco: 390.000
        link: www.chavesnamao.anunciotaltaltal
        }
   7° Finalizar enviando para um xlsx ou enviar por wtts

Código a ser feito:
    ° Criar um função que faça o usuario responder os inputs necessarios para rodar a busca
    ° função de busca imovel
    ° tratar e armazenar os valores recebidos
    ° resumir principais informaçoes e enviar por wtts ou um xlsx
