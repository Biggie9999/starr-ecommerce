const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();
async function main() {
  const orders = await prisma.order.findMany({ orderBy: { createdAt: 'desc' }, take: 5 });
  console.log("Recent orders:", JSON.stringify(orders, null, 2));
}
main().catch(console.error).finally(() => prisma.$disconnect());
