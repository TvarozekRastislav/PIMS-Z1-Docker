require 'net/http'
require 'json'

class ApiController < ApplicationController


  def index

  end
  def make_api_call
    uri = URI('http://api:80') # Replace with the actual API URL

    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = (uri.scheme == 'https')

    request = Net::HTTP::Get.new(uri)
    # You can add headers and other options here if needed

    response = http.request(request)

    if response.code == '200'
      # API call was successful, handle the response
      @response_body = JSON.parse(response.body)
      render :make_api_call
      # render json: @response_body
    else
      # Handle errors or other responses as needed
      redirect_to index_url, notice: "Zoznam je prádny najskôr vytvorte nový hod!"
    end
  end

  def show_throw
    uri = URI("http://api:80/#{params[:id]}") # Replace with the actual API URL

    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = (uri.scheme == 'https')

    request = Net::HTTP::Get.new(uri)
    # You can add headers and other options here if needed
    response = http.request(request)

    if response.code == '200'
      # API call was successful, handle the response
      @response_body = JSON.parse(response.body)
      render :show
      # render json: @response_body
    else
      # Handle errors or other responses as needed
      render json: { error: 'API request failed' }, status: :bad_request
    end
  end

  def destroy_throw
    uri = URI("http://api:80/#{params[:id]}") # Replace with the actual API URL

    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = (uri.scheme == 'https')

    request = Net::HTTP::Delete.new(uri)
    # You can add headers and other options here if needed
    response = http.request(request)

    if response.code == '200'
      # API call was successful, handle the response
      @response_body = JSON.parse(response.body)
      redirect_to index_url, notice: "Hod bol úspešne zmazaný"
      # render json: @response_body
    else
      # Handle errors or other responses as needed
      render json: { error: 'API request failed' }, status: :bad_request
    end
  end

  def make_api_call_post
      uri = URI('http://api:80') # Replace with the actual API URL

      http = Net::HTTP.new(uri.host, uri.port)
      http.use_ssl = (uri.scheme == 'https')

      request_data = {
        speed: params[:speed].to_i, # Replace with the actual speed value you want to send
        angle: params[:angle].to_i  # Replace with the actual angle value you want to send
      }

      request = Net::HTTP::Post.new(uri)
      request['Content-Type'] = 'application/json'
      request.body = request_data.to_json

      response = http.request(request)

      if response.code == '200'
        # API call was successful, handle the response
        response_body = JSON.parse(response.body)
        redirect_to api_make_api_call_url, notice: "Hod bol úspešne vytvorený"
      else
        # Handle errors or other responses as needed
        render json: { error: 'API request failed' }, status: :bad_request
      end
    end
end