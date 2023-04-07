require 'net/http'
require 'yaml'
require 'json'


data = URI( 'https://randomuser.me/api/')

res = Net::HTTP.get(data)
randomDatas = JSON.parse(res)

yamlDatas = YAML.dump(res)
File.write('randomuser.yaml', yamlDatas)