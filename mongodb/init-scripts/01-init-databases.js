// Script de inicialização do MongoDB com dados de exemplo
// Este script será executado automaticamente quando o container for criado

// Usar o banco de dados playground
db = db.getSiblingDB('playground');

// ===========================================
// COLLECTION: users (Usuários)
// ===========================================
db.users.insertMany([
    {
        _id: ObjectId(),
        name: "João Silva",
        email: "joao.silva@email.com",
        age: 28,
        city: "São Paulo",
        country: "Brasil",
        createdAt: new Date(),
        isActive: true,
        preferences: {
            theme: "dark",
            language: "pt-BR",
            notifications: true
        },
        tags: ["developer", "javascript", "nodejs"]
    },
    {
        _id: ObjectId(),
        name: "Maria Santos",
        email: "maria.santos@email.com",
        age: 32,
        city: "Rio de Janeiro",
        country: "Brasil",
        createdAt: new Date(),
        isActive: true,
        preferences: {
            theme: "light",
            language: "pt-BR",
            notifications: false
        },
        tags: ["designer", "ui", "ux"]
    },
    {
        _id: ObjectId(),
        name: "Carlos Oliveira",
        email: "carlos.oliveira@email.com",
        age: 45,
        city: "Belo Horizonte",
        country: "Brasil",
        createdAt: new Date(),
        isActive: false,
        preferences: {
            theme: "dark",
            language: "en-US",
            notifications: true
        },
        tags: ["manager", "leadership", "strategy"]
    },
    {
        _id: ObjectId(),
        name: "Ana Costa",
        email: "ana.costa@email.com",
        age: 26,
        city: "Porto Alegre",
        country: "Brasil",
        createdAt: new Date(),
        isActive: true,
        preferences: {
            theme: "light",
            language: "pt-BR",
            notifications: true
        },
        tags: ["data-scientist", "python", "machine-learning"]
    }
]);

// ===========================================
// COLLECTION: products (Produtos)
// ===========================================
db.products.insertMany([
    {
        _id: ObjectId(),
        name: "Smartphone Galaxy S24",
        category: "Electronics",
        price: 2999.99,
        currency: "BRL",
        stock: 50,
        description: "Smartphone Android com câmera de 108MP",
        specifications: {
            screen: "6.2 inches",
            storage: "256GB",
            ram: "8GB",
            battery: "4000mAh"
        },
        tags: ["smartphone", "android", "samsung"],
        createdAt: new Date(),
        updatedAt: new Date(),
        isAvailable: true
    },
    {
        _id: ObjectId(),
        name: "Notebook MacBook Pro",
        category: "Electronics",
        price: 12999.99,
        currency: "BRL",
        stock: 15,
        description: "Notebook Apple com chip M3 Pro",
        specifications: {
            screen: "14 inches",
            storage: "512GB SSD",
            ram: "16GB",
            processor: "M3 Pro"
        },
        tags: ["notebook", "apple", "macbook"],
        createdAt: new Date(),
        updatedAt: new Date(),
        isAvailable: true
    },
    {
        _id: ObjectId(),
        name: "Fone de Ouvido Bluetooth",
        category: "Accessories",
        price: 299.99,
        currency: "BRL",
        stock: 100,
        description: "Fone sem fio com cancelamento de ruído",
        specifications: {
            battery: "30 horas",
            connectivity: "Bluetooth 5.0",
            weight: "250g"
        },
        tags: ["headphone", "bluetooth", "wireless"],
        createdAt: new Date(),
        updatedAt: new Date(),
        isAvailable: true
    }
]);

