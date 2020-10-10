class Product2 < ApplicationRecord

  # this model access the view...
  
  self.table_name  = 'vw_Product2'
  # specify primary key name if it's other than id
  self.primary_key = 'id'



end
