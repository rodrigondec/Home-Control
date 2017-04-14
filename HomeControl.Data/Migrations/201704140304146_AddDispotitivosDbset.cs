namespace HomeControl.Data.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class AddDispotitivosDbset : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.Dispositivoes",
                c => new
                    {
                        Id = c.Int(nullable: false, identity: true),
                        Ativo = c.Boolean(nullable: false),
                        Porta = c.Int(nullable: false),
                        Estado = c.Int(nullable: false),
                        Discriminator = c.String(nullable: false, maxLength: 128),
                        Comodo_Id = c.Int(),
                    })
                .PrimaryKey(t => t.Id)
                .ForeignKey("dbo.Comodoes", t => t.Comodo_Id)
                .Index(t => t.Comodo_Id);
            
        }
        
        public override void Down()
        {
            DropForeignKey("dbo.Dispositivoes", "Comodo_Id", "dbo.Comodoes");
            DropIndex("dbo.Dispositivoes", new[] { "Comodo_Id" });
            DropTable("dbo.Dispositivoes");
        }
    }
}
