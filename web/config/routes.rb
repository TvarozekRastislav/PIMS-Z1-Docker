Rails.application.routes.draw do
  resources :posts
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Defines the root path route ("/")
  root "api#index"
  get '/index', to: 'api#index'
  get '/api/make_api_call', to: 'api#make_api_call'
  get '/api/show_throw/:id', to: 'api#show_throw', as: "show_throw"
  get '/api/destroy_throw/:id', to: 'api#destroy_throw', as: "destroy_throw"
  get '/api/make_api_call_post', to: 'api#make_api_call_post'

end
