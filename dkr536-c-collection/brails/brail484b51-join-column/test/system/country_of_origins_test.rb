require "application_system_test_case"

class CountryOfOriginsTest < ApplicationSystemTestCase
  setup do
    @country_of_origin = country_of_origins(:one)
  end

  test "visiting the index" do
    visit country_of_origins_url
    assert_selector "h1", text: "Country Of Origins"
  end

  test "creating a Country of origin" do
    visit country_of_origins_url
    click_on "New Country Of Origin"

    fill_in "Active status", with: @country_of_origin.active_status
    fill_in "Ctype", with: @country_of_origin.ctype
    fill_in "Fdate", with: @country_of_origin.fdate
    fill_in "Name", with: @country_of_origin.name
    fill_in "Sort order", with: @country_of_origin.sort_order
    click_on "Create Country of origin"

    assert_text "Country of origin was successfully created"
    click_on "Back"
  end

  test "updating a Country of origin" do
    visit country_of_origins_url
    click_on "Edit", match: :first

    fill_in "Active status", with: @country_of_origin.active_status
    fill_in "Ctype", with: @country_of_origin.ctype
    fill_in "Fdate", with: @country_of_origin.fdate
    fill_in "Name", with: @country_of_origin.name
    fill_in "Sort order", with: @country_of_origin.sort_order
    click_on "Update Country of origin"

    assert_text "Country of origin was successfully updated"
    click_on "Back"
  end

  test "destroying a Country of origin" do
    visit country_of_origins_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Country of origin was successfully destroyed"
  end
end
