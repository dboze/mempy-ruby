require 'celluloid/io'
require 'http'

class NapFetcher
  include Celluloid::IO

  def request_nap(msg)
    HTTP.get(
      "http://localhost:4567?sec=3&msg=#{msg}", 
      socket_class: Celluloid::IO::TCPSocket
    )
  end
  
end

fetcher = NapFetcher.new

words = %w(i am fast)

futures = []

words.each do |word|
  futures << fetcher.future.request_nap(word)
end

futures.each do |future|
  response = future.value
  puts response.body
end
