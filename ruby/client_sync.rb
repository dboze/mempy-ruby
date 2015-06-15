require 'celluloid/io'
require 'http'

class NapFetcher
  
  def request_nap(msg)
    HTTP.get(
      "http://localhost:4567?sec=3&msg=#{msg}", 
      socket_class: Celluloid::IO::TCPSocket
    )
  end
  
end

fetcher = NapFetcher.new

words = %w(i am fast)

words.each do |word|
  response = fetcher.request_nap(word)
  puts response.body
end
