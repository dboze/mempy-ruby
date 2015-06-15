require 'angelo'

class NapApp < Angelo::Base
  
  task :nap do |sec, msg|
    sleep sec.to_i
    msg
  end
  
  get '/' do
    future = future(:nap, params[:sec], params[:msg])
    future.value
  end
  
end

NapApp.run!
