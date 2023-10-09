class DepartmentsController < ApplicationController
  def index
    response =RestClient.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")

    @departments=JSON.parse(response)["departments"]
  end
end