// ===========================================
// COLLECTION: orders (Pedidos)
// ===========================================
db.orders.insertMany([
    {
        _id: ObjectId(),
        orderNumber: "ORD-2024-001",
        userId: db.users.findOne({ email: "joao.silva@email.com" })._id,
        items: [
            {
                productId: db.products.findOne({ name: "Smartphone Galaxy S24" })._id,
                quantity: 1,
                price: 2999.99
            }
        ],
        totalAmount: 2999.99,
        currency: "BRL",
        status: "completed",
        shippingAddress: {
            street: "Rua das Flores, 123",
            city: "São Paulo",
            state: "SP",
            zipCode: "01234-567"
        },
        createdAt: new Date(),
        updatedAt: new Date()
    },
    {
        _id: ObjectId(),
        orderNumber: "ORD-2024-002",
        userId: db.users.findOne({ email: "maria.santos@email.com" })._id,
        items: [
            {
                productId: db.products.findOne({ name: "Fone de Ouvido Bluetooth" })._id,
                quantity: 2,
                price: 299.99
            }
        ],
        totalAmount: 599.98,
        currency: "BRL",
        status: "pending",
        shippingAddress: {
            street: "Av. Copacabana, 456",
            city: "Rio de Janeiro",
            state: "RJ",
            zipCode: "22000-000"
        },
        createdAt: new Date(),
        updatedAt: new Date()
    }
]);

// ===========================================
// COLLECTION: blog_posts (Posts do Blog)
// ===========================================
db.blog_posts.insertMany([
    {
        _id: ObjectId(),
        title: "Introdução ao MongoDB",
        slug: "introducao-ao-mongodb",
        content: "MongoDB é um banco de dados NoSQL orientado a documentos...",
        author: db.users.findOne({ email: "joao.silva@email.com" })._id,
        category: "Tutorial",
        tags: ["mongodb", "database", "nosql"],
        published: true,
        publishedAt: new Date(),
        views: 1250,
        likes: 45,
        comments: [
            {
                author: "Usuário Anônimo",
                content: "Excelente tutorial!",
                createdAt: new Date()
            }
        ],
        createdAt: new Date(),
        updatedAt: new Date()
    },
    {
        _id: ObjectId(),
        title: "Melhores Práticas de UI/UX",
        slug: "melhores-praticas-ui-ux",
        content: "Design de interface é fundamental para uma boa experiência do usuário...",
        author: db.users.findOne({ email: "maria.santos@email.com" })._id,
        category: "Design",
        tags: ["ui", "ux", "design"],
        published: true,
        publishedAt: new Date(),
        views: 890,
        likes: 32,
        comments: [],
        createdAt: new Date(),
        updatedAt: new Date()
    }
]);

// ===========================================
// COLLECTION: categories (Categorias)
// ===========================================
db.categories.insertMany([
    {
        _id: ObjectId(),
        name: "Electronics",
        slug: "electronics",
        description: "Produtos eletrônicos e tecnológicos",
        parentCategory: null,
        isActive: true,
        createdAt: new Date()
    },
    {
        _id: ObjectId(),
        name: "Accessories",
        slug: "accessories",
        description: "Acessórios para dispositivos eletrônicos",
        parentCategory: null,
        isActive: true,
        createdAt: new Date()
    },
    {
        _id: ObjectId(),
        name: "Tutorial",
        slug: "tutorial",
        description: "Tutoriais e guias de programação",
        parentCategory: null,
        isActive: true,
        createdAt: new Date()
    },
    {
        _id: ObjectId(),
        name: "Design",
        slug: "design",
        description: "Artigos sobre design e UX/UI",
        parentCategory: null,
        isActive: true,
        createdAt: new Date()
    }
]);

print("✅ Dados de exemplo inseridos com sucesso!");
print("📊 Collections criadas:");
print("   - users (4 documentos)");
print("   - products (3 documentos)");
print("   - orders (2 documentos)");
print("   - blog_posts (2 documentos)");
print("   - categories (4 documentos)");
print("");
print("🔗 Conexão: mongodb://admin:password123@localhost:27017/playground");
print("🌐 Interface Web: http://localhost:8081");
print("   Usuário: admin / Senha: admin123");
