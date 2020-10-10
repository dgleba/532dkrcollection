class CreateRoles < ActiveRecord::Migration[5.2]
  def change
    create_table :roles do |t|
      t.string :name
      t.string :description
      t.integer :active_status
      t.integer :sort

      t.timestamps
    end
  end
end
