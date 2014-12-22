class CreateLogs < ActiveRecord::Migration
  def change
    create_table :logs do |t|
      t.string :q1
      t.string :q2
      t.string :q3
      t.string :q4
      t.string :q5
      t.string :q6

      t.timestamps
    end
  end
end
