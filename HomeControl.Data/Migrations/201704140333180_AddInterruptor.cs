namespace HomeControl.Data.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class AddInterruptor : DbMigration
    {
        public override void Up()
        {
            AddColumn("dbo.Dispositivoes", "ValorAtual", c => c.Single());
            AddColumn("dbo.Dispositivoes", "ValorMaximo", c => c.Single());
            AddColumn("dbo.Dispositivoes", "ValorMinimo", c => c.Single());
            AddColumn("dbo.Dispositivoes", "EstadoAtual", c => c.Single());
        }
        
        public override void Down()
        {
            DropColumn("dbo.Dispositivoes", "EstadoAtual");
            DropColumn("dbo.Dispositivoes", "ValorMinimo");
            DropColumn("dbo.Dispositivoes", "ValorMaximo");
            DropColumn("dbo.Dispositivoes", "ValorAtual");
        }
    }
}
