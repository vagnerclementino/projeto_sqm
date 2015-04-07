Um Modelo para Predição da Confiabilidade baseado em Métricas de Software
================
A qualidade do software, apesar de ser um conceito abstrato, deve ser
sempre buscada. Com a crescente complexidade dos sistemas fica cada vez
mais difícil alcançar esta propriedade. Um fator chave para a qualidade
do produto de software é a Confiabilidade. A Engenharia da
Confiabilidade de Softwares é repleta de trabalhos que visam criar um
modelo para medir a Confiabilidade. Seguinte esta tendência, este
trabalho propõe a criação de um modelo estatístico capaz de mensurar a
Confiabilidade de um software através de seus dados históricos de
falhas, bem como de suas atuais métricas. Utilizando os dados coletados
dos Bug Tracking System de cinco softwares de código aberto escritos em
Java pretende-se confrontar as taxas de Confiabilidade obtidas com os
bugs reportados na versão atual do sistema.

Contextualização 
================

A primeira preocupação no processo de desenvolvimento de um software é
aderir o seu uso com os requisitos funcionais solicitados. Não obstante,
a experiência mostra que os sistemas de sucesso são aqueles que não
relegam ao segundo plano os requisitos não funcionais. Atributos não
funcionais, tais como Adequação Funcional, Eficiência, Compatibilidade,
Usabilidade, Confiabilidade, Segurança, Manutenibilidade e Portabilidade
são características inerentes à *qualidade* do produto de
software@citeulike:10951538. Apesar do conceito de qualidade ser
abstrato, deve-se sempre buscar formas de mensurá-lo e avaliá-lo.

De acordo com a ANSI, Software Confiabilidade é pode ser definida como a
*probabilidade* de operação de produto de software sem a ocorrência de
falhas por um determinado *período de tempo* em um ambiente específico
@IEEE-610.12-1990 [@pham2007system]. A Confiabilidade é um importante
atributo da qualidade de software, todavia, é difícil de obter devido a
intrínseca complexidade dos softwares. Analisando a definição de
Confiabilidade, verifica-se que o conceito é visto como um função
probabilística dependente do tempo. Esta definição remonta a origem da
área, que em seu início apresentava-se como uma especialização da
tradicional Engenharia da Confiabilidade, cujo foco estava na análise da
durabilidade do hardware. Ao contrário do hardware, os softwares não
sofrem a influência do tempo: um sistema com design “perfeito” que não
sofra qualquer tipo de manutenção ou atualização irá executar sem falhas
para sempre. Neste contexto, verifica-se que a principal diferença entre
a Confiabilidade de Hardware e a de Software é que a segunda busca a
perfeição design, ao contrário da primeira que visa a perfeição da
montagem/fabricação.

Desde o início da Engenharia de Software processos, ferramentas e
metodologias vêm sendo criados com o objetivo de minimizar as falhas de
softwares. Apesar de todo o esforço os problemas ainda persistem. A
literatura é repleta de exemplos de problemas em softwares que
acarretaram em prejuízos financeiros e até de perdas de vidas humanas.
Um clássico exemplo é o Therac 25, uma máquina de terapia por radiação
controlada por computador, que no ano de 1986 provocou graves lesões e
mortes em pacientes devido a uma falha do seu software embutido. Cabe
ressaltar que uma alta Confiabilidade não deveria ser uma preocupação
apenas de aplicações críticas. A manutenção e evolução representa a
maior parte dos custos do software@1423995, neste sentido garantir uma
maior Confiabilidade representa redução de custos.

Apesar de sua importância, a Engenharia da Confiabilidade de Softwares
ainda está dando os seus primeiros passos. Veremos na seção
[sec:problema] um dos problemas a serem resolvidos nesta área de
pesquisa.

O Problema a ser Resolvido 
==========================

