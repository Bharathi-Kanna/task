import yaml

def fileReader(filePath):
    with open(filePath, 'r') as file:
        data = yaml.safe_load(file)
    return data

data = fileReader('randomuser.yaml')
print(data)


# output
# {"results":[{"gender":"male","name":{"title":"Mr","first":"Samuel","last":"Matthews"},"location":{"street":{"number":591,"name":"School Lane"},"city":"Dundalk","state":"Waterford","country":"Ireland","postcode":21538,"coordinates":{"latitude":"-4.2400","longitude":"-82.4973"},"timezone":{"offset":"-2:00","description":"Mid-Atlantic"}},"email":"samuel.matthews@example.com","login":{"uuid":"d960b5e2-07f1-4107-8c39-f5ef3a8e1b5d","username":"brownmeercat952","password":"sandy1","salt":"bE9fhbBY","md5":"180983af86010bb3b0fe29ec28af85f0","sha1":"83f1a298a1b2085eb1bf52cba36cc0f077fc90b1","sha256":"45c8227d1c7e01c49e14aadbeebbb50cd9641dd73f9f096ab34449b03ce81eee"},"dob":{"date":"1962-06-06T17:12:00.851Z","age":60},"registered":{"date":"2020-04-15T11:05:42.479Z","age":2},"phone":"021-658-1638","cell":"081-423-2756","id":{"name":"PPS","value":"5443017T"},"picture":{"large":"https://randomuser.me/api/portraits/men/95.jpg","medium":"https://randomuser.me/api/portraits/med/men/95.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/95.jpg"},"nat":"IE"}],"info":{"seed":"065fe078f072c19e","results":1,"page":1,"version":"1.4"}}
