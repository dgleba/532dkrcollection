class Product3sController < ApplicationController
before_action :authenticate_user!

  #cancancan
  load_and_authorize_resource
  # before_action :set_product3, only: [:show, :edit, :update, :destroy]

  #cancancan
  load_and_authorize_resource

  #cancancan
  load_and_authorize_resource


  # cancancan..
  #load_and_authorize_resource :product3

  # GET /product3s
  def index
    # @q = @product3s.search params[:q]
    # @product3s = @q.result.page(params[:page])
    @product3s = Product3.ppf
    
    #@recname = "#{@product3s.name}"

  end

  # GET /product3s/1
  def show
  end

  # GET /product3s/new
  def new
  end

  # GET /product3s/1/edit
  def edit
  end

  # POST /product3s
  def create
    respond_to do |format|
      if @product3.save
        format.html { redirect_to @product3, notice: t('success_create') }
        format.json { render :show, status: :created, location: @product3 }
      else
        format.html { render :new }
        format.json { render json: @product3.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /product3s/1
  def update
    respond_to do |format|
      if @product3.update(product3_params)
        format.html { redirect_to @product3, notice: t('success_update') }
        format.json { render :show, status: :ok, location: @product3 }
      else
        format.html { render :edit }
        format.json { render json: @product3.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /product3s/1
  def destroy
    @product3.destroy
    respond_to do |format|
      format.html { redirect_to product3s_url, notice: t('success_destroy') }
      format.json { head :no_content }
    end
  end

  private

  # Only allow a trusted parameter "white list" through.
  def product3_params
    params.require(:product3).permit(:name, :pdate, :active_status, :sort_order, :pfeature_id, pfid2 )
  end
end
