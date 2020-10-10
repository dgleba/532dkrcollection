class Product3 < ApplicationRecord

    self.table_name  = 'products'
    # specify primary key name if it's other than id
    # self.primary_key = 'id'
    

    # this works with pfeature_id. I can't get the CASE to work. See view for FAV.

    def self.ppf
        # raw sql select using ...
        Product.find_by_sql \
        <<-SQL
          SELECT   product_features.pfeature_id as pfeature_id,
              case (product_features.pfeature_id)
                when product_features.pfeature_id >= 1 then "ffavv"
                else ""
              end as pfid2, products.*
            FROM products LEFT OUTER JOIN product_features ON product_features.product_id = products.id 
        SQL
    end
    

    # had trouble accessing pfeature_id

    def self.ppf1
      # raw sql select using ...
      Product.find_by_sql \
      <<-SQL
        SELECT  products.*, product_features.pfeature_id as pfeature_id FROM products LEFT OUTER JOIN 
          product_features ON product_features.product_id = products.id 
      SQL
    end
  


  # i had no luck access this method.

  def self.recname
    # show columns contents, not record object like:  #<Vehicle:0x007f343b3f2890> 2016-06-08  Details Edit  Delete
    # http://stackoverflow.com/questions/4829909/how-do-i-print-out-the-contents-of-an-object-in-rails-for-easy-debugging
    #"Name:#{self.name} Age:#{self.age} Weight: #{self.weight}"

    # "#{self.id},#{name},#{pfeature_id}"

    # This is not what I expected. name=product3
    "#{name},#{ppf.pfeature_id}"
  end

end
