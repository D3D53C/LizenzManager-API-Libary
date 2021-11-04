import requests

class LizenzManager:
    def __init__(self, server, key, secret):
        self.server = server
        self.key = key 
        self.secret = secret

# Utilitys
    def basicget(self, endpoint,data = ""):
        return requests.get("http://" + self.server + endpoint + data, auth=(self.key, self.secret))

    def basicput(self, endpoint, mydata, myheaders):
        return requests.post("http://" + self.server + endpoint, auth=(self.key, self.secret), headers=myheaders, data = mydata)

    def basicpost(self, endpoint, mydata, myheaders):
        return requests.post("http://" + self.server + endpoint, auth=(self.key, self.secret), headers=myheaders, data = mydata)
        

# Generators
    def getGenerators(self):
        return self.basicget(self, "/wp-json/lmfwc/v2/generators/")
    
    def getGenerator(self, generatorid):
        return self.basicget(self, "/wp-json/lmfwc/v2/generators/", generatorid)

    def creategenerator(self, name, charset, chunks, times_activated_max, separator, prefix, suffix, expires_in, chunk_length):
        data = '{ "name": '+ name + ',"charset": '+ charset + ', "chunks": '+ chunks + ', "chunk_length": '+ chunk_length + ', "times_activated_max": '+ times_activated_max + ', "separator": '+ separator + ',"suffix": '+ suffix + ',"expires_in": '+ expires_in + ', "prefix": '+ prefix + ' }'
        headers = '{Content-Type: application/json}'
        return self.basicpost(self, "/wp-json/lmfwc/v2/generators", data, headers)
    
    def creategenerator(self, generatorid, name, charset, chunks, times_activated_max, separator, prefix, suffix, expires_in, chunk_length):
        data = '{ "name": '+ name + ',"charset": '+ charset + ', "chunks": '+ chunks + ', "chunk_length": '+ chunk_length + ', "times_activated_max": '+ times_activated_max + ', "separator": '+ separator + ',"suffix": '+ suffix + ',"expires_in": '+ expires_in + ', "prefix": '+ prefix + ' }'
        headers = '{Content-Type: application/json}'
        return self.basicput(self, "/wp-json/lmfwc/v2/generators" + generatorid, data, headers)

# Licenses
    def Listlicenses(self):
        return self.basicget(self, "/wp-json/lmfwc/v2/generators/")

    def getlicense(self, lickey):
        return self.basicget(self, "/wp-json/lmfwc/v2/licenses/", lickey)
        
    def activatelicense(self, lickey):
        return self.basicget(self, "/wp-json/lmfwc/v2/licenses/activate/", lickey)
    
    def createlicense(self, productID, licKey, validfor, status, times_activated_max):
        data = '{ "product_id": '+ productID + ', "license_key": '+ licKey + ', "valid_for": '+ validfor + ', "status": '+ status + ', "times_activated_max": '+ times_activated_max + ' }'
        headers = '{Content-Type: application/json}'
        return self.basicpost(self, "/wp-json/lmfwc/v2/licenses", data, headers)

    def updatelicense(self, license, productID, licKey, validfor, status, times_activated_max, order_id):
        data = '{ "order_id": '+ order_id + ',"product_id": '+ productID + ', "license_key": '+ licKey + ', "valid_for": '+ validfor + ', "status": '+ status + ', "times_activated_max": '+ times_activated_max + ' }'
        headers = '{Content-Type: application/json}'
        return self.basicput(self, "/wp-json/lmfwc/v2/licenses/" + license, data, headers)

    def deactivatelicense(self, lickey):
        return self.basicget(self, "/wp-json/lmfwc/v2/licenses/deactivate/", lickey)
    
    def validatlicense(self, lickey):
        return self.basicget(self, "/wp-json/lmfwc/v2/licenses/validate/", lickey)
    