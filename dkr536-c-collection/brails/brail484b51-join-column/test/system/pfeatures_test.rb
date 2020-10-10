require "application_system_test_case"

class PfeaturesTest < ApplicationSystemTestCase
  setup do
    @pfeature = pfeatures(:one)
  end

  test "visiting the index" do
    visit pfeatures_url
    assert_selector "h1", text: "Pfeatures"
  end

  test "creating a Pfeature" do
    visit pfeatures_url
    click_on "New Pfeature"

    fill_in "Active status", with: @pfeature.active_status
    fill_in "Fdate", with: @pfeature.fdate
    fill_in "Name", with: @pfeature.name
    fill_in "Sort order", with: @pfeature.sort_order
    click_on "Create Pfeature"

    assert_text "Pfeature was successfully created"
    click_on "Back"
  end

  test "updating a Pfeature" do
    visit pfeatures_url
    click_on "Edit", match: :first

    fill_in "Active status", with: @pfeature.active_status
    fill_in "Fdate", with: @pfeature.fdate
    fill_in "Name", with: @pfeature.name
    fill_in "Sort order", with: @pfeature.sort_order
    click_on "Update Pfeature"

    assert_text "Pfeature was successfully updated"
    click_on "Back"
  end

  test "destroying a Pfeature" do
    visit pfeatures_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Pfeature was successfully destroyed"
  end
end