Diferentemente de outras engenharias, o processo de mediação e avaliação
dos softwares é ainda incipiente na Engenharia de Software. Questões
como *\`\`Quão bom é um software, quantitativamente?"* ainda não
produzem respostas satisfatórias. A fim de preencher esta lacuna
diversos trabalhos vêm sendo propostos com objetivo de definir threshold
de métricas de software@rttool [@csmrwcre2014b; @5609747], detectar bad
smells@7012985 e mensurar a Confiabilidade@Lyu:1996 [@srm:2000].

Os trabalhos relacionados à predição da Confiabilidade de Software podem
ser divididos entre os de *Modelos de Predição* e os dos *Modelos de
Estimação*@Lyu:2007:SRE:1253532.1254716. O primeiro grupo têm por
objetivo predizer a Confiabilidade em algum ponto do futuro com base em
dados históricos. O segundo visa estimar a Confiabilidade no presente ou
em algum ponto futuro utilizando dados atuais do processo de
desenvolvimento de software.

Apesar da grande contribuição dos trabalhos de predição da
Confiabilidade, não há um modelo que atenda todas as situações. Devido à
complexidade do inerente ao software, qualquer modelo de predição
naturalmente necessitar de algum pressuposto adicional. Ademais, existem
poucos trabalhos que consideram métricas de medição de software, tais
como Depth of Inheritance Tree (DIT), Number of Children (NOC), Coupling
between Object Classes (CBO), Lack of Cohesion of Methods (LCOM),
Weighted Methods per Class (WMC), no processo de predição da
Confiabilidade.

Solução Proposta 
================

Este documento propõe um estudo com o objetivo de formular um modelo
estatístico que possibilite mensurar Aa Confiabilidade de software
utilizando dados históricos, bem como suas respectivas métricas de
software. A taxa de confiabilidade será data ao nível de um módulo de
software. Neste trabalho, entende como módulo a separação lógica de
funcionalidades do sistema.

A fim de calcular a taxa de Confiabilidade dos sistemas, pretende-se
coletar dados de falhas de cinco programas de código aberto escritos em
Java. Os dados serão coletados diretamente do *Bug Tracking System -
BST* da aplicação. De posse dos dados de falhas, será coletados as
métricas dos softwares. Posteriormente será calculado a taxa de
confiabilidade de cada um dos módulos que compõem o sistema. O cálculo
ao nível de um módulo, se deve essencialmente pelo dificuldade em
conseguir dados de bugs em uma menor granularidade, como por exemplo ao
nível de classes ou *packages*. Estudos estão sendo realizados com o
objetivo de definir o melhor modelo estatístico a ser aplicado no
calculo da Confiabilidade. Um outro ponto em aberto neste trabalho é
quanto a escolha da ferramente para coleta das métricas de software.

Avaliação da Solução 
====================

A avaliação deste trabalho consistirá basicamente em confrontar as taxas
de confiabilidade calculadas pelo modelo proposto com os dados reais
coletados dos BST’s. Suponha um sistema $S$ composto pelos módulos
$M_1, M_2$ e $M_3$, no qual cada um dos módulo está presente nas versões
$v_0, v_1 \ldots v_n$ do software. Seja $B_i$ o conjunto de bugs
coletados na versão $v_i$ do sistema, onde $0 \leq i \leq n$. Para cada
módulo de $S$ iremos utilizando os dados em $B_0, B_1, \ldots, B_n-1$ a
fim de calcular a taxa de confiabilidade $\omega$ do módulo. A partir
dos valores obtido de $\omega$ será possível confrontar com os bugs
relatos em $B_n$, ou seja, como os dados da última versão do sistema. A
figura [fig:avalicao] exibe de forma abstrata o processo de avaliação.

![Processo de Avaliação: Visão
abstrata](./img/projeto_mes_avaliacao.png "fig:") [fig:avalicao]

Limitações e Ameaças a Validade 
===============================

Uma primeira limitação deste trabalho está no fato de não ser possível
de medir a taxa de Confiabilidade em uma granularidade menor do que um
módulo. Conforme exposto, é difícil encontrar informações sobre bugs ao
nível de classe ou package. Um outro fator limitador está relacionado ao
número de sistemas avaliados bem como a linguagem utilizado. O fato de
usar um número reduzido de sistemas desenvolvidos em uma mesma linguagem
dificulta a generalização dos resultados obtidos. Por se tratar de um
modelo estatística para o cálculo da Confiabilidade, simplificações e
outras suposições são necessárias. Todavia, está é uma ameaça comum a
validade de qualquer trabalho nesta área.
