require "application_system_test_case"

class ProductsTest < ApplicationSystemTestCase
  setup do
    @product = products(:one)
  end

  test "visiting the index" do
    visit products_url
    assert_selector "h1", text: "Products"
  end

  test "creating a Product" do
    visit products_url
    click_on "New Product"

    fill_in "Active status", with: @product.active_status
    fill_in "Country of origin", with: @product.country_of_origin_id
    fill_in "Name", with: @product.name
    fill_in "Pcolor", with: @product.pcolor
    fill_in "Pdate", with: @product.pdate
    fill_in "Sort order", with: @product.sort_order
    click_on "Create Product"

    assert_text "Product was successfully created"
    click_on "Back"
  end

  test "updating a Product" do
    visit products_url
    click_on "Edit", match: :first

    fill_in "Active status", with: @product.active_status
    fill_in "Country of origin", with: @product.country_of_origin_id
    fill_in "Name", with: @product.name
    fill_in "Pcolor", with: @product.pcolor
    fill_in "Pdate", with: @product.pdate
    fill_in "Sort order", with: @product.sort_order
    click_on "Update Product"

    assert_text "Product was successfully updated"
    click_on "Back"
  end

  test "destroying a Product" do
    visit products_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Product was successfully destroyed"
  end
end
