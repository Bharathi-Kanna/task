require 'httparty'

apiKey = "6773ca61db21fb3adb45c0c49d5d7a25"
puts "Enter a location (city, state, or zip code):"
location = gets.chomp
response = HTTParty.get("https://api.openweathermap.org/data/2.5/weather?q=636008&units=metric&appid=#{apiKey}")
if response.code == 200
  data = response.parsed_response
  puts "Current temperature in #{data['name']}: #{data['main']['temp']}°C"
  puts "Weather conditions: #{data['weather'][0]['description']}"
  puts "Wind speed: #{data['wind']['speed']} m/s"
  puts "Humidity: #{data['main']['humidity']}%"
else
  puts "Error getting weather data: #{response.code} - #{response.message}"
end


# sample input salem

# output
# Current temperature in Salem: 24.91°C
# Weather conditions: clear sky
# Wind speed: 2.92 m/s
# Humidity: 77%

