namespace HomeControl.Data.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class Alteracoes : DbMigration
    {
        public override void Up()
        {
            DropPrimaryKey("dbo.Embarcadoes");
            AlterColumn("dbo.Embarcadoes", "Id", c => c.Int(nullable: false, identity: true));
            AddPrimaryKey("dbo.Embarcadoes", "Id");
        }
        
        public override void Down()
        {
            DropPrimaryKey("dbo.Embarcadoes");
            AlterColumn("dbo.Embarcadoes", "Id", c => c.Int(nullable: false));
            AddPrimaryKey("dbo.Embarcadoes", "id");
        }
    }
}
