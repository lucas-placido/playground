# MongoDB Playground

Este projeto contém um ambiente Docker Compose com MongoDB configurado e dados de exemplo para uso como playground.

## 🚀 Como usar

### 1. Iniciar o ambiente

```bash
docker-compose up -d
```

### 2. Acessar o MongoDB

**Conexão via string de conexão:**
```
mongodb://admin:password123@localhost:27017/playground
```

**Interface Web (Mongo Express):**
- URL: http://localhost:8081
- Usuário: `admin`
- Senha: `admin123`

### 3. Parar o ambiente

```bash
docker-compose down
```

### 4. Limpar dados (remover volumes)

```bash
docker-compose down -v
```

## 📊 Dados de Exemplo

O ambiente inclui as seguintes collections com dados de exemplo:

### 👥 Users (4 documentos)
- Dados de usuários com informações pessoais, preferências e tags
- Campos: name, email, age, city, country, preferences, tags, etc.

### 🛍️ Products (3 documentos)
- Catálogo de produtos eletrônicos
- Campos: name, category, price, specifications, stock, etc.

### 📦 Orders (2 documentos)
- Pedidos de compra com itens e endereços
- Campos: orderNumber, userId, items, totalAmount, status, etc.

### 📝 Blog Posts (2 documentos)
- Posts de blog com comentários e métricas
- Campos: title, content, author, category, views, likes, comments, etc.

### 🏷️ Categories (4 documentos)
- Categorias para produtos e posts
- Campos: name, slug, description, parentCategory, etc.

## 🔧 Comandos Úteis

### Conectar via MongoDB Shell
```bash
docker exec -it mongodb-playground mongosh -u admin -p password123 --authenticationDatabase admin
```

### Backup dos dados
```bash
docker exec mongodb-playground mongodump --username admin --password password123 --authenticationDatabase admin --db playground --out /backup
```

### Restaurar dados
```bash
docker exec mongodb-playground mongorestore --username admin --password password123 --authenticationDatabase admin --db playground /backup/playground
```

## 📝 Exemplos de Queries

### Buscar todos os usuários ativos
```javascript
db.users.find({isActive: true})
```

### Buscar produtos por categoria
```javascript
db.products.find({category: "Electronics"})
```

### Buscar pedidos com status específico
```javascript
db.orders.find({status: "completed"})
```

### Buscar posts com mais de 1000 visualizações
```javascript
db.blog_posts.find({views: {$gt: 1000}})
```

### Agregação: Total de vendas por categoria
```javascript
db.orders.aggregate([
  {
    $unwind: "$items"
  },
  {
    $lookup: {
      from: "products",
      localField: "items.productId",
      foreignField: "_id",
      as: "product"
    }
  },
  {
    $unwind: "$product"
  },
  {
    $group: {
      _id: "$product.category",
      totalSales: { $sum: "$items.price" }
    }
  }
])
```

### Inserir um documento (insertOne)
```javascript
db.users.insertOne({
  name: "Alice",
  email: "alice@example.com",
  isActive: true,
  createdAt: new Date()
})
```

### Inserir vários documentos (insertMany)
```javascript
db.products.insertMany([
  { name: "Keyboard", category: "Electronics", price: 149.9, stock: 30 },
  { name: "Mouse", category: "Electronics", price: 79.9, stock: 50 }
])
```

### Atualizar um documento (updateOne)
```javascript
db.users.updateOne(
  { email: "alice@example.com" },
  { $set: { city: "São Paulo" }, $currentDate: { updatedAt: true } }
)
```

### Atualizar vários documentos (updateMany)
```javascript
db.products.updateMany(
  { category: "Electronics" },
  { $inc: { price: 10 }, $currentDate: { updatedAt: true } }
)
```

### Upsert (atualiza se existir, insere se não existir)
```javascript
db.users.updateOne(
  { email: "bob@example.com" },
  { $set: { name: "Bob", isActive: true }, $setOnInsert: { createdAt: new Date() } },
  { upsert: true }
)
```

### Deletar um documento (deleteOne)
```javascript
db.orders.deleteOne({ orderNumber: "ORD-1001" })
```

### Deletar vários documentos (deleteMany)
```javascript
db.blog_posts.deleteMany({ views: { $lt: 10 } })
```

### Listar bancos de dados
```javascript
show dbs
```

### Selecionar banco de dados
```javascript
use playground
```

### Listar coleções
```javascript
show collections
```

### Contar documentos
```javascript
db.users.countDocuments({ isActive: true })
```

### Projeção, ordenação e limite
```javascript
db.products
  .find({}, { name: 1, price: 1, _id: 0 })
  .sort({ price: -1 })
  .limit(5)
```

### Índices úteis
```javascript
// Índice único por email
db.users.createIndex({ email: 1 }, { unique: true })

// Ver índices da coleção
db.users.getIndexes()
```

## 🛠️ Configurações

- **MongoDB Port:** 27017
- **Mongo Express Port:** 8081
- **Database:** playground
- **Root User:** admin
- **Root Password:** password123
- **Mongo Express User:** admin
- **Mongo Express Password:** admin123

## 📁 Estrutura do Projeto

```
.
├── docker-compose.yml          # Configuração do Docker Compose
├── init-scripts/               # Scripts de inicialização
│   └── 01-init-databases.js   # Script com dados de exemplo
└── README.md                   # Este arquivo
```

## 🎯 Próximos Passos

1. Explore os dados através da interface web do Mongo Express
2. Teste diferentes queries usando o MongoDB Shell
3. Experimente com agregações e índices
4. Adicione mais dados conforme necessário
5. Use este ambiente para aprender e testar funcionalidades do MongoDB
