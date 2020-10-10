require 'test_helper'

class Product3sControllerTest < ActionDispatch::IntegrationTest
  setup do
    @product3 = product3s(:one)
  end

  test "should get index" do
    get product3s_url
    assert_response :success
  end

  test "should get new" do
    get new_product3_url
    assert_response :success
  end

  test "should create product3" do
    assert_difference('Product3.count') do
      post product3s_url, params: { product3: { active_status: @product3.active_status, name: @product3.name, pdate: @product3.pdate, sort_order: @product3.sort_order } }
    end

    assert_redirected_to product3_url(Product3.last)
  end

  test "should show product3" do
    get product3_url(@product3)
    assert_response :success
  end

  test "should get edit" do
    get edit_product3_url(@product3)
    assert_response :success
  end

  test "should update product3" do
    patch product3_url(@product3), params: { product3: { active_status: @product3.active_status, name: @product3.name, pdate: @product3.pdate, sort_order: @product3.sort_order } }
    assert_redirected_to product3_url(@product3)
  end

  test "should destroy product3" do
    assert_difference('Product3.count', -1) do
      delete product3_url(@product3)
    end

    assert_redirected_to product3s_url
  end
end
