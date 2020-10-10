class ProductsController < ApplicationController
before_action :authenticate_user!
  #
  autocomplete :pfeature, :name, :full => true


  #cancancan
  load_and_authorize_resource
  # before_action :set_product, only: [:show, :edit, :update, :destroy]
  #
  autocomplete :pfeature, :name, :full => true


  #cancancan
  load_and_authorize_resource

  #cancancan
  load_and_authorize_resource


  # cancancan..
  #load_and_authorize_resource :product

  # GET /products
  def index
    @q = @products.search params[:q]
    @products = @q.result.page(params[:page])
  end

  # GET /products/1
  def show
  end

  # GET /products/new
  def new
  end

  # GET /products/1/edit
  def edit
  end

  # POST /products
  def create
    respond_to do |format|
      if @product.save
        format.html { redirect_to @product, notice: t('success_create') }
        format.json { render :show, status: :created, location: @product }
      else
        format.html { render :new }
        format.json { render json: @product.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /products/1
  def update
    respond_to do |format|
      if @product.update(product_params)
        format.html { redirect_to @product, notice: t('success_update') }
        format.json { render :show, status: :ok, location: @product }
      else
        format.html { render :edit }
        format.json { render json: @product.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /products/1
  def destroy
    @product.destroy
    respond_to do |format|
      format.html { redirect_to products_url, notice: t('success_destroy') }
      format.json { head :no_content }
    end
  end

  private

  # Only allow a trusted parameter "white list" through.
  def product_params
    params.require(:product).permit(:name, :pcolor, :country_of_origin_id, :pdate, :active_status, :sort_order, :pfeature_ids=> [])
  end
end
