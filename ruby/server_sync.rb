require 'sinatra'

get '/' do
  sleep params[:sec].to_f
  params[:msg]
end
