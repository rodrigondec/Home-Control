# Diagrama de classes

## ![](/Class Diagram.png)Pattern Composite

### Client, Component, Leaf, Módulo, MóduloPrivado

Essas classes são responsáveis por fazer o mapeamento da propriedade e seus respectivos ambientes.  
seguindo a estrutura composite:

* Um`Client` possui um`Component`. Esse primeiro `Component` será um `MóduloPrivado`. juntamente com o `Client` representará o _**Imóvel**_
* O `MóduloPrivado` _**Imóvel**_ terá uma lista de `Component` que representarão os ambientes
* Um ambiente _**Quintal**_ seria um `Leaf` do _**Imóvel**_
* Um ambiente _**Casa**_ seria um `Módulo` do _**Imóvel**_
  * Um sub-ambiente _**QuartoFulado**_ seria um `MóduloPrivado` da _**Casa**_
  * Um sub-ambiente _**Sala**_ seria um `Leaf` da _**Casa**_

Dessa forma fazendo a categorização dos ambientes e sub-ambientes do Imóvel em questão.

Outros exemplos:

#### Controle de uma casa

* Uma casa é uma \`propriedade\` \*\*\*residência\*\*\*

* \*\*\*residência\*\*\* tem um \`módulo público\` \*\*\*home\*\*\*

  * \*\*\*home\*\*\* terá os \`leafs\` \*\*\*sala\*\*\*, \*\*\*cozinha\*\*\*, \*\*\*jardim\*\*\*, \*\*\*entrada\*\*\* e etc

  * \*\*\*home\*\*\* terá os \`módulos privado\`\` \*\*\*quarto de fulano\*\*\*, \*\*\*quarto de cicrano\*\*\* e etc

    * \*\*\*quarto de fulano\*\*\* terá o \`leaf\` \*\*\*dispositivos quarto de fulano\*\*\*

#### Controle de um condomínio

* Um condomínio é uma \`propriedade\` \*\*\*propriedade\_condomínio\*\*\*

* \*\*\*propriedade\_condomínio\*\*\* terá o \`módulo público\` \*\*\*condomínio\*\*\*

  * \*\*\*condomínio\*\*\* terá os \`leafs\` \*\*\*jardim\*\*\*, \*\*\*piscina\*\*\*, \*\*\*sauna\*\*\*, \*\*\*entrada\*\*\* e etc

  * \*\*\*condomínio\*\*\* terá os \`módulos privados\` \*\*\*prédio a\*\*\*, \*\*\*prédio b\*\*\*, \*\*\*prédio b\*\*\* e etc

    * \*\*\*prédio a\*\*\* terá os \`leafs\` \*\*\*elevador\*\*\*, \*\*\*entrada\*\*\*, \*\*\*escada\*\*\* e etc

    * \*\*\*prédio a\*\*\* terá os \`módulos privados\` \*\*\*andar 1\*\*\*, \*\*\*andar 2\*\*\*, \*\*\*andar 3\*\*\*, \*\*\*apt 101\*\*\*, \*\*\*apto 203\*\*\* e etc

      * \*\*\*apto 101\*\*\* terá os \`leafs\` \*\*\*sala\*\*\*, \*\*\*cozinha\*\*\*, \*\*\*entrada\*\*\* e etc

      * \*\*\*apto 101\*\*\* terá os \`módulos privados\` \*\*\*quarto de fulano\*\*\*, \*\*\*quarto de cicrano\*\*\* e etc

        * \*\*\*quarto de fulano\*\*\* terá o \`leaf\` \*\*\*dispositivos quarto de fulano\*\*\*

## Pontos de extensão

### Dispositivo

#### Interruptor:

* Verificar se está ligado.
* Ligar/Desligar interruptor.

#### Sensor:

* Verificar valor atual.

#### Potênciometro:

* Alterar valor.
* Recuperar valor atual.

### Monitor

#### MonitorTurno

bla

#### MonitorAutom

bla

### Regra

bla

#### RegraMarcada

bla

#### 



