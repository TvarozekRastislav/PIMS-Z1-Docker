class SouvenirsController < ApplicationController

  def index
    response = RestClient.get("https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=#{params["department_id"]}")
    object_ids = JSON.parse(response)["objectIDs"]
    @souvenirs = []
    object_ids.shuffle.each.each do |obj_id|
      response = RestClient.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/#{obj_id}")
      parse_response = JSON.parse(response)
      if !parse_response["primaryImageSmall"].empty? and !parse_response["artistDisplayName"].empty? and !parse_response["objectDate"].empty?
        attributes = { primaryImageSmall: parse_response["primaryImageSmall"],
                       title: parse_response["title"],
                       culture: parse_response["culture"],
                       objectDate: parse_response["objectDate"],
                       artistDisplayName: parse_response["artistDisplayName"] }
        @souvenirs << Souvenir.new(attributes)
      end
      break if @souvenirs.length>0
    end
  end
end
