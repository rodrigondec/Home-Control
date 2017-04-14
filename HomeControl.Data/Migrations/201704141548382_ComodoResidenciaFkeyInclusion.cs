namespace HomeControl.Data.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class ComodoResidenciaFkeyInclusion : DbMigration
    {
        public override void Up()
        {
            RenameColumn(table: "dbo.Comodoes", name: "Residencia_Id", newName: "ResidenciaId");
            RenameIndex(table: "dbo.Comodoes", name: "IX_Residencia_Id", newName: "IX_ResidenciaId");
        }
        
        public override void Down()
        {
            RenameIndex(table: "dbo.Comodoes", name: "IX_ResidenciaId", newName: "IX_Residencia_Id");
            RenameColumn(table: "dbo.Comodoes", name: "ResidenciaId", newName: "Residencia_Id");
        }
    }
}
