# Automacao Discord

Script para automacao de tarefas no Discord do cria.

## Requisitos
- Python 3+
- `discord.py`

### 1. **Instalar Dependências**

Antes de rodar o script, é necessário instalar as dependências. Use o seguinte comando para instalar as bibliotecas necessárias:

   ```sh
   pip install -r requirements.txt
   ```

### 2. **Configurar as Mensagens do Bot**

As mensagens que o bot envia estão armazenadas na lista `frases`. Para alterar as mensagens, basta modificar os itens dessa lista.

```python
frases = [
  "Mensagem personalizada 1",
  "Mensagem personalizada 2",
  "Mensagem personalizada 3"
]
```

Adicione ou remova mensagens conforme necessário.

### 3. **Configurar o Tempo entre as Mensagens**

O tempo entre as mensagens é controlado pela variável `last_time`. O bot seleciona um intervalo de tempo aleatório entre 400ms e 4000ms por padrão.

Para alterar o intervalo, modifique a linha:

```python
last_time = random.randint(400, 3600)  # Intervalo entre 0.4s e 4s
```

Se quiser um intervalo maior, altere os valores de `random.randint` para algo como:

```python
last_time = random.randint(60, 12)  # Intervalo entre 1 minuto a 1 hora
```

### 4. **Adicionar ou Trocar Contas**

Para usar uma conta diferente, basta alterar as variáveis `EMAIL` e `SENHA` com as credenciais da conta desejada:

```python
EMAIL = "novaconta@gmail.com"
SENHA = "NovaSenha123"
```

### 5. **Rodar o Bot**

Após fazer as configurações, basta rodar o script Python:

```bash
python nome_do_script.py
```

O bot irá fazer login no Discord e começar a enviar as mensagens automaticamente.

### 6. **Modo Headless (sem interface gráfica)**

Por padrão, o bot roda de forma "headless", ou seja, sem abrir o navegador na sua interface gráfica. Para rodar o bot com a interface gráfica, basta remover ou comentar a linha:

```python
options.add_argument("--headless")  # Executa sem interface gráfica
```

