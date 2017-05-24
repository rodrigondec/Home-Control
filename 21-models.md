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

* Uma casa é o `MóduloPrivado` _**Residência**_ de um `Client`
  * _**Residência**_ terá os `Leafs` _**Sala**_, _**Cozinha**_, _**Jardim**_, _**Portão**_ e etc
  * _**Residência**_ terá os `MódulosPrivados` _**Quarto de fulano**_, _**Quarto de cicrano**_ e etc
    * _**Quarto de fulano**_ terá o `Leaf` _**Dispositivos quarto de fulano**_

#### Controle de um condomínio

*  Um condomínio é o `MóduloPrivado` _**Condomínio**_ de um `Client`
  *   _**Condomínio**_ terá o `MóduloPrivado` _**AreasRestritas**_
    * _**AreasRestritas**_ terá os `Leafs` _**Jardim**_, _**Piscina**_, _**Sauna**_ e etc
  * _**Condomínio**_ terá o `Leaf` _**Entrada**_ e etc
  *  _**Condomínio**_ terá os `MódulosPrivados` _**Prédio a**_, _**Prédio b**_, _**Prédio c**_ e etc
    *  _**Prédio a**_ terá os `Leafs` _**Elevador**_, _**Entrada**_, _**Escada**_ e etc
    *  _**Prédio a**_ terá os `MódulosPrivados` _**Andar 1**_, _**Andar 2**_, _**Andar 3**_, _**Apt 101**_, _**Apto 203**_ e etc
      *  _**Apto 101**_ terá os `Leafs` _**Sala**_, _**Cozinha**_, _**Entrada**_ e etc
      *  _**Apto 101**_ terá os `MódulosPrivados` _**Quarto de fulano**_, _**Quarto de cicrano**_ e etc
        * _**Quarto de fulano**_ terá o `Leaf` _**Dispositivos quarto de fulano**_

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



