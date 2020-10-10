class Product < ApplicationRecord
has_many :product_feature
  has_many :pfeature, through: :product_feature

  belongs_to :country_of_origin

  def self.pf
    # raw sql select using ...
    Product.find_by_sql \
    <<-SQL
      SELECT  products.id as id, products.name as name, product_features.pfeature_id as pfeature_id FROM products LEFT OUTER JOIN 
        product_features ON product_features.product_id = products.id 
    SQL
  end

  def to_s
    # show columns contents, not record object like:  #<Vehicle:0x007f343b3f2890> 2016-06-08  Details Edit  Delete
    # http://stackoverflow.com/questions/4829909/how-do-i-print-out-the-contents-of-an-object-in-rails-for-easy-debugging
    #"Name:#{self.name} Age:#{self.age} Weight: #{self.weight}"
    "#{id}, #{name}"
  end


end
