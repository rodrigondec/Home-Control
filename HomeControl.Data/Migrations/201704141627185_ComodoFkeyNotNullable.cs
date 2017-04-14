namespace HomeControl.Data.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class ComodoFkeyNotNullable : DbMigration
    {
        public override void Up()
        {
            DropForeignKey("dbo.Comodoes", "ResidenciaId", "dbo.Residencias");
            DropIndex("dbo.Comodoes", new[] { "ResidenciaId" });
            AlterColumn("dbo.Comodoes", "ResidenciaId", c => c.Int(nullable: false));
            CreateIndex("dbo.Comodoes", "ResidenciaId");
            AddForeignKey("dbo.Comodoes", "ResidenciaId", "dbo.Residencias", "Id", cascadeDelete: true);
        }
        
        public override void Down()
        {
            DropForeignKey("dbo.Comodoes", "ResidenciaId", "dbo.Residencias");
            DropIndex("dbo.Comodoes", new[] { "ResidenciaId" });
            AlterColumn("dbo.Comodoes", "ResidenciaId", c => c.Int());
            CreateIndex("dbo.Comodoes", "ResidenciaId");
            AddForeignKey("dbo.Comodoes", "ResidenciaId", "dbo.Residencias", "Id");
        }
    }
}
