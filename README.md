# API Silvertec - Monte Seu Computador
API com a funcionalidade de selecionar as peças de montagem do computador do cliente.

## Funções da API
* Lista todos os pedidos realizados.
* Filtro dos itens por meio do campo `client`
* Detalhe de um pedido específico através do `id`. Ex http://127.0.0.1:8000/pcbuilder/10/
* Filtro por pedidos feitos por um cliente. Ex http://127.0.0.1:8000/pcbuilder/?client=TesteCliente`

# Parâmetros
* A API trabalha com a seguinte estrutura:
```json
	{
                 "client": String,
                 "processor": id,
                 "motherboard": id,
                 "memory": [id],
                 "graphic_card": id
	}
```
- `client`: Nome do cliente.
- `processador`: id do processador referente a tabela de **Produtos Disponíveis**.
- `motherboard`: id da placa referente a tabela de **Produtos Disponíveis**.
- `memory`: id da memória referente a tabela de **Produtos Disponíveis**.
- `graphic_card`: id da memória referente a tabela de **Produtos Disponíveis**.

- **Produtos Disponíveis**
| Produto  |  ID  |
| ------------------- | :--------: |
|  Processador Intel Core i5 |  1 |
|  Processador Intel Core i7 |  2 |
|  Processador AMD Athlon |  3 |
|  Processador AMD Ryzen 7 |  4 |
|  Placa Mãe Asus Prime |  10 |
|  Placa Mãe Gigabyte |  11 |
|  Placa Mãe ASRock Fatal |  12 |
|  HyperX 4GB |  20 |
|  HyperX 8GB |  21 |
|  HyperX 16GB |  22 |
|  HyperX 32GB |  23 |
|  HyperX 64GB |  24 |
|  Placa de Video Gigabyte Geforce GTX 1060 6GB |  30 |
|  Placa de Video PNY RTX 2060 6GB | 31 |
|  Placa de Video Radeon RX 580 8GB | 32 |
